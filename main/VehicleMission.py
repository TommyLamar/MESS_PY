from main.Vehicle import *
from main.Task import *
import json


class VehicleMission:
    vehicle = Vehicle("changeMe", [])
    tasks = [Task(-1.23, "changeMe", "changeMe", "changeMe")]

    def __init__(self, vehicle, tasks):
        self.vehicle = vehicle
        self.tasks = tasks

    def createTask(self, time, message, topic, type):
        self.tasks.append(Task(time, message, topic, type))

    def addTask(self, t):
        self.tasks.append(t)

    def getVehicle(self):
        return self.vehicle

    def getTasks(self):
        return self.tasks

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)

    def fromJSON(self, jsonData):
        v = Vehicle(-1, [])
        self.vehicle = v.fromJSON(jsonData["vehicle"])
        for t in jsonData["tasks"]:
            temp = Task(-1, "", "", "")
            self.tasks.append(temp.fromJSON(t))
        return self
