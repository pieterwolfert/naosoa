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

"""
Training loop in which the networks are trained online
"""

while True:

    #get a number of images to calculate movement in the last few seconds
    camera_images = connector.get_images(nr_images) #a stream of images

    #Calculate movement based
    movement = vision.get_movement(camera_images)

    #(rewardcenter calculates a reward for the movement)

    #receives the limb movements to predict mobile movement
    predicted_movement = sensorimotorsystem.getprediction

    #compare predicted mobile movement with actual mobile movement
    error = comparator.calculate_error(movement, predicted_movement)

    #outputs limb movements
    integrator.limb_movements

