from Vehicle import *
from Task import *


class VehicleMission:
    vehicle = Vehicle("changeMe", [])
    tasks = [Task(-1.23, "changeMe", "changeMe", "changeMe")]

    def __init__(self, vehicle, tasks):
        self.vehicle = vehicle
        self.tasks = tasks


