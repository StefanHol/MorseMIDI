# MorseMIDI

This project is based on the fork of the GitHub project [EdgarBarranco/MorseMIDI](https://github.com/EdgarBarranco/MorseMIDI).

## Modifications:
- Changed GUI to Pygubu
- Added functionality to store and load settings or restore to default
- Edited MIDI code title
- Output estimation of time ticks that are needed for the MIDI code

This project was written in Python using the libraries [Tkinter](https://docs.python.org/3/library/tkinter.html) and [MIDIUtil](https://pypi.org/project/MIDIUtil/). MorseMIDI converts text to Morse code in MIDI format, allowing you to embed Morse code into your music. The inspiration for this project came from the online page "[Morse Code: MIDI & Text Generator](http://www.robertecker.com/hp/research/morse-generator.php)" by Robert Ecker.

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

Be sure you have activated the venv or installed the packages then run
``` bash
python MorseMIDI.py
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

![Linux UI](https://github.com/EdgarBarranco/MorseMIDI/blob/45a64e4814d7321f0e4b856ce113beef9194daf2/images/linux-ui.png "Linux UI")


## Screenshots in Ableton and FL Studio:
FL Studio:

![FL Studio](https://github.com/EdgarBarranco/MorseMIDI/blob/791d9e9acfa76f24ac5765676c5635ae1286b860/images/flstudi.png "Midi file in FL Studio")
