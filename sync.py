#!/usr/bin/env python3
"""Small Git coordinator; Python standard library only, all text is UTF-8."""
from __future__ import annotations

import argparse
import contextlib
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import socket
import subprocess
import sys
import time


ROOT = Path(__file__).resolve().parent
SECRET = re.compile(
    rb"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"
    rb"|\bgh[pousr]_[A-Za-z0-9]{30,}\b"
    rb"|\bgithub_pat_[A-Za-z0-9_]{30,}\b"
    rb"|\bAKIA[A-Z0-9]{16}\b"
    rb"|\bsk-(?:proj-)?[A-Za-z0-9_-]{40,}\b"
    rb"|https?://[^\s/@:]+:[^\s/@]+@"
)
DENIED_DIRS = {".local", ".openai", ".codex", ".agents", ".venv", "node_modules",
               "build", "dist", "dist-system", "outputs", "dados", "vault",
               ".dart_tool", "__pycache__", "bin", "obj", ".tools", ".packages"}
DENIED_SUFFIXES = {".pem", ".key", ".pfx", ".p12", ".jks", ".keystore", ".db",
                   ".sqlite", ".sqlite3", ".exe", ".apk", ".aab", ".zip", ".log"}


class SyncError(Exception):
    pass


def run(args, cwd=None, check=True, timeout=120):
    env = dict(os.environ, GIT_TERMINAL_PROMPT="0", GCM_INTERACTIVE="never",
               GIT_MERGE_AUTOEDIT="no", GIT_EDITOR="true", GIT_LFS_SKIP_SMUDGE="1")
    result = subprocess.run(args, cwd=cwd, env=env, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, timeout=timeout)
    if check and result.returncode:
        # Keep remote messages (which might contain credentials) out of shared reports.
        command = " ".join(str(a) for a in args[:3])
        raise SyncError(f"Falhou: {command} (código {result.returncode}). Consulte o Git local.")
    return result


def git(path, *args, check=True):
    return run(["git", "-C", str(path), *args], check=check)


def value(path, *args):
    return git(path, *args).stdout.decode("utf-8", "replace").strip()


def paths(data):
    return [part.decode("utf-8") for part in data.split(b"\0") if part]


def json_write(path, content):
    payload = json.dumps(content, ensure_ascii=False, indent=2) + "\n"
    if path.exists() and path.read_text(encoding="utf-8") == payload:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(payload, encoding="utf-8")
    temporary.replace(path)


@contextlib.contextmanager
def exclusive_lock(path):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a+b") as handle:
        handle.seek(0)
        if os.name == "nt":
            import msvcrt
            if path.stat().st_size == 0:
                handle.write(b"0")
                handle.flush()
            handle.seek(0)
            try:
                msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
            except OSError:
                raise SyncError("Outra sincronização está em execução.") from None
        else:
            import fcntl
            try:
                fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except OSError:
                raise SyncError("Outra sincronização está em execução.") from None
        try:
            yield
        finally:
            handle.seek(0)
            if os.name == "nt":
                msvcrt.locking(handle.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                fcntl.flock(handle, fcntl.LOCK_UN)


def safe_path(workspace, relative):
    path = (workspace / relative).resolve()
    if path == workspace or not path.is_relative_to(workspace):
        raise SyncError("Pasta de projeto precisa estar dentro do workspace.")
    return path


def guard_blob(name, data, allow_dist=False):
    path = Path(name)
    parts = {part.lower() for part in path.parts}
    denied_dirs = DENIED_DIRS - {"dist"} if allow_dist else DENIED_DIRS
    if parts & denied_dirs or path.suffix.lower() in DENIED_SUFFIXES:
        raise SyncError(f"Arquivo fora da política de sincronização: {name}")
    if (path.name == ".env" or path.name.startswith(".env.")) and not path.name.endswith((".example", ".sample")):
        raise SyncError(f"Arquivo de ambiente não permitido: {name}")
    if path.name.lower() in {"local.properties", "key.properties", "credentials.json"}:
        raise SyncError(f"Configuração local/credencial não permitida: {name}")
    if len(data) > 90 * 1024 * 1024:
        raise SyncError(f"Arquivo maior que 90 MiB: {name}")
    for match in SECRET.finditer(data):
        # URL-validation fixtures may deliberately contain dummy credentials.
        # Exempt only test files and reserved example/invalid hosts, never real hosts/tokens.
        if match.group().startswith(b"http") and parts & {"test", "tests", "integration_test"}:
            host = re.match(rb"[A-Za-z0-9.-]+", data[match.end():])
            if host and host.group().lower() in {b"example.com", b"example.org", b"example.net", b"example.invalid", b"localhost"}:
                continue
        raise SyncError(f"Possível credencial encontrada: {name}. Revise antes de enviar.")


def check_index(path, allow_dist=False):
    changed = paths(git(path, "diff", "--cached", "--name-only", "--diff-filter=ACMRT", "-z").stdout)
    for name in changed:
        mode = value(path, "ls-files", "-s", "--", name).split(" ", 1)[0]
        if mode in {"120000", "160000"}:
            raise SyncError(f"Link ou repositório aninhado exige revisão: {name}")
        guard_blob(name, git(path, "show", f":{name}").stdout, allow_dist)


def check_outgoing(path, remote_exists, allow_dist=False):
    revs = ["HEAD", "--not", "--remotes=origin"] if remote_exists else ["HEAD"]
    commits = value(path, "rev-list", *revs).splitlines()
    seen = set()
    for commit in commits:
        changed = paths(git(path, "diff-tree", "--root", "--no-commit-id", "--name-only",
                            "--diff-filter=ACMRT", "-r", "-m", "-z", commit).stdout)
        for name in changed:
            blob = value(path, "rev-parse", f"{commit}:{name}")
            if (name, blob) not in seen:
                guard_blob(name, git(path, "show", f"{commit}:{name}").stdout, allow_dist)
                seen.add((name, blob))


def same_remote(left, right):
    def normalize(url):
        return url.removesuffix(".git").rstrip("/").replace("git@github.com:", "https://github.com/")
    return normalize(left) == normalize(right)


def sync_repo(path, entry, device, background=False):
    branch, remote = entry["branch"], entry["url"]
    allow_dist = entry.get("allow_dist", False)
    # Ref validation also prevents option-like branch names in commands below.
    if branch.startswith("-") or git(ROOT, "check-ref-format", "--branch", branch, check=False).returncode:
        raise SyncError("Branch inválida no inventário.")
    if not path.exists():
        run(["git", "clone", "--branch", branch, "--", remote, str(path)], timeout=300)
    if not (path / ".git").exists() or Path(value(path, "rev-parse", "--show-toplevel")).resolve() != path.resolve():
        raise SyncError("Pasta existente sem repositório próprio. Não será substituída.")
    if not same_remote(value(path, "remote", "get-url", "origin"), remote):
        raise SyncError("Origin difere do inventário. Verifique antes de sincronizar.")
    if value(path, "symbolic-ref", "--short", "HEAD") != branch:
        raise SyncError(f"Branch diferente de {branch}. Nenhum checkout automático foi feito.")
    gitdir = Path(value(path, "rev-parse", "--absolute-git-dir"))
    for marker in ("index.lock", "MERGE_HEAD", "rebase-merge", "rebase-apply", "CHERRY_PICK_HEAD", "REVERT_HEAD", "sequencer"):
        if (gitdir / marker).exists():
            raise SyncError("Operação Git em andamento; finalize antes de sincronizar.")
    if git(path, "ls-files", "-u").stdout:
        raise SyncError("Existem conflitos locais não resolvidos.")
    dirty = git(path, "status", "--porcelain", "-z").stdout
    if dirty:
        names = set(paths(git(path, "diff", "--name-only", "-z", "HEAD").stdout))
        names.update(paths(git(path, "ls-files", "--others", "--exclude-standard", "-z").stdout))
        if background:
            recent = [name for name in names if (path / name).exists()
                      and time.time() - (path / name).lstat().st_mtime < 30]
            if recent:
                return {"status": "aguardando-edicao", "branch": branch}
        # Check before staging, then check the exact index snapshot to close the read/stage gap.
        for name in names:
            file = path / name
            if file.is_symlink():
                raise SyncError(f"Link exige revisão: {name}")
            if file.is_file():
                guard_blob(name, file.read_bytes(), allow_dist)
        git(path, "add", "--all", "--", ".")
        check_index(path, allow_dist)
        if git(path, "diff", "--cached", "--quiet", check=False).returncode == 1:
            git(path, "commit", "-m", f"sync: checkpoint {device}")
    # A writer may have changed files after staging. Do not merge over new work.
    if git(path, "status", "--porcelain", "-z").stdout:
        raise SyncError("Arquivos mudaram durante o checkpoint; nova tentativa no próximo ciclo.")
    git(path, "fetch", "origin")
    target = f"refs/remotes/origin/{branch}"
    remote_exists = git(path, "show-ref", "--verify", "--quiet", target, check=False).returncode == 0
    check_outgoing(path, remote_exists, allow_dist)
    if remote_exists:
        merged = git(path, "merge", "--no-edit", target, check=False)
        if merged.returncode:
            # Only abort the merge we started, after making a clean local checkpoint.
            if (gitdir / "MERGE_HEAD").exists():
                git(path, "merge", "--abort")
            # Repeated timer runs for the same conflict reuse one rescue branch.
            rescue = f"codex/sync-rescue-{device}-{value(path, 'rev-parse', 'HEAD')[:12]}"
            saved = git(path, "push", "origin", f"HEAD:refs/heads/{rescue}", check=False).returncode == 0
            detail = f"Resgate enviado: {rescue}" if saved else "Checkpoint preservado localmente; envio de resgate pendente."
            raise SyncError(f"Integração interrompida. {detail}")
    # Push is never forced. Another machine winning a race simply postpones this push.
    git(path, "push", "--set-upstream", "origin", f"HEAD:refs/heads/{branch}")
    return {"status": "sincronizado", "branch": branch, "head": value(path, "rev-parse", "HEAD")}


def attempt(path, entry, device, background):
    try:
        return sync_repo(path, entry, device, background)
    except (SyncError, subprocess.TimeoutExpired, OSError, UnicodeError) as error:
        return {"status": "pendente", "detail": str(error) if isinstance(error, SyncError)
                else f"Falha local/rede: {type(error).__name__}"}


def selected_projects(root, manifest):
    selection_file = root / ".local" / "project-selection.json"
    if not selection_file.exists():
        return manifest["projects"]
    selection = json.loads(selection_file.read_text(encoding="utf-8"))
    included = selection.get("include") if isinstance(selection, dict) else None
    if not isinstance(included, list) or not all(isinstance(item, str) for item in included):
        raise SyncError("Seleção local precisa de uma lista include de IDs de projetos.")
    known = {entry["id"] for entry in manifest["projects"]}
    if set(included) - known:
        raise SyncError("Seleção local contém projeto ausente do inventário; revise .local/project-selection.json.")
    return [entry for entry in manifest["projects"] if entry["id"] in included]


def sync(root, workspace, background=False):
    local = root / ".local"
    device_file = local / "device.txt"
    if not device_file.exists():
        local.mkdir(exist_ok=True)
        device_file.write_text(hashlib.sha256(socket.gethostname().encode()).hexdigest()[:10], encoding="utf-8")
    device = device_file.read_text(encoding="utf-8").strip()
    manifest = json.loads((root / "projects.json").read_text(encoding="utf-8"))
    central = {"url": manifest["central_url"], "branch": "main"}
    with exclusive_lock(local / "sync.lock"):
        # Reject invalid local selections before any repository operation.
        selected_projects(root, manifest)
        central_state = attempt(root, central, device, background)
        # If offline, the last local inventory still lets each app make a checkpoint.
        manifest = json.loads((root / "projects.json").read_text(encoding="utf-8"))
        report = {}
        known_paths = {root.resolve()}
        for entry in selected_projects(root, manifest):
            try:
                path = safe_path(workspace, entry["path"])
                if path in known_paths or any(path.is_relative_to(other) or other.is_relative_to(path) for other in known_paths):
                    raise SyncError("Pastas de repositórios sobrepostas no inventário.")
                known_paths.add(path)
                report[entry["id"]] = attempt(path, entry, device, background)
            except (SyncError, KeyError, ValueError) as error:
                report[entry.get("id", "inventario")] = {"status": "pendente", "detail": str(error)}
        # No timestamps or central hashes: unchanged cycles create no new commits.
        json_write(root / "devices" / f"{device}.json", report)
        report["central"] = attempt(root, central, device, False)
        json_write(local / "status.json", report)
        return report


def doctor(root):
    manifest = json.loads((root / "projects.json").read_text(encoding="utf-8"))
    projects = selected_projects(root, manifest)
    checks = {"git": ["git", "--version"], "python": [sys.executable, "--version"]}
    requirements = " ".join(item for entry in projects for item in entry["requirements"]).lower()
    for label, keyword, command in (
        ("flutter", "flutter", ["flutter", "--version"]),
        ("java", "java", ["java", "-version"]),
        ("dotnet", ".net", ["dotnet", "--version"]),
        ("tesseract", "tesseract", ["tesseract", "--version"]),
    ):
        if keyword in requirements:
            checks[label] = command
    for name, command in checks.items():
        executable = shutil.which(command[0])
        if not executable:
            print(f"{name}: AUSENTE")
            continue
        # .bat files require cmd.exe on Windows; no user-controlled command text.
        args = [executable, *command[1:]]
        if os.name == "nt" and executable.lower().endswith((".bat", ".cmd")):
            args = ["cmd.exe", "/d", "/c", *args]
        try:
            result = run(args, check=False, timeout=30)
            lines = (result.stdout + result.stderr).decode("utf-8", "replace").strip().splitlines()
            print(f"{name}: {lines[0] if lines else 'sem resposta'}")
        except (OSError, subprocess.TimeoutExpired):
            print(f"{name}: erro ao verificar")
    for entry in projects:
        print(f"\n{entry['id']}: {', '.join(entry['requirements'])}")
        print("  Preparar: " + " ; ".join(entry["setup"]))
        print("  Validar: " + " ; ".join(entry["validate"]))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["sync", "doctor"], nargs="?", default="sync")
    parser.add_argument("--background", action="store_true")
    parser.add_argument("--workspace", type=Path, default=ROOT.parent)
    args = parser.parse_args()
    if args.command == "doctor":
        doctor(ROOT)
        return 0
    try:
        report = sync(ROOT, args.workspace.resolve(), args.background)
    except (SyncError, OSError, ValueError, KeyError) as error:
        print(f"Clustter: {error}", file=sys.stderr)
        return 1
    for name, state in report.items():
        print(f"{name}: {state['status']}" + (f" — {state['detail']}" if "detail" in state else ""))
    return 1 if any(item["status"] == "pendente" for item in report.values()) else 0


if __name__ == "__main__":
    raise SystemExit(main())
