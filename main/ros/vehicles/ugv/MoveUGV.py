import rospy
from mess_msgs.msg import MessToUGV
from std_msgs.msg import Bool

pointReached = True

def ugvWaypoint(vehicle, tx, ty, rz, op):
    # get topic to publish to
    topic = getVertexTopicString(vehicle.getName())
    print(topic)


    # create publisher
    talker = rospy.Publisher(topic, MessToUGV, queue_size=10)
    rospy.init_node('ugvWaypointPublisher', anonymous=True)
    rate = rospy.Rate(10)

    # build message
    msg = MessToUGV()
    msg.Tx = tx
    msg.Ty = ty
    msg.Rz = rz
    msg.Op = op

    # publish message
    talker.publish(msg)


def getVertexTopicString(name):
    return "/" + name + "/messop/messop/vertex"


def flagCallback(data):
    global pointReached
    pointReached = data.data


def ugvNavigateWaypoints(vehicle, points):
    global pointReached
    vertexTopic = getVertexTopicString(vehicle.getName())
    flagTopic = getFlagTopicString(vehicle.getName())

    rospy.init_node('ugvWaypoints', anonymous=True)
    talker = rospy.Publisher(vertexTopic, MessToUGV, queue_size=10)

    rospy.init_node('vertexTalker')

    for point in points:
        # build message
        msg = MessToUGV()
        msg.Tx = point.tx
        msg.Ty = point.ty
        msg.Rz = point.rz
        msg.Op = point.op

        talker.publish(msg)
        while not pointReached:
            rospy.Subscriber(flagTopic, Bool, flagCallback)


def getFlagTopicString(name):
    return "/" + name + "/messop/messop/transitionFlag"


