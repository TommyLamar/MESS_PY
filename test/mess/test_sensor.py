import unittest
from main.Sensor import *
import json


class MyTestCase(unittest.TestCase):
    def test_json(self):
        baseSensor = Sensor("package1", 42)
        baseSensor.setName("Wil")
        jsonstr = baseSensor.toJSON()
        with open("testJSONs\\testSensor.json", "w") as outfile:
            outfile.write(jsonstr)

        temp = ""
        with open("testJSONs\\testSensor.json", "r") as infile:
            temp = json.load(infile)

        newSensor = Sensor("", -1)
        newSensor.fromJSON(temp)

        self.assertEqual(baseSensor.getRate(), newSensor.getRate())
        self.assertEqual(baseSensor.getPackage(), newSensor.getPackage())
        self.assertEqual(baseSensor.getName(), newSensor.getName())

        # add assertion here


if __name__ == '__main__':
    unittest.main()
