# -*- coding: utf-8 -*-
"""
Created on Wed May 17 11:20:58 2017

@author: WoutervanderWeel
"""

class SensoriMotorSystem:
	"""
	Receives motor commands for each limb and predicts the amount of movement
	Needs to be trained online, to become increasingly accurate during the experiment
	"""
	def __init__(self):