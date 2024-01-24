from main.ObstacleMap import *
from main.Mission import *



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

    def getMission(self):
        return self.mission

    def addVehicle(self, v):
        vm = VehicleMission(v, [])
        if not self.mission.checkDuplicates(vm):
            self.mission.addVehicleMission(vm)
            self.vehicles.append(v)

    def getVehicles(self):
        return self.vehicles

    def getEnvironmentSensors(self):
        return self.environmentSensors

    def addEnvironmentSensors(self, sensor):
        self.environmentSensors.append(sensor)

    def addVehicleSensor(self, sensor, vehicle):
        for v in self.vehicles:
            if v.getViconID == vehicle.getViconID():
                v.addSensor(sensor)

    def getMap(self):
        return self.map

    def getAllSensors(self):
        # To Do
        # returns all sensors in an expirement, both environmental and vehicle
        return []

    def compile(self):
        return self.mission.generateMasterTasks()

    def addTask(self, t, v):
        self.mission.addTask(t, v)

