# -*- coding: utf-8 -*-
"""
Created on Wed May 17 11:11:27 2017

@author: WoutervanderWeel
"""
import os

import theano
import lasagne
from theano import tensor as T

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
		correlations  = self.correlation(limb_speeds_epoch, mobile_movement_epoch)

		#Take the idx of the limb that correlates the most
		max_corr_limb = np.argmax[correlations]

		limb_speeds = [0.1, 0.1, 0.1, 0.1]

		#Increase the speed of the limb that correlated most
		limb_speeds[max_corr_limb] = limb_speeds_epoch[max_corr_limb]+correlations[max_corr_limb]*self.learning_rate

		#Decrease the speed of all other limbs
		limb_speeds

		return limb_speeds

	def correlation(self, limb_speeds_epoch, mobile_movement_epoch):
		limb_speeds_left_leg = [item[0] for item in limb_speeds_epoch]
		limb_speeds_right_leg = [item[1] for item in limb_speeds_epoch]
		limb_speeds_left_arm = [item[2] for item in limb_speeds_epoch]
		limb_speeds_right_arm = [item[3] for item in limb_speeds_epoch]
		corr = np.corrcoef([limb_speeds_left_arm, limb_speeds_right_arm,
							limb_speeds_left_leg, limb_speeds_right_leg,
							mobile_movement_epoch])

		return [corr[0,4], corr[1,4], corr[2,4], corr[3,4]]

	# def limbMovements(self, error, mobile_movement, epoch):
	# 	# input tensors for data and targets
	# 	#input_var = T.fmatrix('input')
	# 	#target_var = T.dmatrix('targets')
    #
	# 	# input and output sizes
	# 	#data_size = #size(mobile_movement, error)
	# 	#n_classes = #No_Limbs
    #
	# 	#load previous epoch network or build network
	# 	#if (epoch != 0):
	# 		#load network from previous epoch
	# 		#network = self.readNetwork()
	# 	#else:
	# 		# build a new network
	# 		#network = self.buildNetwork(input_var)#, data_size, n_classes)
    #
	# 	# train the network with new input
	# 	#network = self.trainNetwork(network, error, mobile_movement, input_var, target_var)
    #
	# 	#use the trained network to calculate appropriate limb movements
    #
    #
	# 	#save the network after this epoch
	# 	#params = lasagne.layers.get_all_param_values(network)
	# 	#self.saveNetwork(params)
    #
	# 	return 1
    #
    #
	# def buildNetwork(self, input_var, data_size, n_classes):
	# 	#lasagne tutorial
	# 	#l_in = lasagne.layers.InputLayer(shape=(None, 1, 28, 28),input_var=self.input_var)
    #
	# 	# default paramaters are used now, if we improve on this later on, denseLayer takes an argument W for weight init
	# 	network = lasagne.layers.InputLayer(shape=(None, 1, data_size[1], 1))
	# 	hidden = lasagne.layers.DenseLayer(network, num_units=10, nonlinearity=lasagne.nonlinearities.sigmoid)
	# 	output = lasagne.layers.DenseLayer(hidden, num_units=n_classes, nonlinearity=lasagne.nonlinearities.softmax)
    #
	# 	return output
    #
	# def readNetwork(self):
	# 	#read in the previous network
	# 	network = self.buildNetwork()
    #
	# 	# Load and set stored parameters from file
	# 	npz = np.load('./' + self.network_name + '.npz')
	# 	lasagne.layers.set_all_param_values(network, npz['params'])
    #
	# 	return network
    #
	# def trainNetwork(self, network, input_images, input_var, target_var):
	# 	#train the network for 1 epoch
    #
	# 	# get the prediction during training
	# 	self.prediction = lasagne.layers.get_output(self.network)
    #
	# 	# define the (data) loss
	# 	self.loss = lasagne.objectives.categorical_crossentropy(self.prediction, self.target_var)
	# 	self.loss = self.loss.mean()
    #
    #
    #
	# 	return network
    #
	# def saveNetwork(self, params):
	# 	#save the trained network
	# 	np.savez(
	# 		os.path.join('./', self.network_name + '.npz'),params=params)

