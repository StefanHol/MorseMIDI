# MorseMIDI

This project is based on the fork of the GitHub project [EdgarBarranco/MorseMIDI](https://github.com/EdgarBarranco/MorseMIDI).

This project was written in Python using the libraries [Tkinter](https://docs.python.org/3/library/tkinter.html) and [MIDIUtil](https://pypi.org/project/MIDIUtil/). MorseMIDI converts text to Morse code in MIDI format, allowing you to embed Morse code into your music. The inspiration for this project came from the online page "[Morse Code: MIDI & Text Generator](http://www.robertecker.com/hp/research/morse-generator.php)" by Robert Ecker.

## Modifications:
- Changed GUI to Pygubu
- Input fields instead of sliders

## Features
- Input fields to change MIDI parameters
- Input Text to be converted
- MIDI code title can be changed
- Calc output estimation of time ticks that are needed for the MIDI code
- Store and load settings as JSON file
- Restore to default
- Selectable themes

## Open ToDos:
- Store selected theme
- Check timing calcutaion and output for beats and resolutions

## Create Virtualenvironment and install requirements

**Create the venv**
``` bash
python -m venv venv
```

**Start Virtualenvironment on Windows and install requirements**
``` bash
venv\Scripts\activate
pip3 install -r requirements.txt
```

**Start Virtualenvironment on Linux and install requirements**
``` bash
source ./venv/bin/activate
pip3 install -r requirements.txt
```

## Run

Be sure you have activated the venv or installed the packages then run.

Windows:
``` bash
venv\Scripts\activate
python MorseMIDI.py
```

Linux
``` bash
source ./venv/bin/activate
python3 MorseMIDI.py
```


# The Tool

International Morse Code encodes 26 letters, numbers from zero to nine, and a subset of special characters such as periods, comas, etc. An interval of silence equivalent to the length of the short signal is used to maintain the spacing between each dot or dash signal. An interval of silence equivalent to three short signals is used to maintain the spacing between each letter. Additionally, an interval of silence equivalent to seven short signals is used to maintain the spacing between each word. This encoding has been implemented using the UI.

The UI offers the following options:

- Volume:
Default 100. it is the velocity of the node. DAWs will use this as audio level.
- Note:
Default 80. MIDI note to use for the tones.
- BPM:
Default 120. BPM to encode MIDI file.
- Time Resolution:
Default 480. Co-relates to Words Per Minute.
- Dot length:
Default 110. Length of the Morse Code "DOT".
- Dash length:
Default 230. Length of the Morse Code "DASH".
- Silence between marks:
Default 10. Length of the silence between DOT or DASH.
- Silence between letters:
Default 130. Length of the silence between letters.
- Silence between words:
Default 250. Length of the silence between words.
- Textbox:
Type whatever you want to convert to morse in this box.
- Convert & Save button:
Save file dialog will be shown to save the newly created MIDI file.
- Calc-Length button:
Calculate the expected length for the time resolution

## UI screenshots:

File Menu:

![File Menu at Windows UI](https://github.com/StefanHol/MorseMIDI/blob/main/images/File_Menu.png "File Menu at Windows UI")

Windows UI:

![Windows UI](https://github.com/StefanHol/MorseMIDI/blob/main/images/windows-ui_default.png "Windows 10 UI")

Linux UI:

![Linux UI](https://github.com/StefanHol/MorseMIDI/blob/main/images/linux-ui.png "Linux UI")

![Linux UI darkly](https://github.com/StefanHol/MorseMIDI/blob/main/images/linux-ui_darkly_theme.png "Linux UI darkly")


## Screenshots in Ardour and Bitwig Studio:

Ardour:

![FL Studio](https://github.com/StefanHol/MorseMIDI/blob/main/images/ardour.png "Midi file in Ardour")

Bitwig:

![FL Studio](https://github.com/StefanHol/MorseMIDI/blob/main/images/bitwig.png "Midi file in Bitwig Studio")



# Create executable
## For Windows

If you want to build an EXE-File for Windows

1. Activate `venv` see above
2. install pyinstaller
    ```
    pip install -r requirements_to_build.txt
    ```
3. ``build.bat`` will build the MorseMIDI.exe for you
    - Output will be stored in ``dist\MorseMIDI`` folder


## For Linux

If you want to build an executable for Linux

1. Activate `venv` see above
2. install pyinstaller
    ```
    pip install -r requirements_to_build.txt
    ```
3. ``chmod +x ./build.sh``
4. ``build.sh`` will build the executable ``MorseMIDI`` for you
    - Output will be stored in ``dist/MorseMIDI`` folder

