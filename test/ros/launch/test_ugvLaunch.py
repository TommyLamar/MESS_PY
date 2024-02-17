import unittest
import main.ros.launch.UGVLaunch as ugvl

class MyTestCase(unittest.TestCase):
    def test_something(self):

        print(ugvl.getLaunchString("joe"))
        ugvl.saveLaunchFile("joe", "testLaunchFiles")
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
