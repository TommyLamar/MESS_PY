import unittest
from main.fileTransfer.SCPFuncs import upload


class MyTestCase(unittest.TestCase):
    def test_put(self):
        host = "192.168.0.139" #turtlebot
        lp = "testFiles/helloTB.txt"
        rp = "~/tstDir"
        x = upload(host, lp, rp)
        self.assertEqual(x, 1)  # add assertion here


if __name__ == '__main__':
    unittest.main()
