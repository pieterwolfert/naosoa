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
#get camera images


#vision = VisualSystem(images)



"""
Training loop in which the networks are trained on-line
"""
