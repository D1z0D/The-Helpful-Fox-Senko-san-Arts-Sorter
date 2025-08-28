#!/bin/bash

echo "Launch installer..."

if ! command -v python3 &> /dev/null; then
    echo "Python3 not found! Install: sudo apt install python3 python3-pip"
    exit 1
fi

echo "Creating a virtual environment..."
python3 -m venv venv

echo "Activating a virtual environment..."
source venv/bin/activate

echo "Installing ultralytics and dependencies..."
pip install --upgrade pip
pip install ultralytics
pip install opencv-python numpy Pillow PyQt5

echo "Install complete!"
echo "To launch: python3 gui.py"