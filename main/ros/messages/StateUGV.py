import roslibpy


class StateUGV_msg:

    def __init__(self, tx, ty, rz):
        self.Tx = tx
        self.Ty = ty
        self.Rz = rz

    def getMessage(self):
        return roslibpy.Message(self.__dict__)
