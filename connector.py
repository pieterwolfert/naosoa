"""
@author: Pieter Wolfert
"""
from naoqi import ALProxy

class RobotConnect:
    """
    Class for connecting to robot.
    IP has to be a string.
    """
    def __init__(self, ip):
        self.robotip = ip
        self.port = 9559

    """
    Get proxy with a given name.
    Returns the specific proxy blob.
    """
    def setProxy(self, name):
        self.nameProxy = ALProxy(name, self.robotip, self.port)

    def setMotionProxy(self):
        self.motionProxy = ALProxy("ALMotion", self.robotip, self.port)

    def setVideoProxy(self):
        self.videoProxy = ALproxy("ALVideoDevice", self.robotip, self.port)

"""
Main is purely for testing purposes.
"""
def main():
    naomi = RobotConnect("192.168.0.104")
    naomi.setMotionProxy()

if __name__ == '__main__':
    main()
