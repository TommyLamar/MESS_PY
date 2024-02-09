import unittest
from main.Task import *

class TestToJson(unittest.TestCase):
    def test_something(self):
        task = Task(1.23, "hello", "world", "monkey")
        print(task.toJSON())
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
