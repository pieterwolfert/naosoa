from connector import RobotConnect
from comparator import Comparator
from integrator import Integrator
from visualsystem import VisualSystem
from sensorimotorsystem import SensoriMotorSystem
from randommovement import RandomMovement

import naoqi

"""
Set parameters
"""

ip = '168.192.1.143'
port = '9559'
nr_epochs = 10
nr_images = 5

"""
Create proxies
"""

motionProxy = naoqi.ALProxy("ALMotion", ip , port)

"""
Instantiate all needed classes
"""

#Create the robot system parts
connector = RobotConnect(ip)
vision = VisualSystem()
sensorimotorsystem = SensoriMotorSystem()
comparator = Comparator()
integrator = Integrator()

prev_limb_movements = None

"""
Training loop in which the networks are trained on-line
"""
epoch = 0
error = 0
mobile_movement = 0



while True:
    # outputs limb movements
    limb_movements = integrator.limbMovements(error, mobile_movement, epoch)

    # use limb_movements to move robot limbs
    connector.move(limb_movements)

    #get a number of images to calculate movement in the last few seconds
    camera_images = connector.getImages(nr_images) #a stream of images

    #calculate mobile movement based on the images
    mobile_movement = vision.getMovement(camera_images)

    #receives the limb movements to predict mobile movement
    predicted_mobile_movement = sensorimotorsystem.getPrediction(mobile_movement, limb_movements)

    #compare predicted mobile movement with actual mobile movement
    error = comparator.error(mobile_movement, predicted_mobile_movement, limb_movements)

    epoch += 1
