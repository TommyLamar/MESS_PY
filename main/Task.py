class Task:
    timeStamp = -1.23
    message = "changeMe"
    rosTopicPath = "changeMe"
    taskType = "changeMe"  # type may be obsolete now that we are using MAVROS

    def __init__(self, time, message, topic, taskType):
        self.timeStamp = time
        self.message = message
        self.rosTopicPath = topic
        self.taskType = taskType

    def getTimeStamp(self):
        return self.timeStamp

    def getMessage(self):
        return self.message

    def getTopic(self):
        return self.rosTopicPath

    def getType(self):
        return self.taskType

