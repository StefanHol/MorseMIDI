# MorseMIDI
This project was writen in Pyhton using the libreries [Tkinter](https://docs.python.org/3/library/tkinter.html "Tkinter") and [MidiUtils](https://pypi.org/project/MIDIUtil/ "MidiUtils"). This project converts text to Morse code in MIDI format. These MIDI files can be used to embed morse code into your music. This project was inspired by the online page "[Morse Code: MIDI & Text Generator](http://www.robertecker.com/hp/research/morse-generator.php "Morse Code: MIDI & Text Generator")" by Robert Ecker. 

In most cases after installing the latest version of python, you will need to run: 
``` 
pip3 install midiutil
```

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
Default 58. Length of the Morse Code "DOT".
- Dash length:
Default 174. Length of the Morse Code "DASH".
- Silence between marks:
Default 58. Length of the silence between DOT or DASH.
- Silence between letters:
Default 174. Length of the silence between letters.
- Silence between words:
Default 406. Length of the silence between words.
- Textbox:
Type whatever you want to convert to morse in this box.
- Convert button:
Save file dialog will be shown to save the newly created MIDI file.

## UI screenshots:
Windows UI:

![Windows UI](https://github.com/EdgarBarranco/MorseMIDI/blob/7e6d9649ec1b5a382322de3e2825918d4ce451e9/images/windows-ui.png "Windows 10 UI")

Linux UI:

![Linux UI](https://github.com/EdgarBarranco/MorseMIDI/blob/45a64e4814d7321f0e4b856ce113beef9194daf2/images/linux-ui.png "Linux UI")

macOS UI:

![macOS UI](https://github.com/EdgarBarranco/MorseMIDI/blob/6dca719784b34738065cdf6149de23c987487c7a/images/macos-ui.png "macOS Monterey UI")

## Screenshots in Ableton and FL Studio:
Ableton:

![Ableton](https://github.com/EdgarBarranco/MorseMIDI/blob/791d9e9acfa76f24ac5765676c5635ae1286b860/images/ableton.png "Midi file in Ableton Live")

FL Studio:

![FL Studio](https://github.com/EdgarBarranco/MorseMIDI/blob/791d9e9acfa76f24ac5765676c5635ae1286b860/images/flstudi.png "Midi file in FL Studio")
