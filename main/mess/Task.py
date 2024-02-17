import json
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

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)

    def fromJSON(self, jsonData):
        self.timeStamp = jsonData["timeStamp"]
        self.taskType = jsonData["taskType"]
        self.message = jsonData["message"]
        self.rosTopicPath = jsonData["rosTopicPath"]
        return self
