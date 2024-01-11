class Task:
    timeStamp = -1.23
    message = "changeMe"
    rosTopicPath = "changeMe"
    taskType = "changeMe"

    def __init__(self, time, message, topic, type):
        self.timeStamp = time
        self.message = message
        self.rosTopicPath = topic
        self.taskType = type

