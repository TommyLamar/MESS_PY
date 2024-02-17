
# REQUIREMENTS:
# 1. Install rosbridge_suite: sudo apt-get install ros-noetic-rosbridge-suite
# 2. Install tf2_web_republisher: sudo apt-get install ros-noetic-tf2-web-republisher
# 3. In a terminal, execute: roslaunch rosbridge_server rosbridge_websocket.launch
# 4. In a terminal, execute: rosrun tf2_web_republisher tf2_web_republisher

# This sample script demonstrates how a topic can be subscribed to from ROS via a 
# .py script. When this script is run in a terminal, it subscribes to a MESS2UGV 
# message until the client connection is terminated.

##################################################################################

import roslibpy

def callback(data):
    Tx = data['Tx']
    Ty = data['Ty']
    Rz = data['Rz']
    Op = data['Op']

    print(str(Tx) + "\t" + str(Ty) + "\t" + str(Rz) + "\t" + str(Op))


client = roslibpy.Ros(host='localhost', port=9090)
client.run()

listener = roslibpy.Topic(client, '/messop/Turtle01', 'turtlebot3_messop/MESS2UGV')
listener.subscribe(callback)

try:
    while True:
        pass
except KeyboardInterrupt:
    client.terminate()