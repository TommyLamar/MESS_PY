from main.Sensor import *
class Vehicle:
    viconID = "changeMe"
    sensors = [Sensor("changeMe", -1)]
    name = "vehicle"

    def __init__(self, id, sensors):
        self.viconID = id
        self.sensors = sensors

    def getViconID(self):
        return self.viconID

    def getSensors(self):
        return self.sensors

    def addSensor(self, s):
        self.sensors.append(s)

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name
