#!/usr/bin/python3
import pathlib
import tkinter as tk
import pygubu

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "MorseMIDI_Pygubu.ui"
RESOURCE_PATHS = [PROJECT_PATH]


class MorseMIDIUI:
    def __init__(
        self,
        master=None,
        translator=None,
        on_first_object_cb=None,
        data_pool=None
    ):
        self.builder = pygubu.Builder(
            translator=translator,
            on_first_object=on_first_object_cb,
            data_pool=data_pool
        )
        self.builder.add_resource_paths(RESOURCE_PATHS)
        self.builder.add_from_file(PROJECT_UI)
        # Main widget
        self.mainwindow: tk.Toplevel = self.builder.get_object(
            "MorseMIDI", master)
        # Main menu
        _main_menu = self.builder.get_object("menu1", self.mainwindow)
        self.mainwindow.configure(menu=_main_menu)

        self.volume: tk.IntVar = None
        self.note: tk.DoubleVar = None
        self.bpm: tk.DoubleVar = None
        self.time_resolution: tk.DoubleVar = None
        self.dot_len: tk.DoubleVar = None
        self.dash_len: tk.DoubleVar = None
        self.mark_space: tk.StringVar = None
        self.letter_space: tk.DoubleVar = None
        self.word_space: tk.DoubleVar = None
        self.code_title: tk.StringVar = None
        self.builder.import_variables(self)

        self.builder.connect_callbacks(self)

    def run(self):
        self.mainwindow.mainloop()

    def convert(self):
        pass

    def Calc(self):
        pass

    def store_to_json(self):
        pass

    def load_from_json(self):
        pass

    def load_default(self):
        pass

    def on_about_menu_clicked(self):
        pass


if __name__ == "__main__":
    app = MorseMIDIUI()
    app.run()
