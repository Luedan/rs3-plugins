@echo off
setlocal

python --version >nul 2>&1
if not errorlevel 1 (
    set "PY_EXE=python"
    goto :run
)

py --version >nul 2>&1
if not errorlevel 1 (
    set "PY_EXE=py"
    goto :run
)

if exist "C:\Program Files\GIMP 3\bin\python.exe" (
    set "PY_EXE=C:\Program Files\GIMP 3\bin\python.exe"
    goto :run
)

echo [ERROR] No se encontro un ejecutable funcional de Python en el sistema.
exit /b 1

:run
"%PY_EXE%" "%~dp0translate.py" %*
exit /b %ERRORLEVEL%
