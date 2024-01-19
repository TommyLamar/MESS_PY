# The Modular Experimental Software System
# Created as part of a Major Qualifying Project at Worcester Polytechnic Institute
# This totally isn't an RBE project

from main.Experiment import *

import tkinter as tk
from tkinter import filedialog as fd

# Global Variable to hold the experiment being worked on
mainExperiment = Experiment(Mission([]), [], [], ObstacleMap(1, 1))
vehicleDict = {}


# This is the window seen at startup
class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(width=400, height=300)
        self.title("MESS")

        # Set up features
        self.newExpButton = tk.Button(self, text='New Experiment', width=25, command=self.request_name)
        self.newExpButton.pack(pady=10)

        self.openExpButton = tk.Button(self, text='Open Existing Experiment', width=25)
        self.openExpButton.pack(pady=10)

        self.exitButton = tk.Button(self, text='Exit', width=25, command=self.destroy)
        self.exitButton.pack(pady=10)

        self.label_name = tk.Label(self, text=":)")
        self.label_name.pack()

    # Used to start input window for creating a new experiment
    def request_name(self):
        self.window_name = ExpInputWindow(callback=self.name_entered)

    # Using the input from new experiment input window
    def name_entered(self, name):
        # update the text at the bottom of the home screen
        self.label_name.config(text=name)

        # launch the experiment window
        self.ExpWindow = ExperimentWindow(name=name)


# Popup window to get new experiment name
class ExpInputWindow(tk.Toplevel):
    def __init__(self, *args, callback=None, **kwargs):
        super().__init__(*args, **kwargs)
        width = 300
        self.callback = callback
        self.config(width=width, height=110)
        self.resizable(False, False)
        self.title("Experiment Info")

        # setting up features
        self.entry_name = tk.Entry(self)
        self.entry_name.place(x=20, y=40, width=260)

        self.doneButton = tk.Button(self, text="Done", command=self.done_pressed)
        self.doneButton.place(x=20, y=70, width=260)

        self.label_entry = tk.Label(self, text="Enter Experiment Name")
        self.label_entry.place(x=80, y=10)

        # make this the highlighted window
        self.focus()
        self.grab_set()

    def done_pressed(self):
        # Use callback function to return to main window
        self.callback(self.entry_name.get())

        # allow others to be grabbed
        self.grab_release()

        # kill this window
        self.destroy()


# window to set up an experiment
class ExperimentWindow(tk.Toplevel):
    def __init__(self, *args, name, **kwargs):
        super().__init__(*args, **kwargs)

        self.config(width=400, height=300)
        self.title(name)

        # setting up features
        self.addVehicleButton = tk.Button(self, text="Add Vehicle", command=self.request_vehicle)
        self.addVehicleButton.place(x=20, y=50, width=150)

        self.addSensorButton = tk.Button(self, text="Add Sensor", command=self.request_sensor)
        self.addSensorButton.place(x=20, y=100, width=150)

        self.addTaskButton = tk.Button(self, text="Add Task", command=self.request_task)
        self.addTaskButton.place(x=20, y=150, width=150)

        self.addCompileMission = tk.Button(self, text="Compile Mission")
        self.addCompileMission.place(x=50, y=200, width=300)

        self.focus()
        self.grab_set()

    def request_vehicle(self):
        self.grab_release()
        self.window_name = AddVehicleInput(callback=self.vehicleInfo)


    def request_sensor(self):
        self.window_name2 = AddSensorInput(callback=self.sensorInfo)

    def request_task(self):
        self.window_name3 = AddTaskInput(callback=self.taskInfo)

    def vehicleInfo(self, name, id):
        self.grab_set()
        v = Vehicle(id, [])
        if (name not in vehicleDict
                and not mainExperiment.mission.checkDuplicates(VehicleMission(v, []))
                and name):
            mainExperiment.addVehicle(v)
            vehicleDict[name] = v
        else:
            print("Vehicle already in this experiment")
            # can turn this into a popup window later

    def sensorInfo(self, info):
        one = 1  # place holder

    def taskInfo(self, info):
        one = 1  # place holder


# Window that pops up to add a vehicle to an experiment
class AddVehicleInput(tk.Toplevel):
    def __init__(self, *args, callback=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.callback = callback
        self.config(width=300, height=90)
        self.resizable(False, False)
        self.title("Vehicle Information")

        # set up features
        self.vehicleNameEntry = tk.Entry(self)
        self.vehicleNameEntry.place(x=150, y=20, width=130)

        self.label_name = tk.Label(self, text="Vehicle Name:")
        self.label_name.place(x=50, y=20)

        self.vehicleIDEntry = tk.Entry(self)
        self.vehicleIDEntry.place(x=150, y=40, width=130)

        self.label_id = tk.Label(self, text="Vicon ID:")
        self.label_id.place(x=50, y=40)

        self.doneButton = tk.Button(self, text="Done", command=self.done_pressed)
        self.doneButton.place(x=20, y=60, width=260)

        self.focus()
        self.grab_set()

    def done_pressed(self):
        # Use callback function to return to main window
        self.callback(self.vehicleNameEntry.get(), self.vehicleIDEntry.get())

        # allows other to grab
        self.grab_release()

        # kill this window
        self.destroy()


class AddSensorInput(tk.Toplevel):
    def __init__(self, *args, callback=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.callback = callback
        self.config(width=400, height=210)
        self.resizable(False, False)
        self.title("Sensor Information")

        # get options for drop down menu
        options = self.loadOptions()

        # setup for drop down menu
        default = tk.StringVar()
        default.set(options[0])

        self.drop = tk.OptionMenu(self, default, *options)
        self.drop.place(x=150, y=10)

        self.label_drop = tk.Label(self, text="Sensor Location:")
        self.label_drop.place(x=50, y=10)

        self.refreshRateEntry = tk.Entry(self)
        self.refreshRateEntry.place(x=150, y=50, width=130)

        self.label_refreshRate = tk.Label(self, text="Refresh Rate:")
        self.label_refreshRate.place(x=50, y=50)

        self.packageButton = tk.Button(self, text="Select File", command=self.select_file_pressed)
        self.packageButton.place(x=150, y=80, width=130)

        self.label_rosPackage = tk.Label(self, text="ROS Package:")
        self.label_rosPackage.place(x=50, y=80)

        self.label_file = tk.Label(self, text="no file selected")
        self.label_file.place(x=10, y=120)

        self.doneButton = tk.Button(self, text="Done", command=self.done_pressed)
        self.doneButton.place(x=20, y=150, width=260)

        self.focus()

    def done_pressed(self):
        # Use callback function to return to main window
        self.callback(info=1)

        # kill this window
        self.destroy()

    def select_file_pressed(self):
        name = fd.askopenfilename()
        self.label_file.config(text=name)
        print(name)
        # need to actually process this into a usable format for the script

    # create list with all the vehicle names
    def loadOptions(self):
        out = ["Environmental"]
        for key in vehicleDict.keys():
            out.append(key)
        return out


class AddTaskInput(tk.Toplevel):
    def __init__(self, *args, callback=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.callback = callback
        self.config(width=300, height=200)
        self.resizable(False, False)
        self.title("Vehicle Information")

        # set up features
        self.timeStampEntry = tk.Entry(self)
        self.timeStampEntry.place(x=150, y=20, width=130)

        self.label_timeStamp = tk.Label(self, text="Time stamp:")
        self.label_timeStamp.place(x=50, y=20)

        self.messageEntry = tk.Entry(self)
        self.messageEntry.place(x=150, y=60, width=130)

        self.label_message = tk.Label(self, text="ROS Message:")
        self.label_message.place(x=50, y=60)

        self.topicEntry = tk.Entry(self)
        self.topicEntry.place(x=150, y=100, width=130)

        self.label_topic = tk.Label(self, text="ROS Topic:")
        self.label_topic.place(x=50, y=100)

        self.doneButton = tk.Button(self, text="Done", command=self.done_pressed)
        self.doneButton.place(x=20, y=150, width=260)

    def done_pressed(self):
        # Use callback function to return to main window
        self.callback(1)

        # kill this window
        self.destroy()


if __name__ == '__main__':
    mw = MainWindow()
    mw.mainloop()