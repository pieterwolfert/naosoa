# -*- coding: utf-8 -*-
"""
Created on Wed May 17 11:11:27 2017

@author: WoutervanderWeel
"""

import numpy as np

class Integrator:
	"""
	Calculates the required motor commands that will make the mobile move more, based on reward for previous movements
	and error in predicted mobile movement. Tries to minimize error, while maximizing mobile movement
	Inputs: (reward for) amount of mobile movement,
			prediction error of the perceived mobile movement
			previous limb movements/motor commands
	Outputs: motor commands (velocity, angles) for the 4 robot limbs
	"""
	def __init__(self, learning_rate):
		#name for the network, to save and load
		#self.network_name = 'integrator'
		self.learning_rate = learning_rate

	def limbSpeeds(self, limb_speeds_epoch, mobile_movement_epoch):
		"""
		Calculate limb speeds based on previous epoch's limb speeds and mobile movement.
		inputs: limb_speeds: array of floats length 4
				mobile_movement: float.
		"""
		#Calculate correlation between each limb and the mobile movement
		correlations, avg_limb_speeds = self.correlation(limb_speeds_epoch, mobile_movement_epoch)
		print correlations
		max_corr_limb = np.argmax[correlations]

		#Increase the speed of the limb that correlated most and decrease the speeds of other limbs
		pos_new = limb_speeds_epoch[max_corr_limb]+abs(correlations[max_corr_limb])*self.learning_rate
		limb_speeds = [pos_new if i is max_corr_limb else x-abs(correlations[i])*self.learning_rate for i, x in enumerate(correlations)]

		return limb_speeds

	def correlation(self, limb_speeds_epoch, mobile_movement_epoch):
		limb_speeds_left_leg = [item[0] for item in limb_speeds_epoch]
		limb_speeds_right_leg = [item[1] for item in limb_speeds_epoch]
		limb_speeds_left_arm = [item[2] for item in limb_speeds_epoch]
		limb_speeds_right_arm = [item[3] for item in limb_speeds_epoch]
		corr = np.corrcoef([limb_speeds_left_arm, limb_speeds_right_arm,
							limb_speeds_left_leg, limb_speeds_right_leg,
							mobile_movement_epoch])

		return [corr[0, 4], corr[1, 4], corr[2, 4], corr[3, 4]], [np.mean(limb_speeds_left_leg),
														   np.mean(limb_speeds_right_leg),
														   np.mean(limb_speeds_left_arm),
														   np.mean(limb_speeds_right_arm)]
