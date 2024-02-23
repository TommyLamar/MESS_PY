from main.mess.ObstacleMap import *
from main.mess.Mission import *
import json



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
            if v.getIP() == vehicle.getIP():
                v.addSensor(sensor)

    def getMap(self):
        return self.map

    def getAllSensors(self):
        # To Do
        out = []
        for s in self.environmentSensors:
            out.append(["Environmental", s])
        for vm in self.mission.getVehicleMissions():
            v = vm.getVehicle()
            vname = v.getName()
            for s in v.getSensors():
                out.append([vname, s])
        return out

    def compile(self):
        return self.mission.generateMasterTasks()

    def addTask(self, t, v):
        self.mission.addTask(t, v)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)

    def fromJSON(self, jsonData):
        self.vehicles = []
        self.environmentSensors = []
        self.mission = self.mission.fromJSON(jsonData['mission'])
        for vehicle in jsonData['vehicles']:
            v = Vehicle(-1, [])
            self.vehicles.append(v.fromJSON(vehicle))
        for es in jsonData['environmentSensors']:
            s = Sensor("", 1)
            self.environmentSensors.append(s.fromJSON(es))

        return self


