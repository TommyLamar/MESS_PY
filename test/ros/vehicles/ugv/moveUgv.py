import main.ros.vehicles.ugv.MoveUGV as mugv
from main.mess.Vehicle import *


def run():
    host = "192.168.0.139"
    v = Vehicle(host, [], name="burger1")
    mugv.ugvWaypoint(v, 1.0, 0.71, 0, 2)


if __name__ == "__main__":
    run()
