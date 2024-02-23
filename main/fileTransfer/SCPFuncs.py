from paramiko import SSHClient
from scp import SCPClient
import os

def upload(host, localPath, remotePath, user="ubuntu", password="turtlebot", port=-1):
    ssh = initClient(host, user, password, port)
    scp = SCPClient(ssh.get_transport())
    scp.put(localPath, recursive=True, remote_path=remotePath)
    scp.close()
    ssh.close()


def download(host, localPath, remotePath,user="ubuntu", password="turtlebot",  port=-1):
    ssh = initClient(host, user, password, port)

    scp = SCPClient(ssh.get_transport())
    scp.get(remote_path=remotePath, local_path=localPath, recursive=True)
    scp.put(localPath, recursive=True, remote_path=remotePath)
    scp.close()
    ssh.close()


def initClient(host, user, password, port):
    ssh = SSHClient()
    ssh.load_system_host_keys()
    if port == -1:
        ssh.connect(host, username=user, password=password)
    else:
        ssh.connect(host, port, username=user, password=password)

    return ssh




