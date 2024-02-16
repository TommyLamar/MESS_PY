import roslibpy


class MesstoUAV_msg:

    def __init__(self, tx, ty):
        self.TX = tx
        self.Ty = ty

    def getMessage(self):
        return roslibpy.Message(self.__dict__)

