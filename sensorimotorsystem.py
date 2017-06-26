# -*- coding: utf-8 -*-
"""
Created on Wed May 17 11:20:58 2017

@author: WoutervanderWeel
"""
import os

import theano
import lasagne
from theano import tensor as T

import numpy as np


class SensoriMotorSystem:
	"""
	Receives motor commands for each limb and predicts the amount of mobile movement
	Needs to be trained online, to become increasingly accurate during the experiment
	"""
	def __init__(self):
		self.network_name = 'sensorimotorsystem'

	def getPrediction(self, mobile_movement, limb_movements):
		#get a prediction for the amount of mobile movement with these limb movements.

		# input tensors for data and targets
		input_var = T.fmatrix('input')
		target_var = T.dmatrix('targets')

		# input and output sizes
		data_size =  # size(mobile_movement, error)
		n_classes =  # No_Limbs

		# load previous epoch network or build network
		if (epoch != 0):
			# load network from previous epoch
			network = self.readNetwork()
		else:
			# build a new network
			network = self.buildNetwork(input_var, data_size, n_classes)

		# Create theano functions


		# train the network with new input
		network = self.trainNetwork(network, error, mobile_movement, input_var, target_var)

		# use the trained network to calculate appropriate limb movements


		# save the network after this epoch
		params = lasagne.layers.get_all_param_values(network)
		self.saveNetwork(params)

	def buildNetwork(self, input_var, data_size, n_classes):
		# lasagne tutorial
		# l_in = lasagne.layers.InputLayer(shape=(None, 1, 28, 28),input_var=self.input_var)

		# default paramaters are used now, if we improve on this later on, denseLayer takes an argument W for weight init
		network = lasagne.layers.InputLayer(shape=(None, 1, data_size[1], 1))
		hidden = lasagne.layers.DenseLayer(network, num_units=10, nonlinearity=lasagne.nonlinearities.sigmoid)
		output = lasagne.layers.DenseLayer(hidden, num_units=n_classes, nonlinearity=lasagne.nonlinearities.softmax)

		return output

	def readNetwork(self):
		# read in the previous network
		network = self.buildNetwork()

		# Load and set stored parameters from file
		npz = np.load('./' + self.network_name + '.npz')
		lasagne.layers.set_all_param_values(network, npz['params'])

		return network

	def trainNetwork(self, network, input_images, input_var, target_var):
		# train the network for 1 epoch

		# get the prediction during training
		self.prediction = lasagne.layers.get_output(self.network)

		# define the (data) loss
		self.loss = lasagne.objectives.categorical_crossentropy(self.prediction, self.target_var)
		self.loss = self.loss.mean()

		return network

	def saveNetwork(self, params):
		# save the trained network
		np.savez(
			os.path.join('./', self.network_name + '.npz'), params=params)