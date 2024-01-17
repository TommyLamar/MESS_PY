# Obstacle Map


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
