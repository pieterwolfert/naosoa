"""
author: Pieter Wolfert
"""

import naoqi

class RandomMovement:
    def __init__(self, ALMotionProxy):
        #initialization for random movement
        self.motionproxy = ALMotionProxy
    def moveRandomLimb(self):
        pass#select a limb, move it

    def moveRandomAll(self, epoch):
        # move all limbs to a certain degree

        #move up or down based on epoch
        if epoch % 2 == 0:
            target_angle = [-.5]
        else:
            target_angle = [.5]

        #set speeds for different limbs
        speed = [0.2, 0.4, 0.6, 0.8]
        self.moveLeftLeg(target_angle, speed[0])
        self.moveRightLeg(target_angle, speed[1])
        self.moveLeftArm(target_angle, speed[2])
        self.moveRightArm(target_angle, speed[3])

    def moveLeftLeg(self, target_angle, maxSpeedFraction):
        #move left leg
        joints = "LHipPitch"
        self.motionProxy.changeAngles(joints, target_angle, maxSpeedFraction)
    def moveRightLeg(self, target_angle, maxSpeedFraction):
        #move right leg
        joints = "RHipPitch"
        self.motionProxy.changeAngles(joints, target_angle, maxSpeedFraction)
    def moveLeftArm(self, target_angle, maxSpeedFraction):
        #move left arm
        joints = "LShoulderPitch"
        self.motionProxy.changeAngles(joints, target_angle, maxSpeedFraction)
    def moveRightArm(self, target_angle, maxSpeedFraction):
        #move right arm
        joints = "RShoulderPitch"
        self.motionProxy.changeAngles(joints, target_angle, maxSpeedFraction)

if __name__ == "__main__":

    ip = '192.168.1.138'
    port = '9559'

    nr_epochs = 10

    # Create posture proxy
    postureProxy = naoqi.ALProxy("ALRobotPosture", ip, port)
    # Create motion proxy
    motionProxy = naoqi.ALProxy("ALMotion", ip, port)

    postureProxy.goToPosture("LyingBack", 0.7)

    randomMovement = RandomMovement(motionProxy)

    for epoch in range(nr_epochs):
        randomMovement.moveRandomAll(epoch)

    # Sit
    postureProxy.goToPosture("LyingBack", 0.7)
    motionProxy.rest()
