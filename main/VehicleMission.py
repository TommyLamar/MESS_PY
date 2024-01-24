from main.Vehicle import *
from main.Task import *


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


