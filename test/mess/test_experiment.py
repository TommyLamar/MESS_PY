import unittest
from main.Experiment import *


# placeholder
class ExperimentTestCase1(unittest.TestCase):
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
        e = Experiment(mis, [vehicle1, vehicle2], [], ObstacleMap(1,1))
        print(e.toJSON())
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
