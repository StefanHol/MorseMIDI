# MorseMIDI
This project was writen in Pyhton with the libreries [Tkinter](https://docs.python.org/3/library/tkinter.html "Tkinter") and [MidiUtils](https://pypi.org/project/MIDIUtil/ "MidiUtils"). This project converts text to Morse code in MIDI format. These MIDI files can be used to embed morse code into your music. This project was inspired by the online page "[Morse Code: MIDI & Text Generator](http://www.robertecker.com/hp/research/morse-generator.php "Morse Code: MIDI & Text Generator")" by Robert Ecker.

![MorseMIDI](https://github.com/EdgarBarranco/MorseMIDI/blob/994c2d1308aed34ad646c660498f18f708a0debe/MorseMIDI.PNG)

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
