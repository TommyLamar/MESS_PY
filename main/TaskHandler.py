from Task import *
##import rospy #comment out for development on windows since rospy is linux only

class TaskHandler:
    task = Task(-1.23, "changeMe", "changeMe", "changeMe")
    output = "defaultOutput"

    def __init__(self, task):
        self.task = task
