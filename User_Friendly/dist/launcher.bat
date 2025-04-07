@echo off
REM Save the current directory
pushd %~dp0

REM Check if gui.py exists
if not exist gui.py (
    echo Error: gui.py not found in the current directory.
    popd
    pause
    exit /b 1
)

REM Run the Python script and check for errors
echo Running gui.py...
python gui.py
if %errorlevel% neq 0 (
    echo Error: gui.py did not run successfully. Error level: %errorlevel%
    popd
    pause
    exit /b %errorlevel%
)

REM Provide success feedback
echo gui.py ran successfully.

REM Return to the original directory
popd
pause
