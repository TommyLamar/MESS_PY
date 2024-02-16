import unittest
from main.ros.messages.CalibrateUGV import *

class MyTestCase(unittest.TestCase):
    def test_something(self):
        msg = CalibrateUGV_msg(1, 2, 3, 4, 5, 6)
        msg.getMessage()
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
