import main.ros.launch.UGVBringup as ugvb
import main.ros.launch.UAVBringup as uavb
import main.ros.launch.UGVPackage as ugvp
from main.fileTransfer.SCPFuncs import upload
from paramiko import *
from time import sleep
import os


class LaunchFile:
    def __init__(self, vehicle, localPath):
        name = vehicle.getName()
        self.vehicle = vehicle
        self.localPath = localPath
        self.packagePath = localPath + "\\package.xml"
        self.bringupPath = localPath + '/' + name + "_bringup.launch"
        self.messopPath = localPath + '/' + name + "_messop.launch"
        self.saveFiles()

    def saveFiles(self):
        if self.vehicle.getType() == "UGV":
            ugvb.saveLaunchFile(self.vehicle.getName(), '/' + self.bringupPath)
        elif self.vehicle.getType() == "UAV":
            uavb.saveLaunchFile(self.vehicle.getName(), self.bringupPath)

    def execute(self, remotePath):
        print("creating a client")
        ssh = SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(AutoAddPolicy())

        print("getting Vehicle IP")
        host = self.vehicle.getIP()

        bufn = self.vehicle.getName() + "_bringup.launch"

        bringupCMDExe = ""

        launchPath = remotePath + "/messop_ugv/launch"

        while not os.path.exists(self.bringupPath):  # the first char is a / which messes up the exists command
            sleep(1)
            print("waiting for file to exist at " + self.bringupPath)

        if self.vehicle.getType() == "UGV":
            # should have a way in the future to not hard code this
            user = "ubuntu"
            password = "turtlebot"
            temp = upload(host, self.bringupPath, launchPath, user=user, password=password)
            ssh.connect(host, username=user, password=password)
            bringupCMDExe = "roslaunch messop_ugv " + bufn
        elif self.vehicle.getType() == "UAV":
            # Place holders values for user and password for now,
            # todo figure what uav user and password is and also make it not hardcoded
            user = ""
            password = ""
            upload(host, self.bringupPath, remotePath, user=user, password=password)
            ssh.connect(host, username=user, password=password)
            bringupCMDExe = "roslaunch messop_uav " + bufn

        (stdin, stdout, stderr) = ssh.exec_command(bringupCMDExe)  # then execute messop command
        stdout.channel.recv_exit_status()  # blocks until finished running
