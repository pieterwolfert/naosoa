"""
@author: Pieter Wolfert
"""
from visualsystem import VisualSystem
import cv2
from naoqi import ALProxy, ALBroker
import matplotlib.pyplot as plt
import time

class RobotConnect:
    """
    Class for connecting to robot.
    IP has to be a string.
    """
    def __init__(self,name):
        self.name = name

    """
    Get proxy with a given name.
    Returns the specific proxy blob.
    """
    def setProxy(self, name):
        self.nameProxy = ALProxy(name)

    def setMotionProxy(self):
        self.motionProxy = ALProxy("ALMotion")

    def setPostureProxy(self):
        self.postureProxy = ALProxy("ALRobotPosture")

    def setVideoProxy(self):
        self.videoProxy = ALProxy("ALVideoDevice")

def main():
    """
    Main is purely for testing purposes.
    """
    myBroker = ALBroker("myBroker", "0.0.0.0", 0, "192.168.1.143", 9559)
    naomi = RobotConnect("naomi")
    naomi.setVideoProxy()
    vs = VisualSystem(naomi.videoProxy)
    try:
        while True:
            image = vs.capture_frame()
            image = vs.getBall(image)
            cv2.imshow("Image", image)
            vs.getDifference()
            time.sleep(1)
            if cv2.waitKey(33) == 27:
                vs.unsubscribe()
                myBroker.shutdown()
                break #break the while loop
    except KeyboardInterrupt:
        print
        print "Interrupted by user, shutting down"
        myBroker.shutdown()
        sys.exit(0)

if __name__ == '__main__':
    main()
