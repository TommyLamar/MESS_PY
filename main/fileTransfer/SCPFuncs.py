from paramiko import SSHClient
from scp import SCPClient


def upload(host, localPath, remotePath, port=-1):
    ssh = SSHClient()
    ssh.load_system_host_keys()
    if port == -1:
        ssh.connect(host)
    else:
        ssh.connect(host, port)

    scp = SCPClient(ssh.get_transport())
    scp.put(localPath, recursive=True, remote_path=remotePath)
    scp.close()


def download(host, localPath, remotePath, port=-1):
    ssh = SSHClient()
    ssh.load_system_host_keys()
    if port == -1:
        ssh.connect(host)
    else:
        ssh.connect(host, port)

    scp = SCPClient(ssh.get_transport())
    scp.get(remote_path=remotePath, local_path=localPath, recursive=True)
    scp.put(localPath, recursive=True, remote_path=remotePath)
    scp.close()


