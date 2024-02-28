# Obsolete

import os
def saveLaunchFile(vehicleName, filePath):
    s = getLaunchString(vehicleName)
    path = os.getcwd() + filePath
    with open(path, 'w') as file:
        file.write(s)


def getLaunchString(name):
    s = ('<launch>\n'
               '\n'
               '   <!-- Arguments -->\n'
               '   <arg name="ugv_name" default="' + name + '"/>\n'
               '    \n'
               '    <!-- Vehicle Group -->\n'
               '    <group ns="$(arg ugv_name)">\n'
               '    \n'
               '        <!-- Arguments -->\n'
               '        <arg name="model" default="$(env TURTLEBOT3_MODEL)" doc="model type [burger, waffle, waffle_pi]"/>\n'
               '        <arg name="lds_model" default="$(env LDS_MODEL)" doc="LDS MODEL [LDS-01, LDS-02]"/>\n'
               '        \n'
               '        <!-- Parameters -->\n'
               '        <param name="topic_prefix" value="$(arg ugv_name)"/>\n'
               '        <param name="model" value="$(arg model)"/>\n'
               '        \n'
               '        <!-- Other -->\n'
               '        <node pkg="messop_ugv" type="logger" name="messlogger" output="screen"/>\n'
               '        <node pkg="messop_ugv" type="messop" name="messop" output="screen"/>\n'
               '        \n'
               '    </group>\n'
               '</launch>')
    return s

