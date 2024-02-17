# This may get deleted now that uavs are using ros
from Vehicle import *
import json


class UAV(Vehicle):
    rosTopicPath = "changeMe"

    def __init__(self, topic, id, sensors):
        super().__init__(id, sensors)
        self.rosTopicPath = topic

    def getTopic(self):
        return self.rosTopicPath

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)

    def fromJSON(self):
        return self