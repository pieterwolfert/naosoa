# -*- coding: utf-8 -*-
"""
@author: WoutervanderWeel
@author: Pieter Wolfert
"""

import naoqi
import time

class Movement:
    """
    Class for movement, can move limbs separately or all together.
    """
    def __init__(self, ALMotionProxy):
        """Sets movement class with given motion proxy."""
        self.motionProxy = ALMotionProxy

    def moveAll(self, limb_speeds, epoch):
        """Moves all limbs.

        Keyword arguments:
        limb_speeds -- speed for the limbs between 0.00 and 1.00
        epoch -- determines whether an up or down movement should be made.
        """
        if epoch % 2 == 0:
            target_angle_legs = [-0.5]
            target_angle_arms = [0.5]
        else:
            target_angle_legs = [0.5]
            target_angle_arms = [-0.5]
        self.moveLeftLeg(target_angle_legs, limb_speeds[0])
        self.moveRightLeg(target_angle_legs, limb_speeds[1])
        self.moveLeftArm(target_angle_arms, limb_speeds[2])
        self.moveRightArm(target_angle_arms, limb_speeds[3])

    def moveLeftLeg(self, target_angle, maxSpeedFraction):
        """Moves left leg.

        Keyword arguments:
        target_angle -- which angle the leg should be put in to
        maxSpeedFraction -- maximum speed of movement between 0.00 and 1.00
        """
        joints = "LHipPitch"
        self.motionProxy.changeAngles(joints, target_angle, maxSpeedFraction)

    def moveRightLeg(self, target_angle, maxSpeedFraction):
        """Moves right leg.

        Keyword arguments:
        target_angle -- which angle the leg should be put in to
        maxSpeedFraction -- maximum speed of movement between 0.00 and 1.00
        """
        joints = "RHipPitch"
        self.motionProxy.changeAngles(joints, target_angle, maxSpeedFraction)

    def moveLeftArm(self, target_angle, maxSpeedFraction):
        """Moves left arm.

        Keyword arguments:
        target_angle -- which angle the leg should be put in to
        maxSpeedFraction -- maximum speed of movement between 0.00 and 1.00
        """
        joints = "LShoulderPitch"
        self.motionProxy.changeAngles(joints, target_angle, maxSpeedFraction)

    def moveRightArm(self, target_angle, maxSpeedFraction):
        """Moves right arm.

        Keyword arguments:
        target_angle -- which angle the leg should be put in to
        maxSpeedFraction -- maximum speed of movement between 0.00 and 1.00
        """
        joints = "RShoulderPitch"
        self.motionProxy.changeAngles(joints, target_angle, maxSpeedFraction)

def main():
    """Used for testing purposes."""
    ip = '192.168.1.143'
    port = 9559
    nr_epochs = 10
    # Create posture proxy
    postureProxy = naoqi.ALProxy("ALRobotPosture", ip, port)
    # Create motion proxy
    motionProxy = naoqi.ALProxy("ALMotion", ip, port)
    postureProxy.goToPosture("LyingBack", 0.7)
    #Set joints to standard position
    joints = ["LShoulderPitch", "RShoulderPitch", "RElbowRoll", "LElbowRoll",\
                "LHipPitch", "RHipPitch", "LKneePitch", "RKneePitch"]
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

if __name__ == "__main__":
    main()
