from connector import RobotConnect
from comparator import Comparator
from integrator import Integrator
from visualsystem import VisualSystem
from sensorimotorsystem import SensoriMotorSystem

ip =

"""
Instantiate all needed classes
"""

#Instantiate a robot
connector = RobotConnect(ip)
camera_images = connector.get_images #a stream of images







"""
Training loop in which the networks are trained on-line
"""

#for number_of_iterations

#(maybe use n=5 images (a batch) to calculate movement)
vision = VisualSystem()
movement = vision.get_movement(camera_images)

#(rewardcenter calculates a reward for the movement)

#receives the limb movements to predict mobile movement
sensorimotorsystem = SensoriMotorSystem
predicted_movement = sensorimotorsystem.getprediction

#compare predicted mobile movement with actual mobile movement
comparator = Comparator(movement, predicted_movement)
error = comparator.error

#outputs limb movements
integrator = Integrator()
integrator.limb_movements

