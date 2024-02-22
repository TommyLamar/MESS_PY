import roslibpy

class MessToUGVLogger_msg:
    def __init__(self, data):
        self.data = data

    def getMessage(self):
        return roslibpy.Message(self.__dict__)