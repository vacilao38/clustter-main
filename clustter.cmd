@echo off
setlocal
set "CLUSTTER_HOME=%~dp0"
if exist "%CLUSTTER_HOME%.local\python.txt" (
  set /p CLUSTTER_PYTHON=<"%CLUSTTER_HOME%.local\python.txt"
  goto run
)
where py >nul 2>nul
if not errorlevel 1 goto launcher
python "%CLUSTTER_HOME%sync.py" %*
exit /b %errorlevel%
:launcher
py -3 "%CLUSTTER_HOME%sync.py" %*
exit /b %errorlevel%
:run
"%CLUSTTER_PYTHON%" "%CLUSTTER_HOME%sync.py" %*
exit /b %errorlevel%
