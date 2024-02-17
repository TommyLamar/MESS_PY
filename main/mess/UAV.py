# This may get deleted now that uavs are using ros
from Vehicle import *
import json


class UAV(Vehicle):
    ip = "changeMe"

    def __init__(self, ip, id, sensors):
        super().__init__(id, sensors)
        self.ip = ip


    def getIP(self):
        return self.ip

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)

    def fromJSON(self):
        return self