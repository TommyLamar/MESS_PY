# This may get deleted now that uavs are using ros
from Vehicle import *


class UAV(Vehicle):
    rosTopicPath = "changeMe"

    def __init__(self, topic, id, sensors):
        super().__init__(id, sensors)
        self.rosTopicPath = topic

    def getTopic(self):
        return self.rosTopicPath

