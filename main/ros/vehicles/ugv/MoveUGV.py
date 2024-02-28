import rospy
from mess_msgs.msg import MessToUGV

def ugvWaypoint(vehicle, tx, ty, rz, op):
    # get topic to publish to
    topic = getTopicString(vehicle.getName())
    print(topic)

    # create publisher
    talker = rospy.Publisher(topic, MessToUGV, queue_size=10)
    rospy.init_node('talker')

    # build message
    msg = MessToUGV()
    msg.Tx = tx
    msg.Ty = ty
    msg.Rz = rz
    msg.Op = op

    # publish message
    talker.publish(msg)


def getTopicString(name):
    return "/" + name + "/messop/messop/vertex"

