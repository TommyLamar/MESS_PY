
# REQUIREMENTS:
# 1. Install rosbridge_suite: sudo apt-get install ros-noetic-rosbridge-suite
# 2. Install tf2_web_republisher: sudo apt-get install ros-noetic-tf2-web-republisher
# 3. In a terminal, execute: roslaunch rosbridge_server rosbridge_websocket.launch
# 4. In a terminal, execute: rosrun tf2_web_republisher tf2_web_republisher
# Dependencies: roslibpy

# This sample script demonstrates how a topic can be published to ROS via a .py 
# script. When this script is run in a terminal, it publishes a MESS2UGV message
# until the client connection is terminated.

##################################################################################

import roslibpy
import time

client = roslibpy.Ros(host='localhost', port=9090)
client.run()

talker = roslibpy.Topic(client, '/messop/Turtle01', 'turtlebot3_messop/MESS2UGV')
while client.is_connected:
    talker.publish(roslibpy.Message({'Tx': 0.0, 'Ty': 0.0, 'Rz': 0.1, 'Op': 1}))
    print('Sending message...')
    time.sleep(1)

talker.unadvertise()
client.terminate()
