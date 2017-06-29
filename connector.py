# -*- coding: utf-8 -*-
"""
@author: WoutervanderWeel
@author: Pieter Wolfert
"""
from visualsystem import VisualSystem
import cv2
from naoqi import ALProxy, ALBroker
import matplotlib.pyplot as plt
import time

class RobotConnect:
    """
    Handles all connections and proxies for the robot.
    """
    def __init__(self,name):
        """Initialize connection object

        Keyword arguments:
        name -- string with name of robot
        """
        self.name = name

    def setProxy(self, name):
        """Sets a proxy to naoqi module.

        Keyword arguments:
        name -- string with name of module to connect to.
        """
        self.unnamedProxy = ALProxy(name)

    def setMotionProxy(self):
        """Sets a naoqi motion proxy."""
        self.motionProxy = ALProxy("ALMotion")

    def setPostureProxy(self):
        """Sets a naoqi posture proxy."""
        self.postureProxy = ALProxy("ALRobotPosture")

    def setVideoProxy(self):
        """Sets a naoqi video proxy."""
        self.videoProxy = ALProxy("ALVideoDevice")

    def setTextProxy(self):
        """Sets a text to speech proxy."""
        self.textProxy = ALProxy("ALTextToSpeech")

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
