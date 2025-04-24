@echo off
echo Activate venv
call venv\Scripts\activate.bat

echo Run pyinstaller
call pyinstaller --noconfirm -w MorseMIDI.py -n MorseMIDI --add-data="MorseMIDI_Pygubu.ui;." --add-data="icon.ico;." --collect-submodules pygubu
::pyinstaller --clean MorseMIDI.spec

echo deactivate venv
call deactivate

echo keep cmd open and wait for user
call pause
