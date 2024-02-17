import json
class Sensor:
    name = "sensor"

    def __init__(self, package, rate):
        self.rosPackage = package
        self.refreshRate = rate
        self.name = ""

    def getPackage(self):
        return self.rosPackage

    def getRate(self):
        return self.refreshRate

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)

    def fromJSON(self, jsonData):
        self.rosPackage = jsonData["rosPackage"]
        self.refreshRate = jsonData["refreshRate"]
        self.name = jsonData["name"]
        return self