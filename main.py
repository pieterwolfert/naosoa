from connector import RobotConnect
from comparator import Comparator
from integrator import Integrator
from visualsystem import VisualSystem
from sensorimotorsystem import SensoriMotorSystem


"""
Set parameters
"""

ip = '168.192.1.143'
nr_epochs = 1
nr_images = 5

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
Training loop in which the networks are trained online
"""
epoch = 0
while True:

    #get a number of images to calculate movement in the last few seconds
    camera_images = connector.get_images(nr_images) #a stream of images

    #Calculate movement based
    detected_movement = vision.get_movement(camera_images)

    #receives the limb movements to predict mobile movement
    predicted_movement = sensorimotorsystem.prediction(prev_limb_movements)

    #compare predicted mobile movement with actual mobile movement
    error = comparator.error(detected_movement, predicted_movement)

    #outputs limb movements
    limb_movements = integrator.limb_movements(error, detected_movement, epoch)

    #use limb_movements to move robot limbs
    #connector.move(limb_movements)

    #remember limb movements for use in sensorimotorsystem
    #prev_limb_movements = limb_movements
    epoch += 1
