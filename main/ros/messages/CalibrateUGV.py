import roslibpy


class CalibrateUGV_msg:
    def __init__(self, c1, c2, c3, c4, c5, c6):
        self.C1 = c1
        self.C2 = c2
        self.C3 = c3
        self.C4 = c4
        self.C5 = c5
        self.C6 = c6

    def getMessage(self):
        return roslibpy.Message(self.__dict__)
