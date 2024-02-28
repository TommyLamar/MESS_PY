import unittest
import main.ros.launch.UGVMessop as ugvl
import main.ros.launch.UGVBringup as ugvb

class MyTestCase(unittest.TestCase):
    def test_something(self):

        print(ugvb.getLaunchString("mama"))
        ugvb.saveLaunchFile("mama", "/testLaunchFiles")
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
