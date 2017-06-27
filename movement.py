"""
author: Pieter Wolfert
"""

import naoqi
import time

class Movement:
    def __init__(self, ALMotionProxy):
        """
        Class for movement, can move limbs separately or all together.
        """
        self.motionProxy = ALMotionProxy

    def moveLimb(self):
        pass#select a limb, move it

    def moveAll(self, limb_speeds, epoch):
        # move all limbs to a certain degree

        #move up or down based on epoch
        if epoch % 2 == 0:
            target_angle_legs = [-0.5]
            target_angle_arms = [0.5]
        else:
            target_angle_legs = [0.5]
            target_angle_arms = [-0.5]

        #set speeds for different limbs
        #limb_speeds = [((0.1+1.0*epoch)%10)/10, ((5.1+1.0*epoch)%10)/10, ((2.5+1.0*epoch)%10)/10, ((7.5+1.0*epoch)%10)/10]
        self.moveLeftLeg(target_angle_legs, limb_speeds[0])
        self.moveRightLeg(target_angle_legs, limb_speeds[1])
        self.moveLeftArm(target_angle_arms, limb_speeds[2])
        self.moveRightArm(target_angle_arms, limb_speeds[3])

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

    ip = '192.168.1.143'
    port = 9559

    nr_epochs = 10

    # Create posture proxy
    postureProxy = naoqi.ALProxy("ALRobotPosture", ip, port)
    # Create motion proxy
    motionProxy = naoqi.ALProxy("ALMotion", ip, port)

    postureProxy.goToPosture("LyingBack", 0.7)

    #Set joints to standard position
    joints = ["LShoulderPitch", "RShoulderPitch", "RElbowRoll", "LElbowRoll", "LHipPitch", "RHipPitch", "LKneePitch", "RKneePitch"]
    target_angle = [-0.1, -0.1, 0.0, 0.0, -0.1, -0.1, 0.0, 0.0]
    maxSpeedFraction = 0.4
    motionProxy.setAngles(joints, target_angle, maxSpeedFraction)
    time.sleep(2)

    randomMovement = Movement(motionProxy)

    for epoch in range(nr_epochs):
        print(epoch)
        randomMovement.moveAll(epoch)
        time.sleep(3)

    # Sit
    postureProxy.goToPosture("LyingBack", 0.7)
    motionProxy.rest()
