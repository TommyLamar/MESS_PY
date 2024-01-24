from main.VehicleMission import *


class Mission:
    vehicleMissions = []
    masterTasks = []

    def __init__(self, missions):
        self.vehicleMissions = missions

    def addVehicleMission(self, vm):
        # only add vm if associated vehicle does not already have a vehicle mission
        if not self.checkDuplicates(vm):
            self.vehicleMissions.append(vm)
        else:
            raise ValueError("Duplicate Vehicle for Vehicle Mission")

    def removeVehicleMission(self, vm):
        # removes VehicleMission vm from mission

        # vehicle if to remove
        v = vm.getVehicle().getViconID()


        # Filter to keep vms that don't have the needed
        newVms = [x for x in self.getVehicleMissions() if x.getVehicle().getViconID() != v]

        # update and return
        self.vehicleMissions = newVms
        return self.getVehicleMissions()

    def getVehicleMissions(self):
        return self.vehicleMissions

    def checkDuplicates(self, vm):
        id = vm.getVehicle().getViconID()

        # determine if duplicate based on the ViconID for the Vehicle associated with a VehicleMission
        for vehicleMission in self.vehicleMissions:
            if vehicleMission.getVehicle().getViconID() == id:
                return True

        return False

    def getMasterTasks(self):
        return self.masterTasks

    def generateMasterTasks(self):
        # creates an ordered list off of timestamps of all tasks associated with all the VehicleMissions

        unsorted = []
        for vm in self.vehicleMissions:
            vehicle = vm.getVehicle()
            for task in vm.getTasks():
                t = Temp(vehicle, task)
                unsorted.append(t)

        # sort the list based on the timestamps
        unsorted.sort(key=lambda x: x.getTask().getTimeStamp())

        # create a list of just the tasks
        onlyTasks = []
        for obj in unsorted:
            onlyTasks.append(obj.getTask())

        # update that
        self.masterTasks = onlyTasks

        # return list of tasks and their associated
        print(unsorted)
        return unsorted

    def addTask(self, t, v):
        vID = v.getViconID()
        for vm in self.vehicleMissions:
            if vID == vm.getVehicle().getViconID():
                vm.addTask(t)


class Temp:

    def __init__(self, v, t):
        self.vehicle = v
        self.task = t

    def getVehicle(self):
        return self.vehicle

    def getTask(self):
        return self.task