# The Modular Experimental Software System
# Created as part of a Major Qualifying Project at Worcester Polytechnic Institute
# This totally isn't an RBE project
# I dream of one day refactoring this so all the window classes will be their own file

from main.Experiment import *

import tkinter as tk
from tkinter import filedialog as fd
import json

# Global Variable to hold the experiment being worked on
mainExperiment = Experiment(Mission([]), [], [], ObstacleMap(1, 1))
vehicleDict = {}
expName = [""]


# This is the window seen at startup
class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(width=400, height=300)
        self.title("MESS")

        # Set up features
        self.newExpButton = tk.Button(self, text='New Experiment', width=25, command=self.request_name)
        self.newExpButton.pack(pady=10)

        self.openExpButton = tk.Button(self, text='Open Existing Experiment', width=25, command=self.select_file_pressed)
        self.openExpButton.pack(pady=10)

        self.exitButton = tk.Button(self, text='Exit', width=25, command=self.destroy)
        self.exitButton.pack(pady=10)

        self.label_name = tk.Label(self, text=":)")
        self.label_name.pack()

    # Used to start input window for creating a new experiment
    def request_name(self):
        self.window_name = ExpInputWindow(callback=self.name_entered)

    def name_entered(self, name):
        # update the text at the bottom of the home screen
        self.label_name.config(text=name)
        # launch the experiment window
        self.ExpWindow = ExperimentWindow(name=name)
        expName[0] = name

        # Using the input from new experiment input window

    def select_file_pressed(self):
        name = fd.askopenfilename()
        if name[-5:] == ".json": ##only open json files
            ss = name.split('/')
            stripName = ss[0][:-4] ##remove the .json from the file name
            self.label_name.config(text=stripName)
            with open(name, "r") as file:
                data = json.load(file)
                mainExperiment.fromJSON(data)
                expName[0] = stripName
            print(expName[0])

            ##update the vehicle dictionary
            vehicleDict.clear()
            for v in mainExperiment.getVehicles():
                vehicleDict[v.getName()] = v

            self.ExpWindow = ExperimentWindow(name=stripName)


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

        self.name = name

        self.config(width=400, height=300)
        self.title(name)

        # setting up features
        self.addVehicleButton = tk.Button(self, text="Add Vehicle", command=self.request_vehicle)
        self.addVehicleButton.place(x=20, y=50, width=150)

        self.addSensorButton = tk.Button(self, text="Add Sensor", command=self.request_sensor)
        self.addSensorButton.place(x=20, y=100, width=150)

        self.addVehicleButton = tk.Button(self, text="View Vehicles", command=self.request_view_vehicles)
        self.addVehicleButton.place(x=200, y=50, width=150)

        self.addSensorButton = tk.Button(self, text="View Sensors", command=self.request_view_sensors)
        self.addSensorButton.place(x=200, y=100, width=150)

        self.addTaskButton = tk.Button(self, text="Add Task", command=self.request_task)
        self.addTaskButton.place(x=20, y=150, width=150)

        self.addCompileMission = tk.Button(self, text="Compile Mission", command=self.request_compile)
        self.addCompileMission.place(x=50, y=200, width=300)

        self.addSaveMission = tk.Button(self, text="Save Mission", command=self.request_save)
        self.addSaveMission.place(x=50, y=250, width=300)

        self.focus()
        self.grab_set()

    def request_vehicle(self):
        self.grab_release()
        self.window_name = AddVehicleInput(callback=self.vehicleInfo)

    def request_view_vehicles(self):
        self.grab_release()
        self.window_name5 = ViewVehicleWindow(name=self.name)

    def request_sensor(self):
        self.grab_release()
        self.window_name2 = AddSensorInput(callback=self.sensorInfo)

    def request_view_sensors(self):
        self.grab_release()
        self.window_name6 = SensorWindow(name=self.name)

    def request_task(self):
        self.grab_release()
        self.window_name3 = AddTaskInput(callback=self.taskInfo)

    def request_compile(self):
        self.grab_release()
        self.window_name4 = MissionWindow(name=self.name)

    def request_save(self):
        jsonstr = mainExperiment.toJSON()
        fileName = "savedJsons\\"+expName[0] + ".json"
        with open(fileName, "w") as outfile:
            outfile.write(jsonstr)
        self.destroy()


    def vehicleInfo(self, name, id):
        self.grab_set()
        v = Vehicle(id, [])
        if (name not in vehicleDict
                and not mainExperiment.mission.checkDuplicates(VehicleMission(v, []))
                and name):
            mainExperiment.addVehicle(v)
            vehicleDict[name] = v
            v.setName(name)
        else:
            print("Vehicle already in this experiment")
            # can turn this into a popup window later

    def sensorInfo(self, package, rate, vehicleName, sensorName):
        self.grab_set()
        sensor = Sensor(package, rate)
        sensor.setName(sensorName)
        if vehicleName == "Environmental":
            mainExperiment.addEnvironmentSensors(sensor)
        elif vehicleName in vehicleDict:
            print(vehicleDict.get(vehicleName))
            mainExperiment.addVehicleSensor(sensor, vehicleDict.get(vehicleName))


    def taskInfo(self, timeStamp, message, topic, vehicle):
        self.grab_set()
        t = Task(timeStamp, message, topic, "")
        mainExperiment.addTask(t, vehicle)


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
        self.selected = tk.StringVar()
        self.selected.set(options[0])

        self.drop = tk.OptionMenu(self, self.selected, *options)
        self.drop.place(x=150, y=10)

        self.label_drop = tk.Label(self, text="Sensor Location:")
        self.label_drop.place(x=50, y=10)

        self.refreshRateEntry = tk.Entry(self)
        self.refreshRateEntry.place(x=150, y=50, width=130)

        self.label_refreshRate = tk.Label(self, text="Refresh Rate:")
        self.label_refreshRate.place(x=50, y=50)

        self.packageButton = tk.Button(self, text="Select File", command=self.select_file_pressed)
        self.packageButton.place(x=150, y=120, width=130)

        self.label_rosPackage = tk.Label(self, text="ROS Package:")
        self.label_rosPackage.place(x=50, y=120)

        self.label_file = tk.Label(self, text="no file selected")
        self.label_file.place(x=10, y=150)

        self.doneButton = tk.Button(self, text="Done", command=self.done_pressed)
        self.doneButton.place(x=20, y=180, width=260)

        self.nameEntry = tk.Entry(self)
        self.nameEntry.place(x=150, y=80, width=130)

        self.label_name = tk.Label(self, text="Sensor Name:")
        self.label_name.place(x=50, y=80)

        self.package = ""

        self.focus()

    def done_pressed(self):
        rr = int(self.refreshRateEntry.get())
        p = self.package
        vehicle = self.selected.get()
        name = self.nameEntry.get()
        # Use callback function to return to main window
        self.callback(p, rr, vehicle, name)

        # kill this window
        self.destroy()

    def select_file_pressed(self):
        name = fd.askopenfilename()
        self.package = name
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
        self.config(width=300, height=300)
        self.resizable(False, False)
        self.title("Vehicle Information")

        # get options for drop down menu
        options = self.loadOptions()

        # setup for drop down menu
        self.selected = tk.StringVar()
        self.selected.set(options[0])

        self.drop = tk.OptionMenu(self, self.selected, *options)
        self.drop.place(x=150, y=150)

        self.label_drop = tk.Label(self, text="Vehicle:")
        self.label_drop.place(x=50, y=150)

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
        self.doneButton.place(x=20, y=200, width=260)

        self.focus()
        self.grab_set()

    def done_pressed(self):
        # Use callback function to return to main window
        if self.selected.get() in vehicleDict:
            timeStamp = float(self.timeStampEntry.get())
            message = self.messageEntry.get()
            topic = self.topicEntry.get()
            vehicle = vehicleDict.get(self.selected.get())

            self.callback(timeStamp, message, topic, vehicle)

            # kill this window
            self.destroy()

    def loadOptions(self):
        out = ["Don't Select Me"]
        for key in vehicleDict.keys():
            out.append(key)
        return out


class MissionWindow(tk.Toplevel):
    def __init__(self, *args, name, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(width=600, height=300)
        title = name + "- Mission Overview"
        self.title(title)

        # screen elements
        self.bar = tk.Scrollbar(self)
        self.text = tk.Text(self, height=10, width=60)
        self.text.place(x=20, y=20)
        self.bar.place(x=510, y=20, height=200)
        self.bar.config(command=self.text.yview)
        self.text.config(yscrollcommand=self.bar.set)

        self.focus()
        self.grab_set()

        for s in self.loadTasks():
            self.text.insert(tk.END, s)

    def loadTasks(self):
        # This is wildly inefficient in terms of running time and could be simplified if we just give the vehicle object
        # An attribute for the vehicle name, would also save the vehicle dictionary shenanigans, but im too far in to
        # Want to change that at this moment

        out = ["Time\t Vehicle\t\t Topic\t\t Message\n"]
        tasks = mainExperiment.compile()

        for obj in tasks:
            task = obj.getTask()
            time = str(task.getTimeStamp())
            topic = str(task.getTopic())
            message = str(task.getMessage())
            vehicle = obj.getVehicle()
            vehicleName = vehicle.getName()
            string = time + "\t" + vehicleName + "\t\t" + topic + "\t\t" + message + "\n"
            out.append(string)

        return out


class ViewVehicleWindow(tk.Toplevel):
    def __init__(self, *args, name, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(width=600, height=300)
        title = name + "- Vehicles"
        self.title(title)

        # get options for drop down menu
        options = self.loadOptions()

        # setup for drop down menu
        self.selected = tk.StringVar()
        self.selected.set(options[0])

        self.drop = tk.OptionMenu(self, self.selected, *options)
        self.drop.place(x=20, y=20)

        self.viewInfoButton = tk.Button(self, text="View Info", command=self.loadText)
        self.viewInfoButton.place(x=150, y=20)

        # screen elements
        self.bar = tk.Scrollbar(self)
        self.text = tk.Text(self, height=10, width=60)
        self.text.place(x=20, y=70)
        self.bar.place(x=510, y=70, height=200)
        self.bar.config(command=self.text.yview)
        self.text.config(yscrollcommand=self.bar.set)

        self.focus()
        self.grab_set()

    def loadOptions(self):
        out = ["Don't Select Me"]
        for key in vehicleDict.keys():
            out.append(key)
        return out

    def loadText(self):
        self.text.delete('1.0', tk.END)
        vehicleName = self.selected.get()
        if vehicleName in vehicleDict:
            vehicle = vehicleDict.get(vehicleName)
            vid = vehicle.getViconID()
            sensors = vehicle.getSensors()
            self.text.insert(tk.END, "Name: "+vehicleName+"\n")
            self.text.insert(tk.END, "ViconID: "+str(vid))
            self.text.insert(tk.END, "\nSensor Info\n")
            self.text.insert(tk.END, "Name\t\tRefresh Rate\n")

            for sensor in sensors:
                sensorString = sensor.getName() + "\t\t" + str(sensor.getRate())
                self.text.insert(tk.END, sensorString)


class SensorWindow(tk.Toplevel):
    def __init__(self, *args, name, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(width=600, height=300)
        title = name + "- Sensors"
        self.title(title)

        # screen elements
        self.bar = tk.Scrollbar(self)
        self.text = tk.Text(self, height=10, width=60)
        self.text.place(x=20, y=20)
        self.bar.place(x=510, y=20, height=200)
        self.bar.config(command=self.text.yview)
        self.text.config(yscrollcommand=self.bar.set)

        self.focus()
        self.grab_set()

        for s in self.loadSensors():
            self.text.insert(tk.END, s)

    def loadSensors(self):
        out = ["Location\t\t Name\t\t Refresh Rate\n"]
        for row in mainExperiment.getAllSensors():
            sensor = row[1]
            location = row[0]
            out.append(location + "\t\t" + sensor.getName() + "\t\t" + str(sensor.getRate()) + "\n")

        return out

if __name__ == '__main__':
    mw = MainWindow()
    mw.mainloop()
