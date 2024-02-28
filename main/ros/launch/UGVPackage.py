# Obsolete

import os


def savePackageFile(filePath):
    s = buildPackageString()
    path = os.getcwd() + filePath
    with open(path, 'w') as file:
        file.write(s)


def buildPackageString():
    s = ('<?xml version="1.0"?>\n'
         '  <package format="2">\n'
         '  <name>messop_ugv</name>\n'
         '  <version>1.0.0</version>\n'
         '  <description>The messop_ugv package</description>\n'
         '  <url type="website">https://github.com/marinarasauced/messop_ugv</url>\n'
         '  <maintainer email="mjnelson@wpi.edu">Marina Nelson</maintainer>\n'
         '  <author email="mjnelson@wpi.edu">Marina Nelson</author>\n'
         '  <license>TO DO</license>\n'
         '  <buildtool_depend>catkin</buildtool_depend>\n'
         '  <build_depend>geometry_msgs</build_depend>\n'
         '  <build_depend>mess_msgs</build_depend>\n'
         '  <build_depend>nav_msgs</build_depend>\n'
         '  <build_depend>rospy</build_depend>\n'
         '  <build_depend>sensor_msgs</build_depend>\n'
         '  <build_depend>std_msgs</build_depend>\n'
         '  <build_export_depend>geometry_msgs</build_export_depend>\n'
         '  <build_export_depend>mess_msgs</build_export_depend>\n'
         '  <build_export_depend>nav_msgs</build_export_depend>\n'
         '  <build_export_depend>rospy</build_export_depend>\n'
         '  <build_export_depend>sensor_msgs</build_export_depend>\n'
         '  <build_export_depend>std_msgs</build_export_depend>\n'
         '  <exec_depend>geometry_msgs</exec_depend>\n'
         '  <exec_depend>mess_msgs</exec_depend>\n'
         '  <exec_depend>nav_msgs</exec_depend>\n'
         '  <exec_depend>rospy</exec_depend>\n'
         '  <exec_depend>sensor_msgs</exec_depend>\n'
         '  <exec_depend>std_msgs</exec_depend>\n'
         '  <export>\n'
         '  </export>\n'
         '</package>')
    return s