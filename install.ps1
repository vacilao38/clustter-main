param(
    [string]$PythonPath,
    [switch]$Uninstall
)
$ErrorActionPreference = 'Stop'
$centralPath = $PSScriptRoot
$workspacePath = Split-Path -Parent $centralPath
$localPath = Join-Path $centralPath '.local'
$utf8 = New-Object System.Text.UTF8Encoding($false)
$utf8Bom = New-Object System.Text.UTF8Encoding($true)
$hashProvider = [Security.Cryptography.SHA256]::Create()
$taskSuffix = ([BitConverter]::ToString($hashProvider.ComputeHash($utf8.GetBytes($centralPath.ToLowerInvariant())))).Replace('-','').Substring(0,10)
$taskName = 'Clustter-Sync-' + $taskSuffix
$startupPath = Join-Path ([Environment]::GetFolderPath('Startup')) ($taskName + '.lnk')
if ($Uninstall) {
    Unregister-ScheduledTask -TaskName $taskName -Confirm:$false -ErrorAction SilentlyContinue
    if (Test-Path -LiteralPath $startupPath) { Remove-Item -LiteralPath $startupPath }
    Write-Output 'Agendamento removido; projetos preservados.'
    exit 0
}
if (-not (Get-Command git -ErrorAction SilentlyContinue)) { throw 'Instale Git para Windows primeiro.' }
if (-not $PythonPath) {
    $launcher = Get-Command py -ErrorAction SilentlyContinue
    if ($launcher) { $PythonPath = & $launcher.Source -3 -c 'import sys; print(sys.executable)' }
    else {
        $pythonCommand = Get-Command python -ErrorAction SilentlyContinue
        if ($pythonCommand) { $PythonPath = & $pythonCommand.Source -c 'import sys; print(sys.executable)' }
    }
}
if (-not $PythonPath -or -not (Test-Path -LiteralPath $PythonPath)) { throw 'Instale Python 3.10+ ou use -PythonPath com o executável.' }
& $PythonPath -c 'import sys; sys.exit(0 if sys.version_info >= (3,10) else 1)'
if ($LASTEXITCODE -ne 0) { throw 'Python 3.10 ou superior é necessário.' }
$gitName = git config user.name
$gitEmail = git config user.email
if (-not $gitName -or -not $gitEmail) { throw 'Configure git config --global user.name e user.email antes de instalar.' }
[IO.Directory]::CreateDirectory($localPath) | Out-Null
[IO.File]::WriteAllText((Join-Path $localPath 'python.txt'), $PythonPath, $utf8)
$workspaceAgents = Join-Path $workspacePath 'AGENTS.md'
if (-not (Test-Path -LiteralPath $workspaceAgents)) {
    $instructions = @'
# Clustter
- Usar UTF-8.
- Ler clustter-main/AGENTS.md, projects.json, PENDENCIAS.md e o handoff do projeto antes de trabalhar.
- Executar clustter-main/clustter.cmd sync ao iniciar e encerrar; registrar falhas e conflitos.
- Atualizar clustter-main/handoffs/<id>.md com resultado, testes e próximo passo.
- Cada app/ferramenta da Clustter tem repositório próprio público por padrão, salvo exceção documentada; cadastrar em projects.json. Não abrir projetos externos à família.
- Nunca publicar dados ou segredos. Publicação no catálogo exige pedido explícito.
'@
    [IO.File]::WriteAllText($workspaceAgents, $instructions, $utf8)
}
# Store paths safely as literals inside a local script; never interpolate into shell code.
$pythonLiteral = $PythonPath.Replace("'", "''")
$scriptLiteral = (Join-Path $centralPath 'sync.py').Replace("'", "''")
$logLiteral = (Join-Path $localPath 'sync.log').Replace("'", "''")
$runnerPath = Join-Path $localPath 'run-sync.ps1'
$runner = "`$env:PYTHONUTF8='1'`r`nif ((Test-Path -LiteralPath '$logLiteral') -and (Get-Item -LiteralPath '$logLiteral').Length -gt 2MB) { Move-Item -LiteralPath '$logLiteral' -Destination '$logLiteral.previous' -Force }`r`n& '$pythonLiteral' '$scriptLiteral' sync --background *>> '$logLiteral'`r`nexit `$LASTEXITCODE`r`n"
[IO.File]::WriteAllText($runnerPath, $runner, $utf8Bom)
$psExecutable = Join-Path $env:SystemRoot 'System32\WindowsPowerShell\v1.0\powershell.exe'
$arguments = '-NoProfile -NonInteractive -WindowStyle Hidden -ExecutionPolicy Bypass -File "' + $runnerPath + '"'
try {
    $action = New-ScheduledTaskAction -Execute $psExecutable -Argument $arguments -WorkingDirectory $centralPath
    $logon = New-ScheduledTaskTrigger -AtLogOn -User ([Security.Principal.WindowsIdentity]::GetCurrent().Name)
    $settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -MultipleInstances IgnoreNew -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -ExecutionTimeLimit (New-TimeSpan -Minutes 20)
    $principal = New-ScheduledTaskPrincipal -UserId ([Security.Principal.WindowsIdentity]::GetCurrent().Name) -LogonType Interactive -RunLevel Limited
    Register-ScheduledTask -TaskName $taskName -Action $action -Trigger $logon -Settings $settings -Principal $principal -Force | Out-Null
    if (Test-Path -LiteralPath $startupPath) { Remove-Item -LiteralPath $startupPath }
    Write-Output ('Agendamento ativo: ' + $taskName + ' (somente entrada no Windows).')
} catch {
    # Standard users may lack Task Scheduler registration. Run once at logon.
    $shortcut = (New-Object -ComObject WScript.Shell).CreateShortcut($startupPath)
    $shortcut.TargetPath = $psExecutable
    $shortcut.Arguments = $arguments
    $shortcut.WorkingDirectory = $centralPath
    $shortcut.WindowStyle = 7
    $shortcut.Save()
    Write-Output 'Inicialização por usuário ativa, somente uma vez ao entrar no Windows.'
}
& (Join-Path $centralPath 'update-schedule.ps1')
if ($LASTEXITCODE -ne 0) { throw 'Não foi possível remover um agendamento periódico anterior.' }
& $PythonPath (Join-Path $centralPath 'sync.py') sync
if ($LASTEXITCODE -ne 0) { throw 'Instalado, mas há pendências de sincronização. Confira .local/status.json e autenticação GitHub.' }
Write-Output 'Clustter pronta neste computador. Execute doctor para verificar os SDKs.'
