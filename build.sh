#!/bin/bash

echo "Starte PyInstaller für Linux"

# Pfad zum PyInstaller-Befehl (kann je nach Installation variieren)
PYINSTALLER_CMD="pyinstaller"

# Optionen für PyInstaller
NO_CONFIRM="--noconfirm"
WINDOWED="-w"
NAME="-n MorseMIDI"
ADD_DATA_UI="--add-data=MorseMIDI_Pygubu.ui:."
ADD_DATA_ICON="--add-data=icon.png:."
COLLECT_SUBMODULES="--collect-submodules=pygubu"

# Führe PyInstaller aus
$PYINSTALLER_CMD $NO_CONFIRM $WINDOWED MorseMIDI.py $NAME $ADD_DATA_UI $ADD_DATA_ICON $COLLECT_SUBMODULES

echo "PyInstaller abgeschlossen. Die ausführbare Datei sollte im Ordner 'dist' liegen."

# Optional: Aufräumen der Build-Dateien (entsprechend ::pyinstaller --clean im Batch)
# echo "Optional: Bereinige Build-Dateien"
# $PYINSTALLER_CMD --clean MorseMIDI.spec

exit 0
