from main.mess.Sensor import *
import json
class Vehicle:
    viconID = "changeMe"
    sensors = [Sensor("changeMe", -1)]
    name = "vehicle"

    def __init__(self, id, sensors):
        self.viconID = id
        self.sensors = sensors
        self.name = ""

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

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)

    def fromJSON(self, jsonData):
        self.viconID = jsonData["viconID"]
        self.name = jsonData["name"]
        for s in jsonData["sensors"]:
            temp = Sensor("", -1)
            self.sensors.append(temp.fromJSON(s))

        return self

