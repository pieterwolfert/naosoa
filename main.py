from connector import RobotConnect
from comparator import Comparator
from visualsystem import VisualSystem
from movement import Movement
from integrator import Integrator
import cv2
import naoqi
import time
import random

myBroker = None

def setParameters():
    """
    Setting broker to connect to the robot.
    """
    ip = '192.168.1.143'
    port = 9559
    myBroker = naoqi.ALBroker("myBroker", "0.0.0.0", 0, ip, port)
    connector = RobotConnect("Naomi")
    connector.setPostureProxy()
    connector.setMotionProxy()
    connector.setVideoProxy()
    return connector

def objectSpeed(vs):
    """
    Calculates the speed of the ball. Plots the camera output.
    """
    image = vs.capture_frame()
    image = vs.getBall(image)
    cv2.imshow("Image", image)
    return vs.getDifference()


def main():
    """
    Instantiate all needed classes
    """
    job = setParameters()
    vs = VisualSystem(job.videoProxy)
    movement = Movement(job.motionProxy)

    """
    Preparations
    """
    job.postureProxy.goToPosture("LyingBack", 0.7)
    #Set joints to standard position
    joints = ["LShoulderPitch", "RShoulderPitch", "RElbowRoll", "LElbowRoll", "LHipPitch", "RHipPitch", "LKneePitch", "RKneePitch"]
    target_angle = [-0.1, -0.1, 0.0, 0.0, -0.1, -0.1, 0.0, 0.0]
    maxSpeedFraction = 0.4
    job.motionProxy.setAngles(joints, target_angle, maxSpeedFraction)
    time.sleep(2)

    """
    Training loop in which the networks are trained on-line
    """
    learning_rate = 0.01
    integrator = Integrator(learning_rate)

    nr_epochs = 5
    nr_iterations = 10

    limb_speeds = [0.1, 0.1, 0.1, 0.1] #left leg, right leg, left arm, right arm
    limb_speeds_epoch = []
    mobile_movement = 0
    mobile_movement_epoch = []

    for epoch in range(nr_epochs):
        print("Epoch " + str(epoch))
        for iteration in range(nr_iterations):

            if epoch == 0:
                limb_speeds = [random.uniform(0.3, 0.7),
                               random.uniform(0.3, 0.7),
                               random.uniform(0.3, 0.7),
                               random.uniform(0.3, 0.7)]

            if cv2.waitKey(33) == 27:
                vs.unsubscribe()
                myBroker.shutdown()
                break #break the loop

            print("limb_speeds: " + str(limb_speeds))
            movement.moveAll(limb_speeds, epoch)
            mobile_movement = objectSpeed(vs)
            time.sleep(5)

            limb_speeds_epoch.append(limb_speeds)
            mobile_movement_epoch.append(mobile_movement)

        #calculate new speeds with limb_speeds and mobile_movement from previous epoch
        limb_speeds = integrator.limbSpeeds(limb_speeds_epoch, mobile_movement_epoch, epoch)

    """
    End of experiment
    """
    job.postureProxy.goToPosture("LyingBack", 0.7)
    job.motionProxy.rest()

if __name__ == '__main__':
    main()
