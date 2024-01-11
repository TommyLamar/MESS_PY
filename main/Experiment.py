from Sensor import *
from ObstacleMap import *
from Mission import *
from Vehicle import *


class Experiment:
    mission = Mission([])
    vehicles = []
    environmentSensors = []
    map = ObstacleMap(1,1)

    def __init__(self, mission, vehicles, sensors, map):
        self.mission = mission
        self.vehicles = vehicles
        self.environmentSensors = sensors
        self.map = map

