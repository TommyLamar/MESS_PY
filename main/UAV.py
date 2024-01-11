# This may get deleted now that uavs are using ros
from Vehicle import *


class UAV(Vehicle):
    ip = "changeMe"

    def __init__(self, ip, id, sensors):
        super().__init__(id, sensors)
        self.ip = ip
