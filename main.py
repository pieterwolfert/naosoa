from connector import RobotConnect
from comparator import Comparator
#from integrator import Integrator
#from visualsystem import VisualSystem
#from sensorimotorsystem import SensoriMotorSystem
from randommovement import RandomMovement

import naoqi
import time

"""
Set parameters
"""

ip = '192.168.1.143'
port = 9559
nr_epochs = 10


"""
Create proxies
"""

# Create posture proxy
postureProxy = naoqi.ALProxy("ALRobotPosture", ip, port)
# Create motion proxy
motionProxy = naoqi.ALProxy("ALMotion", ip, port)

"""
Instantiate all needed classes
"""

#Create the robot system parts
connector = RobotConnect(ip)
#vision = VisualSystem()
#sensorimotorsystem = SensoriMotorSystem()
#comparator = Comparator()
#integrator = Integrator()
randomMovement = RandomMovement(motionProxy)

prev_limb_movements = None

"""
Preparations
"""
postureProxy.goToPosture("LyingBack", 0.7)

#Set joints to standard position
joints = ["LShoulderPitch", "RShoulderPitch", "RElbowRoll", "LElbowRoll", "LHipPitch", "RHipPitch", "LKneePitch", "RKneePitch"]
target_angle = [-0.1, -0.1, 0.0, 0.0, -0.1, -0.1, 0.0, 0.0]
maxSpeedFraction = 0.4
motionProxy.setAngles(joints, target_angle, maxSpeedFraction)
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

    randomMovement.moveRandomAll(limb_speeds, epoch)
    time.sleep(5)

    #get a number of images to calculate movement in the last few seconds
    #camera_images = connector.getImages() #a stream of images

    #calculate mobile movement based on the images
    #mobile_movement = vision.getMovement(camera_images)

    #receives the limb movements to predict mobile movement
    #predicted_mobile_movement = sensorimotorsystem.getPrediction(mobile_movement, limb_speeds)

    #compare predicted mobile movement with actual mobile movement
    #error = comparator.error(mobile_movement, predicted_mobile_movement, limb_speeds)

    epoch += 1


"""
End of experiment
"""
postureProxy.goToPosture("LyingBack", 0.7)
motionProxy.rest()