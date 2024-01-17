from main.VehicleMission import *


class Mission:
    vehicleMissions = []
    masterTasks = []

    def __init__(self, missions):
        self.vehicleMissions = missions

    def addVehicleMission(self, vm):
        if not self.checkDuplicates(vm):
            self.vehicleMissions.append(vm)
        else:
            raise ValueError("Duplicate Vehicle for Vehicle Mission")

    def getVehicleMissions(self):
        return self.vehicleMissions

    def checkDuplicates(self, vm):
        id = vm.getVehicle().getViconID()

        for vehicleMission in self.vehicleMissions:
            if vehicleMission.getVehicle().getViconID() == id:
                return True

        return False

    def getMasterTasks(self):
        return self.masterTasks

    def generateMasterTasks(self):
        unsorted = []
        for vm in self.vehicleMissions:
            for task in vm.getTasks():
                unsorted.append(task)
        unsorted.sort(key=lambda x: x.getTimeStamp())
        self.masterTasks = unsorted
        return self.getMasterTasks()
