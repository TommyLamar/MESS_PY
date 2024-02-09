from main.Task import *
import roslibpy
import json

class TaskHandler:
    task = Task(-1.23, "changeMe", "changeMe", "changeMe")
    output = "defaultOutput"

    def __init__(self, task):
        self.task = task

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)

    def fromJSON(self):
        return self