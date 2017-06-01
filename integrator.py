# -*- coding: utf-8 -*-
"""
Created on Wed May 17 11:11:27 2017

@author: WoutervanderWeel
"""

class Integrator:
	"""
	Calculates the required motor commands that will make the mobile move more, based on reward for previous movements 
	and error in predicted mobile movement
	Inputs: (reward for) amount of mobile movement,
			prediction error of the perceived mobile movement
	Outputs: motor commands (velocity, angles) for the 4 robot limbs
	"""
	def __init__(self):
		#stuff