# Idempotent migration for existing installations: no timer, only logon.
$ErrorActionPreference = 'Stop'
$utf8 = New-Object Text.UTF8Encoding($false)
$hash = [Security.Cryptography.SHA256]::Create()
$suffix = ([BitConverter]::ToString($hash.ComputeHash($utf8.GetBytes($PSScriptRoot.ToLowerInvariant())))).Replace('-','').Substring(0,10)
$taskName = 'Clustter-Sync-' + $suffix
$task = @(Get-ScheduledTask -ErrorAction Stop | Where-Object TaskName -eq $taskName)
if ($task.Count -gt 0) {
    $logon = @($task[0].Triggers | Where-Object { $_.CimClass.CimClassName -eq 'MSFT_TaskLogonTrigger' })
    if ($logon.Count -eq 0) {
        $logon = @(New-ScheduledTaskTrigger -AtLogOn -User ([Security.Principal.WindowsIdentity]::GetCurrent().Name))
    }
    if (@($task[0].Triggers).Count -ne $logon.Count) {
        Set-ScheduledTask -TaskName $taskName -Trigger $logon | Out-Null
    }
}
$localPath = Join-Path $PSScriptRoot '.local'
$runnerPath = Join-Path $localPath 'run-sync.ps1'
$watcherPath = Join-Path $localPath 'watch.ps1'
$shortcutPath = Join-Path ([Environment]::GetFolderPath('Startup')) ($taskName + '.lnk')
if (Test-Path -LiteralPath $shortcutPath) {
    $shortcut = (New-Object -ComObject WScript.Shell).CreateShortcut($shortcutPath)
    $shortcut.Arguments = '-NoProfile -NonInteractive -WindowStyle Hidden -ExecutionPolicy Bypass -File "' + $runnerPath + '"'
    $shortcut.Save()
}
# Stop only the old watcher belonging to this installation; active sync children can finish.
if (Test-Path -LiteralPath $watcherPath) {
    $watchPattern = '(?i)-File\s+"?' + [regex]::Escape($watcherPath) + '"?(?:\s|$)'
    Get-CimInstance Win32_Process -Filter "Name='powershell.exe' OR Name='pwsh.exe'" | Where-Object {
        $_.ProcessId -ne $PID -and $_.CommandLine -match $watchPattern
    } | ForEach-Object { Stop-Process -Id $_.ProcessId -ErrorAction Stop }
}
[IO.Directory]::CreateDirectory($localPath) | Out-Null
[IO.File]::WriteAllText((Join-Path $localPath 'schedule-logon-only-v1'), 'ok', $utf8)
Write-Output 'Clustter: sincronização periódica removida; somente entrada no Windows e comando manual.'
exit 0
