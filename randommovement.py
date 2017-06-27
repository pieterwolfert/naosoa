"""
author: Pieter Wolfert
"""

import naoqi
import time

class RandomMovement:
    def __init__(self, ALMotionProxy):
        #initialization for random movement
        self.motionProxy = ALMotionProxy
    def moveRandomLimb(self):
        pass#select a limb, move it

    def moveRandomAll(self, epoch):
        # move all limbs to a certain degree

        #move up or down based on epoch
        if epoch % 2 == 0:
            target_angle_legs = [-0.5]
            target_angle_arms = [0.5]
        else:
            target_angle_legs = [0.5]
            target_angle_arms = [-0.5]

        #set speeds for different limbs
        speed = [0.1, 0.1, 0.1, 0.1]
        self.moveLeftLeg(target_angle_legs, speed[0])
        self.moveRightLeg(target_angle_legs, speed[1])
        self.moveLeftArm(target_angle_arms, speed[2])
        self.moveRightArm(target_angle_arms, speed[3])

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

    nr_epochs = 20

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

    randomMovement = RandomMovement(motionProxy)

    for epoch in range(nr_epochs):
        print(epoch)
        randomMovement.moveRandomAll(epoch)
        time.sleep(3)

    # Sit
    postureProxy.goToPosture("LyingBack", 0.7)
    motionProxy.rest()
