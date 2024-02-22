# This code is a slightly modified version of the code made by Marina Nelson
# https://github.com/marinarasauced/messcv/blob/main/scripts/threat

import numpy as np
from main.ros.messages.MessToCV import MessToCV
import cv2
from main.ros.RosClient import RosClient


def pointDot(v1, v2):
    return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z


def pointNorm(v1):
    return np.sqrt(v1.x ** 2 + v1.y ** 2 + v1.z ** 2)


class Point:
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)


class ComputerVision:
    def __init__(self, name="UAV00", labRes=0.2, camOpticsx=62.2, camOpticsy=48.8, imgResx=1280, imgResy=960,
                 domainX=5.0, domainY=3.5):
        self.uavName = name
        self.labRes = labRes
        self.optics = np.array([[camOpticsx], [camOpticsy]])
        self.imgRes = np.array([[imgResx], [imgResy]])
        self.domainX = np.arange(-domainX, domainX, labRes)
        self.domainY = np.arange(-domainY, domainY, labRes)
        self.globalX, self.globalY = np.meshgrid(domainX, domainY)
        self.globalR = np.zeros((self.globalX.shape[0], self.globalX.shape[1]))
        self.globalG = np.zeros((self.globalX.shape[0], self.globalX.shape[1]))
        self.globalB = np.zeros((self.globalX.shape[0], self.globalX.shape[1]))
        self.globalN = np.zeros((self.globalX.shape[0], self.globalX.shape[1]))
        self.labenv = np.stack((self.globalX, self.globalY, self.globalR, self.globalG, self.globalB, self.globalN),
                               axis=2)
        self.shouldSample = True
        self.globalCurr = MessToCV(0.0, 0.0, 0.0, 0.0, 0.0, 0.0)

    def getOptics(self):
        return self.optics

    def getCorner(self, tx, ty, tz, rx, ry, rz, i):
        v0 = Point(0.0, 0.0, -1.0)
        vi = Point(0.0, 0.0, -1.0)
        # Corner point:
        if i == 1:
            vi = Point(tz * np.tan(rx + 0.5 * self.optics[0, 0]), tz * np.tan(ry + 0.5 * self.optics[1, 0]), -tz)
        elif i == 2:
            vi = Point(tz * np.tan(rx - 0.5 * self.optics[0, 0]), tz * np.tan(ry + 0.5 * self.optics[1, 0]), -tz)
        elif i == 3:
            vi = Point(tz * np.tan(rx - 0.5 * self.optics[0, 0]), tz * np.tan(ry - 0.5 * self.optics[1, 0]), -tz)
        elif i == 4:
            vi = Point(tz * np.tan(rx + 0.5 * self.optics[0, 0]), tz * np.tan(ry - 0.5 * self.optics[1, 0]), -tz)

        gamma = np.arccos(pointDot(v0, vi) / (pointNorm(v0) * pointNorm(vi)))
        beta = np.arctan(np.tan(0.5 * self.optics[1, 0]) / np.tan(0.5 * self.optics[0, 0]))
        alpha = np.array([beta, np.pi - beta, beta - np.pi, -beta])
        distance = tz * np.tan(gamma)

        x = distance * np.cos(alpha[i - 1])
        y = distance * np.sin(alpha[i - 1])

        x_ = tx + x * np.cos(rz - np.pi / 2) - y * np.sin(rz - np.pi / 2)
        y_ = ty + x * np.sin(rz - np.pi / 2) + y * np.cos(rz - np.pi / 2)

        return Point(x_, y_, 0.0)

    def callBackFlags(self, data):
        xs = self.labenv[:, :, 0].reshape(-1, 1)
        ys = self.labenv[:, :, 1].reshape(-1, 1)
        colors = self.labenv[:, :, 2:5].reshape(-1, 3) / 255
        fname = "labenv.csv"  # TO DO, give some unique name
        np.savetxt(fname, np.concatenate((xs, ys, colors), axis=1), delimiter=",")
        print("Computer Vision Data Logged")

    def callBackState(self, data):
        self.globalCurr.Tx = data.Tx
        self.globalCurr.Ty = data.Ty
        self.globalCurr.Tz = data.Tz
        self.globalCurr.Rx = data.Rx
        self.globalCurr.Ry = data.Ry
        self.globalCurr.Rz = data.Rz
        self.shouldSample = True

    def callbackImage(self, data):
        if self.shouldSample:
            self.shouldSample = False
            array = np.frombuffer(data.data, np.uint8)
            image = cv2.imdecode(array, cv2.IMREAD_COLOR)
            dimensions = image.shape

            if image is not None:
                self.processImage(image, dimensions)

    def processImage(self, data, dimensions):
        # Import data of current state:
        Tx = self.globalCurr.Tx
        Ty = self.globalCurr.Ty
        Tz = self.globalCurr.Tz
        Rx = self.globalCurr.Rx
        Ry = self.globalCurr.Ry
        Rz = self.globalCurr.Rz

        # Source points:
        S1 = self.getCorner(0.0, 0.0, Tz, 0.0, 0.0, np.pi / 2, 1)
        S2 = self.getCorner(0.0, 0.0, Tz, 0.0, 0.0, np.pi / 2, 2)
        S3 = self.getCorner(0.0, 0.0, Tz, 0.0, 0.0, np.pi / 2, 3)
        S4 = self.getCorner(0.0, 0.0, Tz, 0.0, 0.0, np.pi / 2, 4)

        # Destination points:
        D1 = self.getCorner(Tx, Ty, Tz, Rx, Ry, Rz, 1)
        D2 = self.getCorner(Tx, Ty, Tz, Rx, Ry, Rz, 2)
        D3 = self.getCorner(Tx, Ty, Tz, Rx, Ry, Rz, 3)
        D4 = self.getCorner(Tx, Ty, Tz, Rx, Ry, Rz, 4)

        # Memory allocation:
        S_ = np.array([[S1.x, S1.y], [S2.x, S2.y], [S3.x, S3.y], [S4.x, S4.y]])
        D_ = np.array([[D1.x, D1.y], [D2.x, D2.y], [D3.x, D3.y], [D4.x, D4.y]])
        A_ = np.zeros((8, 8), dtype=np.float64)
        B_ = np.zeros((8, 1), dtype=np.float64)

        # Matrix & vector needed to obtain homogeneous transformation matrix:
        for i in range(4):
            # Update first of rows:
            A_[2 * i, 0] = S_[i, 0]
            A_[2 * i, 1] = S_[i, 1]
            A_[2 * i, 2] = 1.0
            A_[2 * i, -2] = -S_[i, 0] * D_[i, 0]
            A_[2 * i, -1] = -S_[i, 1] * D_[i, 0]
            B_[2 * i, 0] = D_[i, 0]

            # Update second of rows:
            A_[2 * i + 1, 3] = S_[i, 0]
            A_[2 * i + 1, 4] = S_[i, 1]
            A_[2 * i + 1, 5] = 1.0
            A_[2 * i + 1, -2] = -S_[i, 0] * D_[i, 1]
            A_[2 * i + 1, -1] = -S_[i, 1] * D_[i, 1]
            B_[2 * i + 1, 0] = D_[i, 1]

        # Projection domain and range:
        X_ = np.linspace(np.min(S_[:, 0]), np.max(S_[:, 0]), self.imgRes[0, 0])
        Y_ = np.linspace(np.min(S_[:, 1]), np.max(S_[:, 1]), self.imgRes[1, 0])
        XP_, YP_ = np.meshgrid(X_, Y_)
        XP = XP_.reshape(1, -1)
        YP = YP_.reshape(1, -1)
        source = np.vstack((XP, YP, np.ones((1, XP.shape[1]))))

        # Homogeneous transformation matrix:
        coefficients = np.append(np.dot(np.linalg.inv(A_), B_), np.array([[1.0]]), axis=0)
        H_ = coefficients.reshape((3, 3))

        # Pixel mapping:
        destination = np.dot(H_, source)
        projection = np.vstack((destination[0, :] / destination[2, :], destination[1, :] / destination[2, :]))
        projection = self.labRes * np.rint(projection / self.labRes)
        indices = np.lexsort(projection[0:2, :])
        projection = projection[:, indices]

        # Pixel RGB generation:
        RGB = data.reshape(-1, 3)
        Red = RGB[:, 2]
        Green = RGB[:, 1]
        Blue = RGB[:, 0]

        col1 = 0
        col2 = 0
        upper = projection.shape[1]
        while col2 < upper - 1:

            # Column indices of current x value in projection:
            while projection[0, col1] == projection[0, col2] and col2 < upper - 1:
                col2 += 1

            # Column indices of current x and y values in projection:
            tracking = projection[:, col1:col2]
            tracked = col1 + np.where(tracking[1, :] == projection[1, col1])[0]

            # Global index of current x and y value:
            globalIx = np.where(np.abs(self.domainX - projection[0, col1]) < self.labRes ** 2)[0]
            globalIy = np.where(np.abs(self.domainY - projection[1, col1]) < self.labRes ** 2)[0]

            # Initial RBG values:
            R0 = self.labenv[globalIy, globalIx, 2]
            G0 = self.labenv[globalIy, globalIx, 3]
            B0 = self.labenv[globalIy, globalIx, 4]
            N0 = self.labenv[globalIy, globalIx, 5]

            # RGB values to be added:
            N1 = col2 - col1
            R1 = np.sqrt((Red[col1:col2] ** 2).sum(0) / N1)
            G1 = np.sqrt((Green[col1:col2] ** 2).sum(0) / N1)
            B1 = np.sqrt((Blue[col1:col2] ** 2).sum(0) / N1)

            # Update lab environment tracking matrix:
            self.labenv[globalIy, globalIx, 2] = np.sqrt((N0 * R0 ** 2 + N1 * R1 ** 2) / (N0 + N1))
            self.labenv[globalIy, globalIx, 3] = np.sqrt((N0 * G0 ** 2 + N1 * G1 ** 2) / (N0 + N1))
            self.labenv[globalIy, globalIx, 4] = np.sqrt((N0 * B0 ** 2 + N1 * B1 ** 2) / (N0 + N1))
            self.labenv[globalIy, globalIx, 5] += N1

            # Update column index for next iteration:
            col1 = col2

    def connect2ros(self, client):

        stateName = "/messop/" + self.uavName + "/state"
        imageName = "/raspicam_node/image/compressed"
        flagName = "/messop/flags/cv"

        stateMessage = ""  # todo
        imageMessage = ""  # todo
        flagMessage = ""  # todo

        client.addSubscriber(imageName, stateMessage)
        client.addSubscriber(stateName, imageMessage)
        client.addSubscriber(flagName, flagMessage)

        client.subscribe(stateName, self.callBackState)
        client.subscribe(imageName, self.callbackImage)
        client.subscribe(flagName, self.callBackFlags)

