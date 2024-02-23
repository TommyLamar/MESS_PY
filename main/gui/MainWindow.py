# The Modular Experimental Software System (MESS)
# Created as part of a Major Qualifying Project at Worcester Polytechnic Institute
# This totally isn't an RBE project
# I also don't know if I'll get around to commenting to explain the code, good luck :)


from main.mess.Experiment import *
from main.gui.ExperimentWindow import ExperimentWindow
from main.gui.ExpInputWindow import ExpInputWindow


import tkinter as tk
from tkinter import filedialog as fd
import json


# This is the window seen at startup
class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(width=400, height=300)
        self.title("MESS")

        # Set up features
        self.newExpButton = tk.Button(self, text='New Experiment', width=25, command=self.request_name)
        self.newExpButton.pack(pady=10)

        self.openExpButton = tk.Button(self, text='Open Existing Experiment', width=25,
                                       command=self.select_file_pressed)
        self.openExpButton.pack(pady=10)

        self.exitButton = tk.Button(self, text='Exit', width=25, command=self.destroy)
        self.exitButton.pack(pady=10)

        self.label_name = tk.Label(self, text=":)")
        self.label_name.pack()

    # Used to start input window for creating a new experiment
    def request_name(self):
        self.window_name = ExpInputWindow(callback=self.name_entered)

    def name_entered(self, name):
        tempExp = Experiment(Mission([]), [], [], ObstacleMap(1, 1))
        vd = {}
        # update the text at the bottom of the home screen
        self.label_name.config(text=name)
        # launch the experiment window
        self.ExpWindow = ExperimentWindow(name=name, exp=tempExp, vehicleDict=vd)

        # Using the input from new experiment input window

    def select_file_pressed(self):
        tempExp = Experiment(Mission([]), [], [], ObstacleMap(1, 1))
        name = fd.askopenfilename()
        if name[-5:] == ".json":  # only open json files
            ss = name.split('/')
            stripName = ss[0][:-4]  # remove the .json from the file name
            self.label_name.config(text=stripName)
            with open(name, "r") as file:
                data = json.load(file)
                tempExp.fromJSON(data)

            # update the vehicle dictionary
            vd = {}
            for v in tempExp.getVehicles():
                vd[v.getName()] = v

            self.ExpWindow = ExperimentWindow(name=stripName, exp=tempExp, vehicleDict=vd)


if __name__ == '__main__':
    mw = MainWindow()
    mw.mainloop()
