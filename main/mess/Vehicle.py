from main.mess.Sensor import *
import json


class Vehicle:
    ip = "changeMe"
    sensors = [Sensor("changeMe", -1)]
    name = "vehicle"

    def __init__(self, ip, sensors, name="", vtype="UGV"):
        self.ip = ip
        self.sensors = sensors
        self.name = name
        self.vtype = vtype

    def getIP(self):
        return self.ip

    def getSensors(self):
        return self.sensors

    def addSensor(self, s):
        self.sensors.append(s)

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setType(self, t):
        self.vtype = t

    def getType(self):
        return self.vtype

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)

    def fromJSON(self, jsonData):
        self.ip = jsonData["viconID"]
        self.name = jsonData["name"]
        for s in jsonData["sensors"]:
            temp = Sensor("", -1)
            self.sensors.append(temp.fromJSON(s))

        return self
