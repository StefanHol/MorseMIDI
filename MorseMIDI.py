from tkinter import filedialog
from tkinter import *
from midiutil import MIDIFile


def morse_to_midi(t, volume, n, bpm, tr, dot, dash, marks, letters, words):
    # print(t, volume, note, bpm, tr, dot, dash, marks, letters, words)
    t = t.replace('\n', " ")
    morse = english_morse(t)
    # print(morse)
    total_time = 0
    for i in morse:
        if i == '.':
            total_time += dot + marks
        elif i == '-':
            total_time += dash + marks
        elif i == '|':
            total_time += words
        elif i == ' ':
            total_time += letters
    print(total_time)
    my_midi = MIDIFile(1)
    my_midi.addTempo(track=0, time=0, tempo=bpm)
    my_midi.addTrackName(track=0, time=0, trackName="Morse Code")

    time = 0
    for i in morse:
        if i == '.':
            my_midi.addNote(track=0, channel=0, pitch=n, time=time, duration=(dot/tr), volume=volume)
            time += (dot / tr) + (marks / tr)
        elif i == '-':
            my_midi.addNote(track=0, channel=0, pitch=n, time=time, duration=(dash/tr), volume=volume)
            time += (dash / tr) + (marks / tr)
        elif i == '|':
            my_midi.addNote(track=0, channel=0, pitch=0, time=time, duration=(words/tr), volume=0)
            time += (words / tr) - (marks / tr)
        elif i == ' ':
            my_midi.addNote(track=0, channel=0, pitch=0, time=time, duration=(letters/tr), volume=0)
            time += (letters / tr) - (marks / tr)

    file = filedialog.asksaveasfile(mode='wb', defaultextension=".mid", filetypes=[("Midi Files", "*.mid")],
                                    initialfile="Morse_Code.mid")
    if file is None:
        return
    my_midi.writeFile(file)


def english_morse(t):
    mcode = {
            ' ': '/', 'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
            'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
            'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
            '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-',
            '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', '"': '.-..-.', '=': '-...-',
            '+': '.-.-.', '@': '.--.-.', ':': '---...', ';': '-.-.-', '_': '..--.-', '$': '.-...', '!': '-.-.--',
            '&': '.-...-', '%': '---..-', '#': '--.--', '*': '-..-.', '\'': '.----.', '\n': ''
    }
    divided = t.split(' ')
    string = ''
    for word in divided:
        for letter in word:
            if letter in mcode:
                string += mcode[letter]
                string += ' '
            else:
                string += '?'
        string = string[:-1]
        string += '|'
    return string[:-1]


main = Tk()
main.title("Morse Code to MIDI")
# main.iconbitmap('icon.ico')     # icon for the window. Comment to build binary with pyinstaller
main.geometry("600x400")
main.resizable(FALSE, FALSE)

Label(main, text="Volume:").grid(row=0, column=0, sticky=W)
vol = Scale(main, from_=0, to=127, orient=HORIZONTAL, length=200)
vol.grid(row=0, column=1)
vol.set(100)

Label(main, text="Note:").grid(row=1, column=0, sticky=W)
note = Scale(main, from_=1, to=127, orient=HORIZONTAL, length=200)
note.grid(row=1, column=1)
note.set(80)

Label(main, text="BPM:").grid(row=2, column=0, sticky=W)
bpmValue = Scale(main, from_=0, to=999, orient=HORIZONTAL, length=200)
bpmValue.grid(row=2, column=1)
bpmValue.set(120)

Label(main, text="Time Resolution:").grid(row=3, column=0, sticky=W)
timeResolution = Scale(main, from_=0, to=9999, orient=HORIZONTAL, length=200)
timeResolution.grid(row=3, column=1)
timeResolution.set(480)

Label(main, text="Dot length:").grid(row=4, column=0, sticky=W)
dotLength = Scale(main, from_=0, to=9999, orient=HORIZONTAL, length=200)
dotLength.grid(row=4, column=1)
dotLength.set(58)

Label(main, text="Dash length:").grid(row=5, column=0, sticky=W)
dashLength = Scale(main, from_=0, to=9999, orient=HORIZONTAL, length=200)
dashLength.grid(row=5, column=1)
dashLength.set(174)

Label(main, text="Silence between marks:", anchor="w").grid(row=6, column=0, sticky=W)
gapMarks = Scale(main, from_=0, to=9999, orient=HORIZONTAL, length=200)
gapMarks.grid(row=6, column=1)
gapMarks.set(58)

Label(main, text="Silence between letters:").grid(row=7, column=0, sticky=W)
gapLetters = Scale(main, from_=0, to=9999, orient=HORIZONTAL, length=200)
gapLetters.grid(row=7, column=1)
gapLetters.set(174)

Label(main, text="Silence between words:").grid(row=8, column=0, sticky=W)
gapWords = Scale(main, from_=0, to=9999, orient=HORIZONTAL, length=200)
gapWords.grid(row=8, column=1)
gapWords.set(406)

Label(main, text="Text to convert to Morse MIDI").grid(row=0, column=2, sticky=W, columnspan=2, padx=20)

text = Text(main, width=25, height=15, wrap=WORD)
text.insert(END, "Hello from K2UN")
text.grid(row=0, column=2, rowspan=8, sticky=W, columnspan=2, padx=20, pady=0)


button = Button(main, text="Convert", command=lambda: morse_to_midi(text.get("1.0", "end-1c").upper(), vol.get(),
                note.get(), bpmValue.get(), timeResolution.get(), dotLength.get(), dashLength.get(), gapMarks.get(),
                gapLetters.get(), gapWords.get()))
button.grid(row=7, column=2, sticky=W, padx=20, pady=5)

main.mainloop()
