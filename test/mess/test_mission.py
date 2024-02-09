import unittest
from main.Mission import *


class TestCheckDuplicates(unittest.TestCase):
    def test_empty_list(self):
        vehicle = Vehicle("1", [])
        vm = VehicleMission(vehicle, [])
        mis = Mission([])

        self.assertFalse(mis.checkDuplicates(vm))

    def test_no_duplicates(self):
        vehicle1 = Vehicle("1", [])
        vehicle2 = Vehicle("2", [])
        vm1 = VehicleMission(vehicle1, [])
        vm2 = VehicleMission(vehicle2, [])
        mis = Mission([vm1])

        self.assertFalse(mis.checkDuplicates(vm2))

    def test_duplicates(self):
        vehicle1 = Vehicle("1", [])
        vehicle2 = Vehicle("1", [])
        vm1 = VehicleMission(vehicle1, [])
        vm2 = VehicleMission(vehicle2, [])
        mis = Mission([vm1])

        self.assertTrue(mis.checkDuplicates(vm2))

    def test_add_no_duplicates(self):
        vehicle = Vehicle("1", [])
        vm = VehicleMission(vehicle, [])
        mis = Mission([])
        expectedOut = [vm]
        mis.addVehicleMission(vm)

        self.assertEqual(expectedOut, mis.getVehicleMissions())

    def test_add_duplicates(self):
        vehicle = Vehicle("1", [])
        vm = VehicleMission(vehicle, [])
        mis = Mission([vm])

        with self.assertRaises(ValueError):
            mis.addVehicleMission(vm)

    def test_remove(self):
        vehicle = Vehicle("1", [])
        vm = VehicleMission(vehicle, [])
        mis = Mission([vm])

        expectedOut = []
        self.assertEqual(expectedOut, mis.removeVehicleMission(vm))

    def test_remove_element_not_in(self):
        vehicle1 = Vehicle("1", [])
        vm1 = VehicleMission(vehicle1, [])
        vehicle2 = Vehicle("2", [])
        vm2 = VehicleMission(vehicle2, [])
        mis = Mission([vm1, vm2])

        expectedOut = [vm1]
        self.assertEqual(expectedOut, mis.removeVehicleMission(vm2))

    def test_remove_empty(self):
        vehicle = Vehicle("1", [])
        vm = VehicleMission(vehicle, [])
        mis = Mission([])

        expectedOut = []
        self.assertEqual(expectedOut, mis.removeVehicleMission(vm))

    def test_generateMaster_empty(self):
        mis = Mission([])
        mis.generateMasterTasks()

        expectedOut = []
        self.assertEqual(expectedOut, mis.getMasterTasks())

    def test_generateMaster_nonEmpty_2vms(self):
        task1 = Task(1, "", "", "")
        task2 = Task(2, "", "", "")
        task3 = Task(3, "", "", "")
        task4 = Task(4, "", "", "")
        vehicle1 = Vehicle("1", [])
        vehicle2 = Vehicle("1", [])
        vm1 = VehicleMission(vehicle1, [task4, task1])
        vm2 = VehicleMission(vehicle2, [task3, task2])

        mis = Mission([vm1, vm2])
        mis.generateMasterTasks()

        expectedOut = [task1, task2, task3, task4]
        self.assertEqual(expectedOut, mis.getMasterTasks())

    def test_toJSON(self):
        task1 = Task(1, "", "", "")
        task2 = Task(2, "", "", "")
        task3 = Task(3, "", "", "")
        task4 = Task(4, "", "", "")
        vehicle1 = Vehicle("1", [])
        vehicle2 = Vehicle("1", [])
        vm1 = VehicleMission(vehicle1, [task4, task1])
        vm2 = VehicleMission(vehicle2, [task3, task2])

        mis = Mission([vm1, vm2])
        mis.generateMasterTasks()
        print(mis.toJSON())
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()
