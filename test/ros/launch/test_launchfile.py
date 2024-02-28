from main.ros.launch import LaunchFile as lf
from main.mess.Vehicle import *


def put():
    host = "192.168.0.139" #turtlebot
    lp = "testFiles/helloTB.txt"
    rp = "~/tstDir"
    print("Made vehicle")
    vehicle = Vehicle(host, [], name="burger1")
    mylf = lf.LaunchFile(vehicle, "testLaunchFiles")
    mylf.execute("~/catkin_ws/src")


if __name__ == '__main__':
    put()
