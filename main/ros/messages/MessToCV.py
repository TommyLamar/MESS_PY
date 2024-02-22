import roslibpy


class MessToCV:

    def __init__(self, tx, ty, tz, rx, ry, rz):
        self.Tx = tx
        self.Ty = ty
        self.Tz = tz
        self.Rx = rx
        self.Ry = ry
        self.Rz = rz

    def getMessage(self):
        return roslibpy.Message(self.__dict__)
