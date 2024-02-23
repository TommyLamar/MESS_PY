import main.ros.launch.UGVBringup as ugvb
import main.ros.launch.UGVMessop as ugvm
import main.ros.launch.UAVBringup as uavb
import main.ros.launch.UAVMessop as uavm
from main.fileTransfer.SCPFuncs import upload
from paramiko import *


class LaunchFile:
    def __init__(self, vehicle, localPath):
        name = vehicle.getName()
        self.vehicle = vehicle
        self.localPath = localPath
        self.bringupPath = localPath + '\\' + name + "_bringup.launch"
        print(self.bringupPath)
        self.messopPath = localPath + '\\' + name + "_messop.launch"
        self.saveFiles()

    def saveFiles(self):
        if self.vehicle.getType() == "UGV":
            ugvb.saveLaunchFile(self.vehicle.getName(), self.bringupPath)
            ugvm.saveLaunchFile(self.vehicle.getName(), self.messopPath)
        elif self.vehicle.getType() == "UAV":
            uavb.saveLaunchFile(self.vehicle.getName(), self.bringupPath)
            uavm.saveLaunchFile(self.vehicle.getName(), self.messopPath)

    def execute(self, remotePath):
        ssh = SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(AutoAddPolicy())

        host = self.vehicle.getIP()

        bufn = self.vehicle.getName() + "_bringup.launch"
        mfn = self.vehicle.getName() + "_messop.launch"
        buildCMD = "catkin_make"
        bringupCMDExe = ""
        messopCMDExe = ""

        if self.vehicle.getType() == "UGV":
            # should have a way in the future to not hard code this
            user = "ubuntu"
            password = "turtlebot"
            upload(host, self.messopPath, remotePath, user=user, password=password)
            upload(host, self.bringupPath, remotePath, user=user, password=password)
            ssh.connect(host, username=user, password=password)
            bringupCMDExe = "roslaunch messop_ugv " + bufn
            messopCMDExe = "roslaunch messop_ugv " + mfn
        elif self.vehicle.getType() == "UAV":
            # Place holders values for user and password for now,
            # todo figure what uav user and password is and also make it not hardcoded
            user = ""
            password = ""
            upload(host, self.messopPath, remotePath, user=user, password=password)
            upload(host, self.bringupPath, remotePath, user=user, password=password)
            ssh.connect(host, username=user, password=password)
            bringupCMDExe = "roslaunch messop_uav " + bufn
            messopCMDExe = "roslaunch messop_uav " + mfn

        (stdin, stdout, stderr) = ssh.exec_command(buildCMD)  # first build everything
        stdout.channel.recv_exit_status()  # blocks until finished running

        (stdin, stdout, stderr) = ssh.exec_command(bringupCMDExe)  # then execute bringup command
        stdout.channel.recv_exit_status()  # blocks until finished running

        (stdin, stdout, stderr) = ssh.exec_command(messopCMDExe)  # then execute messop command
        stdout.channel.recv_exit_status()  # blocks until finished running