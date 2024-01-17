class Sensor:
    rosPackage = "changeMe"
    refreshRate = -1

    def __init__(self, package, rate):
        self.rosPackage = package
        self.refreshRate = rate

    def getPackage(self):
        return self.rosPackage


    def getRate(self):
        return self.refreshRate

