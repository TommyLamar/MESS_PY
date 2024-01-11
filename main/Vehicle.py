from Sensor import *
class Vehicle:
    viconID = "changeMe"
    sensors = [Sensor("changeMe", -1)]

    def __init__(self, id, sensors):
        self.viconID = id
        self.sensors = sensors

