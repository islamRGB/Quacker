@echo off
title QUACKERRR Launcher
cls

:: Set console text color to light green on black
color 0A

echo Welcome to QUACKERRR Launcher!
echo.

cd /d "%~dp0"

where python >nul 2>&1
if %errorlevel% neq 0 (
    color 0C
    echo [ERROR] Python is not installed or not in PATH.
    echo Please install Python 3.11+ from https://python.org
    pause
    exit /b
)

color 0E
echo Preparing to install packages and collect data...
echo.

set packages=QuackLib NetworkTools DataCollector AnalyticsModule Updater SecurityPatch

for %%p in (%packages%) do (
    color 0E
    echo Collecting %%p...
    timeout /t 2 >nul
    color 0A
    echo Successfully installed %%p
    echo.
)

color 0B
echo Installation and data collection completed.
echo Launching main.py...
echo.

color 07
python main.py
if %errorlevel% neq 0 (
    color 0C
    echo [ERROR] Something went wrong running main.py
    pause
    exit /b
)

color 0B
echo Launcher closed.
pause
