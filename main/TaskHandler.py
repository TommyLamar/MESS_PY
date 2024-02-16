from main.Task import *
import roslibpy
import json

flag = [True]
class TaskHandler:
    task = Task(-1.23, "changeMe", "changeMe", "changeMe")
    output = "defaultOutput"

    def __init__(self, task):
        self.task = task

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)

    def fromJSON(self):
        return self

    def executeTask(self):
        client = roslibpy.Ros(host="localhost", port=9090) # placeholder
        client.run()
        if self.task.getType() == "publish":
            print("foo")

        elif self.task.getType() == "subscribe":
            print("bar")
        else:
            print("Error, task fo invalid type")

        while flag[0]:  # wait for flag to be turned off
            pass  # do nothing

        client.terminate()
