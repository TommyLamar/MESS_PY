import unittest
from main.mess.Vehicle import *


class MyTestCase(unittest.TestCase):
    def test_json(self):
        v = Vehicle(1, [])
        s1 = Sensor("s1", 10)
        s2 = Sensor("s2", 20)
        v.addSensor(s1)
        v.addSensor(s2)
        v.setName("monkey")

        jsonstr = v.toJSON()
        with open("testJSONs\\testVehicle.json", "w") as outfile:
            outfile.write(jsonstr)

        temp = ""
        with open("testJSONs\\testVehicle.json", "r") as infile:
            temp = json.load(infile)

        newV = Vehicle(-1, [])
        newV.fromJSON(temp)

        self.assertEqual(v.getName(), newV.getName())
        self.assertEqual(v.getIP(), newV.getIP())
        self.assertEqual(v.getSensors()[0].getName(), newV.getSensors()[0].getName())


if __name__ == '__main__':
    unittest.main()
