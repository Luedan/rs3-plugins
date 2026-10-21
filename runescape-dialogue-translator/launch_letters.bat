@echo off
setlocal
if "%~1"=="" (
    echo =========================================================================
    echo RuneScape Dialogue Translator - Lanzador Multi-Ventana
    echo =========================================================================
    echo Uso:
    echo   launch_letters.bat LETRA1 [LETRA2] [LETRA3] ...
    echo.
    echo Ejemplos:
    echo   launch_letters.bat C D E
    echo   launch_letters.bat C D E F G
    echo =========================================================================
    exit /b 1
)

:loop
if "%~1"=="" goto end
echo [+] Abriendo ventana dedicada para Letra %1...
start "Traductor RS - Letra %1" cmd /k ""%~dp0translate.bat" --letter %1"
shift
goto loop

:end
echo.
echo Todas las ventanas solicitadas han sido iniciadas en paralelo.
