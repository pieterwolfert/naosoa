from connector import RobotConnect
from comparator import Comparator
from visualsystem import VisualSystem
from randommovement import RandomMovement
import cv2
import naoqi
import time


myBroker = None
nr_epochs = 5

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

def objectSpeed(VisualSystem):
    """
    Calculates the speed of the ball. Plots the camera output.
    """
    image = vs.capture_frame()
    image = vs.getBall(image)
    cv2.imshow("Image", image)
    vs.getDifference()


def main():
    """
    Instantiate all needed classes
    """
    job = setParameters()
    vs = VisualSystem(job.videoProxy)
    randomMovement = RandomMovement(job.motionProxy)
    prev_limb_movements = None
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
    epoch = 0
    error = 0
    mobile_movement = 0
    for epoch in range(nr_epochs):
        print("Epoch "+ str(epoch))
        # outputs limb movement speeds
        #limb_speeds = integrator.limbMovements(error, mobile_movement, epoch)

        limb_speeds = [((0.1+1.0*epoch)%10)/10, ((5.1+1.0*epoch)%10)/10, ((2.5+1.0*epoch)%10)/10, ((7.5+1.0*epoch)%10)/10]

        # use limb_movements to move robot limbs
        #connector.move(limb_speeds)
        objectSpeed(vs)
        if cv2.waitKey(33) == 27:
            vs.unsubscribe()
            myBroker.shutdown()
            break #break the while loop

        randomMovement.moveRandomAll(limb_speeds, epoch)
        time.sleep(5)
        #get a number of images to calculate movement in the last few seconds
        #camera_images = connector.getImages() #a stream of images
        #receives the limb movements to predict mobile movement
        #predicted_mobile_movement = sensorimotorsystem.getPrediction(mobile_movement, limb_speeds)
        #compare predicted mobile movement with actual mobile movement
        #error = comparator.error(mobile_movement, predicted_mobile_movement, limb_speeds)
        epoch += 1
    """
    End of experiment
    """
    job.postureProxy.goToPosture("LyingBack", 0.7)
    job.motionProxy.rest()

if __name__ == '__main__':
    main()
