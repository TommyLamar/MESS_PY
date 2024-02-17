# Test Cases for the ObstacleMap Class
import unittest
from main.mess.ObstacleMap import *


class TestSetAndGetValues(unittest.TestCase):
    def test_set_get_no_errors(self):
        value = 42
        obMap = ObstacleMap(10, 10)
        obMap.updateValue(1, 1, value)
        self.assertEqual(value, obMap.getValue(1, 1))  # add assertion here

    def test_set_error_exactly_equal(self):
        obMap = ObstacleMap(10, 10)
        with self.assertRaises(IndexError):
            obMap.updateValue(10, 10, 42)

    def test_set_error_row(self):
        obMap = ObstacleMap(10, 10)
        with self.assertRaises(IndexError):
            obMap.updateValue(11, 5, 42)

    def test_set_error_col(self):
        obMap = ObstacleMap(10, 10)
        with self.assertRaises(IndexError):
            obMap.updateValue(5, 11, 42)

    def test_get_error_exactly_equal(self):
        obMap = ObstacleMap(10, 10)
        with self.assertRaises(IndexError):
            obMap.getValue(10, 10)

    def test_get_error_row(self):
        obMap = ObstacleMap(10, 10)
        with self.assertRaises(IndexError):
            obMap.getValue(11, 5)

    def test_get_error_col(self):
        obMap = ObstacleMap(10, 10)
        with self.assertRaises(IndexError):
            obMap.getValue(5, 11)



if __name__ == '__main__':
    unittest.main()
