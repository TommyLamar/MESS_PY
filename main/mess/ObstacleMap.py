# Obstacle Map
import json

class ObstacleMap:
    def __init__(self, rows, cols):
        self.coords = [[0] * cols] * rows
        self.rows = rows
        self.cols = cols

    def updateValue(self, row, col, val):
        try:
            self.coords[row][col] = val
        except IndexError:
            print("error: coordinate out of bounds of obstacle map")
            raise

    def getValue(self, row, col):
        try:
            return self.coords[row][col]
        except IndexError:
            print("error: coordinate out of bounds of obstacle map")
            raise

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)

    def fromJSON(self, data):
        self.coords = data["coords"]
        self.rows = data["rows"]
        self.cols = data["cols"]
        return self
