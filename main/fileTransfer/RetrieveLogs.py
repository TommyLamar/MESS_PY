from main.fileTransfer.SCPFuncs import download
from datetime import datetime
from main.mess.Vehicle import Vehicle
import os


def retrieveLogs(localPath, expName, vehicles):
    temp = datetime.now()
    d = temp.day
    mm = temp.month
    y = temp.year
    h = temp.hour
    m = temp.minute
    s = temp.second

    lp = localPath + "/" + expName + "_" + str(d) + "_" + str(mm) + "_" + str(y) + "__" + str(h) + "-" + str(m) + "-" + str(s)
    for v in vehicles:
        # need to update this to not just hard code in user and password
        print("Getting log for vehicle " + v.getName() + " ip: " + v.getIP())
        getLog(v.getName(), lp, v.getIP(), -1, "ubuntu", "turtlebot")
        print("Done getting log for vehicle " + v.getName())


def getLog(name, localPath, host, port, user, password):
    remotePath = "~/catkin_ws/logs"
    lp = localPath + "/" + name
    download(host, localPath, remotePath, user=user, password=password, port=port)


