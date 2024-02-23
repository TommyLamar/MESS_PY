from main.mess.Experiment import *
from main.gui.AddSensorWindow import AddSensorWindow
from main.gui.AddVehicleInput import AddVehicleInput
from main.gui.AddTaskInput import AddTaskInput
from main.gui.MissionWindow import MissionWindow
from main.gui.SensorWindow import SensorWindow
from main.gui.ViewVehicleWindow import ViewVehicleWindow
from main.fileTransfer.RetrieveLogs import retrieveLogs
from main.ros.launch.LaunchFile import LaunchFile

import tkinter as tk
from tkinter import filedialog as fd


class ExperimentWindow(tk.Toplevel):
    def __init__(self, *args, name, exp, vehicleDict, **kwargs):
        super().__init__(*args, **kwargs)

        self.name = name
        self.mainExperiment = exp
        self.vehicleDict = vehicleDict

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
        self.addCompileMission.place(x=200, y=150, width=150)

        self.addSaveMission = tk.Button(self, text="Save Mission", command=self.request_save)
        self.addSaveMission.place(x=50, y=250, width=300)

        self.launchButton = tk.Button(self, text="Build Launch Files", command=self.request_launch)
        self.launchButton.place(x=20, y=200, width=150)

        self.exportButton = tk.Button(self, text="Retrieve Log Files", command=self.request_log)
        self.exportButton.place(x=200, y=200, width=150)

        self.focus()
        self.grab_set()

    def request_vehicle(self):
        self.grab_release()
        self.window_name = AddVehicleInput(callback=self.vehicleInfo)

    def request_view_vehicles(self):
        self.grab_release()
        self.window_name5 = ViewVehicleWindow(name=self.name, vehicleDict=self.vehicleDict)

    def request_sensor(self):
        self.grab_release()
        self.window_name2 = AddSensorWindow(vehicleDict=self.vehicleDict, callback=self.sensorInfo)

    def request_view_sensors(self):
        self.grab_release()
        self.window_name6 = SensorWindow(name=self.name, sensors=self.mainExperiment.getAllSensors())

    def request_task(self):
        self.grab_release()
        self.window_name3 = AddTaskInput(vehicleDict=self.vehicleDict, callback=self.taskInfo)

    def request_compile(self):
        self.grab_release()
        self.window_name4 = MissionWindow(name=self.name, tasks=self.mainExperiment.compile())

    def request_log(self):
        # todo would be cool to get a progress window
        path = fd.askdirectory()
        if path != "":
            retrieveLogs(path, self.name, self.vehicleDict.values())

    def request_launch(self):
        for v in self.vehicleDict.values():
            lf = LaunchFile(v, "\\ros\\launch\\savedLaunchFiles")
            #commented out to test and until I know where o put launch files
            #lf.execute("insert some path here")

    def request_save(self):
        jsonstr = self.mainExperiment.toJSON()
        types = [("JSON Files", "*.json")]
        filePath = fd.asksaveasfilename(title="Custom Save Title", filetypes=types)
        with open(filePath, "w") as outfile:
            outfile.write(jsonstr)
        self.destroy()

    def vehicleInfo(self, name, id):
        self.grab_set()
        v = Vehicle(id, [])
        if (name not in self.vehicleDict
                and not self.mainExperiment.mission.checkDuplicates(VehicleMission(v, []))
                and name):
            self.mainExperiment.addVehicle(v)
            self.vehicleDict[name] = v
            v.setName(name)
        else:
            print("Vehicle already in this experiment")
            # can turn this into a popup window later

    def sensorInfo(self, package, rate, vehicleName, sensorName):
        self.grab_set()
        sensor = Sensor(package, rate)
        sensor.setName(sensorName)
        if vehicleName == "Environmental":
            self.mainExperiment.addEnvironmentSensors(sensor)
        elif vehicleName in self.vehicleDict:
            print(self.vehicleDict.get(vehicleName))
            self.mainExperiment.addVehicleSensor(sensor, self.vehicleDict.get(vehicleName))

    def taskInfo(self, timeStamp, message, topic, vehicle):
        self.grab_set()
        t = Task(timeStamp, message, topic, "")
        self.mainExperiment.addTask(t, vehicle)