class ObstacleMap:
    coords = [[-999]*100]*100

    def __init__(self, rows, cols):
        self.coords = [[0] * cols] * rows
