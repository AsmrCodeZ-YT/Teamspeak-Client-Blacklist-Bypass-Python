@echo off
REM Builds TS3-Bypass.exe (single file, asks for Administrator on launch).
REM Creates and activates a virtual environment (.venv) so nothing is installed globally.
REM Requirements: Python 3.8+ installed and on PATH (python.org installer, tick "Add to PATH").

cd /d "%~dp0"

if not exist ".venv\Scripts\activate.bat" (
    echo Creating virtual environment...
    python -m venv .venv
    if errorlevel 1 goto :fail
)

call ".venv\Scripts\activate.bat"
if errorlevel 1 goto :fail

python -m pip install --upgrade pip pyinstaller
if errorlevel 1 goto :fail

python -m PyInstaller --onefile --uac-admin --console --name TS3-Bypass ts-bypass.py
if errorlevel 1 goto :fail

call deactivate

echo.
echo Done. Your exe is at: %~dp0dist\TS3-Bypass.exe
pause
exit /b 0

:fail
echo.
echo Build failed. See the messages above.
pause
exit /b 1
