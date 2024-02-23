# so I wrote this before I realized roslibpy is for ROS 2 and not ROS 1
# Maybe it will be useful in the future so merry Christmas if it is!
import roslibpy


class RosClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client = roslibpy.Ros(host=host, port=port)
        self.publishers = []
        self.subscribers = []
        self.client.run()

    def getClient(self):
        return self.client

    def getHost(self):
        return self.host

    def getPort(self):
        return self.port

    def addPublisher(self, name, messageType):
        talker = roslibpy.Topic(self.client, name, messageType)
        self.publishers.append(talker)

    def publish(self, name, msg):
        for talker in self.publishers:
            if talker.name == name:
                talker.publish(msg)

    def addSubscriber(self, name, msg):
        listener = roslibpy.Topic(self.client, name, msg)
        self.subscribers.append(listener)

    def subscribe(self, name, callback):
        for listener in self.subscribers:
            if listener.name == name:
                listener.subscribe(callback)

    def terminate(self):
        self.client.terminate()

