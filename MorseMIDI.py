#!/usr/bin/python3
# import pathlib
# import tkinter as tk
from tkinter import END
# import pygubu
from tkinter import filedialog
from MorseMIDIui import MorseMIDIUI
from Morse import morse_to_midi
# from Morse import english_morse
from Morse import calculate_details
import json
import os


PROJECT_PATH = os.path.dirname(__file__)
PROJECT_UI = os.path.join(PROJECT_PATH, "app.ui")

__version__ = "0.1.0"


def write_to_json(json_data):
    file_handler = filedialog.asksaveasfilename(defaultextension=".json",
                                    filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
                                    initialfile="default_settings.json",
                                    title="Store JSON-File")
    print(f"selected file_handler to store: '{file_handler}'")
    if file_handler is None:
        print("abort storing")
        return
    if file_handler:
        with open(file_handler, 'w') as file:
            json.dump(json_data, file)
    else:
        print("No file selected.")


def read_from_json():
    json_data = {}
    file_handler = filedialog.askopenfilename(defaultextension=".json",
                                    filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
                                    title="Load JSON-File"
                                    )
    print(f"file_handler: '{file_handler}'")
    if file_handler == "":
        print("No file selected")
        return
    try:
        with open(file_handler, 'r') as file:
            json_data = json.load(file)
    except FileNotFoundError:
        pass
    return json_data


class MorseMIDI(MorseMIDIUI):
    def __init__(self, master=None):
        super().__init__(master)
        print(f"Version: {__version__}")
        self.input_text = ""
        self.code_title_text = ""
        self.read_values()
        ICON_FILE = os.path.join(PROJECT_PATH, 'icon.ico')
        self.mainwindow.iconbitmap(ICON_FILE)

        print(type(self.mainwindow.title(f"MorseMIDI 'Version: {__version__}'")))

    def read_values(self):
        input_text_entry = self.builder.get_object('Input_Text')
        self.input_text = input_text_entry.get("1.0", 'end-1c').upper()
        self.code_title_text = self.code_title.get()
        
        self.volume_value = int(self.volume.get())
        self.note_value = int(self.note.get())
        self.bpm_value = int(self.bpm.get())
        self.time_resolution_value = int(self.time_resolution.get())
        self.dot_len_value = int(self.dot_len.get())
        self.dash_len_value = int(self.dash_len.get())
        self.mark_space_value = int(self.mark_space.get())
        self.letter_space_value = int(self.letter_space.get())
        self.word_space_value = int(self.word_space.get())
        
        print("---- READ VALUES ----")
        print(f'Input_Text: {self.input_text}')
        print(f'code_title: {self.code_title_text}')
                
        print(f'volume_value: {self.volume_value}')
        print(f'note_value: {self.note_value}')
        print(f'bpm_value: {self.bpm_value}')
        print(f'time_resolution_value: {self.time_resolution_value}')
        print(f'dot_len_value: {self.dot_len_value}')
        print(f'dash_len_value: {self.dash_len_value}')
        print(f'mark_space_value: {self.mark_space_value}')
        print(f'letter_space_value: {self.letter_space_value}')
        print(f'word_space_value: {self.word_space_value}')

    def convert(self):
        '''convert Text to Morede Midi code and store to file
        
        '''
        self.read_values()
        morse_to_midi(
                t=self.input_text,
                volume=self.volume_value,
                n=self.note_value,
                bpm=self.bpm_value,
                tr=self.time_resolution_value,
                dot=self.dot_len_value,
                dash=self.dash_len_value,
                marks=self.mark_space_value,
                letters=self.letter_space_value,
                words=self.word_space_value,
                track_name=self.code_title_text
                )

    def Calc(self):
        '''Calculate Morse MIDI Details
        '''
        self.read_values()
        text_inhalt = calculate_details(dot_len=self.dot_len_value,
                                       dash_len=self.dash_len_value,
                                       mark_space=self.mark_space_value,
                                       letter_space=self.letter_space_value,
                                       word_space=self.word_space_value,
                                       text_to_calc=self.input_text,
                                       time_resolution=self.time_resolution_value)

        output_widget = self.builder.get_object('Output_Text')
        output_widget.delete("1.0", END)
        output_widget.insert("1.0", text_inhalt)

    def store_to_json(self):
        self.read_values()
        json_data = {
            "morse_input_text": self.input_text,
            "code_title": self.code_title_text,
            "volume_value": self.volume_value,
            "note_value": self.note_value,
            "bpm_value": self.bpm_value,
            "time_resolution_value": self.time_resolution_value,
            "dot_len_value": self.dot_len_value,
            "dash_len_value": self.dash_len_value,
            "mark_space_value": self.mark_space_value,
            "letter_space_value": self.letter_space_value,
            "word_space_value": self.word_space_value
        }
        write_to_json(json_data)

    def load_from_json(self):
        json_data = read_from_json()
        print(f"json data: {json_data}")
        if json_data is None:
            print("nothing updated")
            return
        else:
            input_text = json_data.get("morse_input_text", "MorseCode")
            self.code_title.set(json_data.get('code_title', "Midi Morse Code Title"))
            self.volume.set(json_data.get('volume_value', 100))
            self.note.set(json_data.get('note_value', 80))
            self.bpm.set(json_data.get('bpm_value', 120))
            self.time_resolution.set(json_data.get('time_resolution_value', 480))
            self.dot_len.set(json_data.get('dot_len_value', 110))
            self.dash_len.set(json_data.get('dash_len_value', 230))
            self.mark_space.set(json_data.get('mark_space_value', 10))
            self.letter_space.set(json_data.get('letter_space_value', 130))
            self.word_space.set(json_data.get('word_space_value', 250))

            output_widget = self.builder.get_object('Input_Text')
            output_widget.delete("1.0", END)
            output_widget.insert("1.0", input_text)

    def load_default(self):
        input_text = "Morse code to MIDI"
        self.code_title.set("MIDI Morse Code")
        self.volume.set(100)
        self.note.set(80)
        self.bpm.set(120)
        self.time_resolution.set(480)
        self.dot_len.set(110)
        self.dash_len.set(230)
        self.mark_space.set(10)
        self.letter_space.set(130)
        self.word_space.set(250)
        
        output_widget = self.builder.get_object('Input_Text')
        output_widget.delete("1.0", END)
        output_widget.insert("1.0", input_text)


if __name__ == "__main__":
    app = MorseMIDI()
    app.run()
