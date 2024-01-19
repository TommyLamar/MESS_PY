from main.Task import *
import roslibpy

class TaskHandler:
    task = Task(-1.23, "changeMe", "changeMe", "changeMe")
    output = "defaultOutput"

    def __init__(self, task):
        self.task = task
