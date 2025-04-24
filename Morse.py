from tkinter import filedialog
from tkinter import *
from tkinter import messagebox  # Importiere das messagebox-Modul
from midiutil import MIDIFile

def morse_to_midi(t, volume, n, bpm, tr, dot, dash, marks, letters, words,
                  track_name="Morse Code"):
    t = t.replace('\n', " ")
    morse = english_morse(t)
    total_time = 0
    for char in morse:
        if char == '.':
            total_time += dot + marks
        elif char == '-':
            total_time += dash + marks
        elif char == '|':
            total_time += words
        elif char == ' ':
            total_time += letters
    print(total_time)
    my_midi = MIDIFile(1)
    my_midi.addTempo(track=0, time=0, tempo=bpm)
    my_midi.addTrackName(track=0, time=0, trackName=track_name)

    time = 0
    for char in morse:
        if char == '.':
            my_midi.addNote(track=0, channel=0, pitch=n, time=time, duration=(dot/tr), volume=volume)
            time += (dot / tr) + (marks / tr)
        elif char == '-':
            my_midi.addNote(track=0, channel=0, pitch=n, time=time, duration=(dash/tr), volume=volume)
            time += (dash / tr) + (marks / tr)
        elif char == '|':
            my_midi.addNote(track=0, channel=0, pitch=0, time=time, duration=(words/tr), volume=0)
            time += (words / tr) - (marks / tr)
        elif char == ' ':
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

def calculate_details(dot_len, 
                      dash_len, mark_space, letter_space,
                      word_space, text_to_calc, time_resolution):    

    morse_code = english_morse(text_to_calc)

    total_length = 0
    unit = 1#int(input_vars["Time Resolution:"].get()) if input_vars["Time Resolution:"].get() else 1

    for char in morse_code:
        if char == '.':
            total_length += dot_len + mark_space
        elif char == '-':
            total_length += dash_len + mark_space
        elif char == ' ':
            total_length += letter_space - mark_space
        elif char == '|':
            total_length += word_space - mark_space
    if len(morse_code) > 0:
        total_length -= mark_space
    print(f"morse_code: '{text_to_calc}' > '{morse_code}' > leng: {total_length}")

    # Remove the trailing space/pipe length
    if morse_code.endswith(' '):
        total_length -= letter_space
    elif morse_code.endswith('|'):
        total_length -= word_space

    text_inhalt = f"1x 4/4 Beat = {4*time_resolution} units -> 4x 4/4 Beat = {16*time_resolution} units"
    text_inhalt += f"\nApproximate total length: {total_length / unit:.2f} units"
    text_inhalt += f"\n'{text_to_calc}':\n'{morse_code}' > length: {total_length}"

    return text_inhalt
