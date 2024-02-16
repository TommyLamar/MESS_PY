import roslibpy


class MessToUGV_msg:

    def __init__(self, tx, ty, rz, op):
        self.Tx = tx
        self.Ty = ty
        self.Rz = rz
        self.Op = op

    def getMessage(self):
        return roslibpy.Message(self.__dict__)