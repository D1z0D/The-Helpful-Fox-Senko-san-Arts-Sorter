@echo off
echo Установка приложения Senko Model...
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo Python not found! Download Python 3.8+ from python.org
    pause
    exit /b 1
)

echo Creating a virtual environment...
python -m venv venv

echo Activating a virtual environment...
call venv\Scripts\activate.bat

echo Installing ultralytics and dependencies...
pip install --upgrade pip
pip install ultralytics
pip install opencv-python numpy Pillow PyQt5

echo Install complete!
echo To launch: python gui.py
pause