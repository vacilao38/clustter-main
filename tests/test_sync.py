"""Integration tests use disposable local remotes, never the user's repositories."""
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

MODULE = Path(__file__).resolve().parents[1] / "sync.py"
SPEC = importlib.util.spec_from_file_location("clustter_sync", MODULE)
sync = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(sync)


class IntegrationTests(unittest.TestCase):
    def setUp(self):
        test_root = MODULE.parent / ".local" / "tests"
        test_root.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(prefix="clustter-test-", dir=test_root)
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.env = patch.dict(os.environ, {
            "GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_NOSYSTEM": "1",
            "GIT_AUTHOR_NAME": "Clustter Test", "GIT_AUTHOR_EMAIL": "test@example.invalid",
            "GIT_COMMITTER_NAME": "Clustter Test", "GIT_COMMITTER_EMAIL": "test@example.invalid",
        })
        self.env.start()
        self.addCleanup(self.env.stop)
        self.remote = self.base / "remote.git"
        self.git(self.base, "init", "--bare", "--initial-branch=main", str(self.remote))
        self.a = self.base / "pc-a"
        self.b = self.base / "pc-b"
        self.git(self.base, "clone", str(self.remote), str(self.a))
        (self.a / "README.md").write_text("início\n", encoding="utf-8")
        self.git(self.a, "add", ".")
        self.git(self.a, "commit", "-m", "initial")
        self.git(self.a, "push", "origin", "main")
        self.git(self.base, "clone", str(self.remote), str(self.b))
        self.entry = {"url": str(self.remote), "branch": "main"}

    def git(self, path, *args):
        result = subprocess.run(["git", "-C", str(path), *args], capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr.decode("utf-8", "replace"))
        return result.stdout.decode("utf-8", "replace").strip()

    def synchronize(self, path, **kwargs):
        return sync.sync_repo(path, self.entry, "test-device", **kwargs)

    def test_new_files_and_deletions_reach_second_computer(self):
        (self.a / "novo.txt").write_text("ação e café\n", encoding="utf-8")
        self.synchronize(self.a)
        self.synchronize(self.b)
        self.assertEqual((self.b / "novo.txt").read_text(encoding="utf-8"), "ação e café\n")
        (self.a / "novo.txt").unlink()
        self.synchronize(self.a)
        self.synchronize(self.b)
        self.assertFalse((self.b / "novo.txt").exists())

    def test_parallel_edits_to_different_files_are_merged(self):
        (self.a / "a.txt").write_text("A", encoding="utf-8")
        (self.b / "b.txt").write_text("B", encoding="utf-8")
        self.synchronize(self.a)
        self.synchronize(self.b)
        self.synchronize(self.a)
        self.assertTrue((self.a / "b.txt").exists())
        self.assertTrue((self.b / "a.txt").exists())

    def test_conflict_preserves_both_versions_and_uploads_rescue(self):
        (self.a / "README.md").write_text("versão A\n", encoding="utf-8")
        (self.b / "README.md").write_text("versão B\n", encoding="utf-8")
        self.synchronize(self.a)
        with self.assertRaisesRegex(sync.SyncError, "Resgate enviado"):
            self.synchronize(self.b)
        self.assertEqual((self.b / "README.md").read_text(encoding="utf-8"), "versão B\n")
        self.assertFalse((self.b / ".git" / "MERGE_HEAD").exists())
        branches = self.git(self.remote, "for-each-ref", "--format=%(refname)")
        self.assertIn("codex/sync-rescue-", branches)
        self.assertEqual(self.git(self.a, "show", "origin/main:README.md"), "versão A")

    def test_offline_checkpoint_is_sent_after_reconnection(self):
        self.git(self.a, "remote", "set-url", "origin", str(self.base / "offline.git"))
        entry = {"url": str(self.base / "offline.git"), "branch": "main"}
        (self.a / "offline.txt").write_text("preservado", encoding="utf-8")
        with self.assertRaises(sync.SyncError):
            sync.sync_repo(self.a, entry, "test-device")
        self.assertEqual(self.git(self.a, "status", "--porcelain"), "")
        self.git(self.a, "remote", "set-url", "origin", str(self.remote))
        self.synchronize(self.a)
        self.synchronize(self.b)
        self.assertEqual((self.b / "offline.txt").read_text(encoding="utf-8"), "preservado")

    def test_detects_secrets_in_existing_unpushed_commits(self):
        token = "gh" + "p_" + "A" * 36
        (self.a / "config.txt").write_text(token, encoding="utf-8")
        self.git(self.a, "add", ".")
        self.git(self.a, "commit", "-m", "unsafe local commit")
        before = self.git(self.remote, "rev-parse", "main")
        with self.assertRaisesRegex(sync.SyncError, "credencial"):
            self.synchronize(self.a)
        self.assertEqual(self.git(self.remote, "rev-parse", "main"), before)

    def test_ignored_local_data_never_reaches_remote(self):
        (self.a / ".gitignore").write_text("dados/\n.env\n", encoding="utf-8")
        (self.a / "dados").mkdir()
        (self.a / "dados" / "pessoal.db").write_bytes(b"private")
        (self.a / ".env").write_text("password=local", encoding="utf-8")
        self.synchronize(self.a)
        files = self.git(self.remote, "ls-tree", "-r", "--name-only", "main")
        self.assertNotIn("pessoal.db", files)
        self.assertNotIn(".env", files)

    def test_clean_sync_does_not_create_commits(self):
        before = self.git(self.a, "rev-parse", "HEAD")
        self.synchronize(self.a)
        self.synchronize(self.a)
        self.assertEqual(self.git(self.a, "rev-parse", "HEAD"), before)

    def test_existing_nonrepo_is_preserved(self):
        existing = self.base / "existing"
        existing.mkdir()
        (existing / "work.txt").write_text("keep", encoding="utf-8")
        with self.assertRaisesRegex(sync.SyncError, "repositório próprio"):
            self.synchronize(existing)
        self.assertEqual((existing / "work.txt").read_text(encoding="utf-8"), "keep")

    def test_branch_switch_is_not_automatic(self):
        self.git(self.a, "checkout", "-b", "codex/work")
        with self.assertRaisesRegex(sync.SyncError, "Branch diferente"):
            self.synchronize(self.a)
        self.assertEqual(self.git(self.a, "branch", "--show-current"), "codex/work")

    def test_background_waits_for_recent_edits(self):
        (self.a / "active.txt").write_text("editing", encoding="utf-8")
        self.assertEqual(self.synchronize(self.a, background=True)["status"], "aguardando-edicao")
        self.assertIn("active.txt", self.git(self.a, "status", "--porcelain"))

    def test_path_escape_is_rejected(self):
        with self.assertRaises(sync.SyncError):
            sync.safe_path(self.base, "../outside")

    def test_lock_prevents_concurrent_cycles(self):
        lock = self.base / "sync.lock"
        with sync.exclusive_lock(lock):
            with self.assertRaises(sync.SyncError):
                with sync.exclusive_lock(lock):
                    self.fail("second lock acquired")

    def test_central_clones_projects_and_repeated_cycles_are_stable(self):
        central_remote = self.base / "central.git"
        self.git(self.base, "init", "--bare", "--initial-branch=main", str(central_remote))
        central = self.base / "clustter-main"
        self.git(self.base, "clone", str(central_remote), str(central))
        manifest = {"central_url": str(central_remote), "projects": [
            dict(self.entry, id="app", path="restored-app")]}
        (central / "projects.json").write_text(json.dumps(manifest), encoding="utf-8")
        (central / ".gitignore").write_text(".local/\n", encoding="utf-8")
        self.git(central, "add", ".")
        self.git(central, "commit", "-m", "central")
        self.git(central, "push", "origin", "main")
        report = sync.sync(central, self.base)
        self.assertEqual(report["app"]["status"], "sincronizado")
        self.assertTrue((self.base / "restored-app" / "README.md").exists())
        before = self.git(central, "rev-parse", "HEAD")
        sync.sync(central, self.base)
        self.assertEqual(before, self.git(central, "rev-parse", "HEAD"))

    def test_reserved_test_url_is_allowed_but_real_host_is_blocked(self):
        dummy = b"https://" + b"user:pass@"
        sync.guard_blob("test/url_test.dart", dummy + b"example.org")
        with self.assertRaises(sync.SyncError):
            sync.guard_blob("test/url_test.dart", dummy + b"real-host.com")
        with self.assertRaises(sync.SyncError):
            sync.guard_blob("lib/config.dart", dummy + b"example.org")


if __name__ == "__main__":
    unittest.main()
