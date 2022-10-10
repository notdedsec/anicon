@echo off
CALL venv/scripts/activate
pyinstaller -F -i ./anicon.ico ./anicon.py
