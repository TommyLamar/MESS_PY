import os


def saveLaunchFile(vehicleName, filePath):
    s = getLaunchString(vehicleName)
    path = os.getcwd() + filePath
    with open(path, 'w') as file:
        file.write(s)


def getLaunchString(name):
    s = ('<launch>\n'

         '  <arg name="ugv_name" default="' + name + '"/>\n'

         '  <arg name="multi_robot_name" default=""/>\n'
         '  <arg name="set_lidar_frame_id" default="base_scan"/>\n'
         '  <arg name="model" default="$(env TURTLEBOT3_MODEL)" doc="model type [burger, waffle, waffle_pi]"/>\n'

         '  <node pkg="rosserial_python" type="serial_node.py" name="$(arg ugv_name)_turtlebot3_core" output="screen">\n'
         '      <param name="port" value="/dev/ttyACM0"/>\n'
         '      <param name="baud" value="115200"/>\n'
         '      <param name="tf_prefix" value="$(arg multi_robot_name)"/>\n'

         '      <remap from="battery_state" to="$(arg ugv_name)/batter_state"/>\n'
         '      <remap from="cmd_vel" to="$(arg ugv_name)/cmd_vel"/>\n'
         '      <remap from="cmd_vel_rc100" to="$(arg ugv_name)/cmd_vel_rc100"/>\n'
         '      <remap from="diagnostics" to="$(arg ugv_name)/diagnostics"/>\n'
         '      <remap from="firmware_version" to="$(arg ugv_name)/firmware_version"/>\n'
         '      <remap from="imu" to="$(arg ugv_name)/imu"/>\n'
         '      <remap from="joint_states" to="$(arg ugv_name)/joint_states"/>\n'
         '      <remap from="magnetic_field" to="$(arg ugv_name)/magnetic_field"/>\n'
         '      <remap from="motor_power" to="$(arg ugv_name)/motor_power"/>\n'
         '      <remap from="odom" to="$(arg ugv_name)/odom"/>\n'
         '      <remap from="reset" to="$(arg ugv_name)/reset"/>\n'
         '      <remap from="sensor_state" to="$(arg ugv_name)/sensor_state"/>\n'
         '      <remap from="sound" to="$(arg ugv_name)/sound"/>\n'
         '      <remap from="tf" to="$(arg ugv_name)/tf"/>\n'
         '  </node>\n'

         '  <arg name="set_frame_id" default="base_scan"/>\n'
         '  <arg name="lds_model" default="$(env LDS_MODEL)" doc="LDS MODEL [LDS-01, LDS-02]"/>\n'

         '  <group if = "$(eval lds_model == \'LDS-01\')">\n'
         '      <node pkg="hls_lfcd_lds_driver" type="hlds_laser_publisher" name="$(arg ugv_name)_turtlebot3_lds" output="screen">\n'
         '          <param name="port" value="/dev/ttyUSB0"/>\n'
         '          <param name="frame_id" value="$(arg set_frame_id)"/>\n'

         '          <remap from="rpms" to="$(arg ugv_name)/rpms"/>\n'
         '          <remap from="scan" to="$(arg ugv_name)/scan"/>\n'
         '      </node>\n'
         '  </group>\n'
         '  <group if = "$(eval lds_model == \'LDS-02\')">\n'
         '  <node pkg="ld08_driver" type="ld08_driver" name="$(arg ugv_name)_turtlebot3_lds" output="screen" args="LD08">\n'
         '      <param name="frame_id" value="$(arg set_frame_id)"/>\n'

         '      <remap from="rpms" to="$(arg ugv_name)/rpms"/>\n'
         '      <remap from="scan" to="$(arg ugv_name)/scan"/>\n'
         '      </node>\n'
         '  </group>\n'

         '  <node pkg="turtlebot3_bringup" type="turtlebot3_diagnostics" name="$(arg ugv_name)_turtlebot3_diagnostics" output="screen"/>\n'

         '  <node pkg="messop_ugv" type="messop" name="$(arg ugv_name)_messop" output="screen"/>\n'
         '  <node pkg="messop_ugv" type="logger" name="$(arg ugv_name)_messlogger" output="screen"/>\n'

         '</launch>\n')
    return s
