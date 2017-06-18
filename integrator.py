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
	and error in predicted mobile movement
	Inputs: (reward for) amount of mobile movement,
			prediction error of the perceived mobile movement
	Outputs: motor commands (velocity, angles) for the 4 robot limbs
	"""
	def __init__(self, data_size, n_classes, network_name):
		#name for the network, to save and load
		self.network_name = network_name

		#input and output sizes
		self.data_size = data_size
		self.n_classes = n_classes

		# input tensors for data and targets
		self.input_var = T.fmatrix('input')
		self.target_var = T.dmatrix('targets')

		# get the network
		#self.network = self.buildNetwork(self.input_var, self.data_size, self.n_classes)

		# get the prediction during training
		self.prediction = lasagne.layers.get_output(self.network)

		# define the (data) loss
		self.loss = lasagne.objectives.categorical_crossentropy(self.prediction, self.target_var)
		self.loss = self.loss.mean()

	def limb_movements(self, error, movement, epoch):
		#load previous epoch network or build network
		if (epoch != 0):
			#load network from previous epoch
			network = self.readNetwork()
		else:
			# build a new network
			network = self.buildNetwork()

		# train the network with new input
		network = self.trainNetwork(error, movement)

		#use the trained network to calculate appropriate limb movements


		#save the network after this epoch
		params = lasagne.layers.get_all_param_values(network)
		self.saveNetwork(params)


	def buildNetwork(self, input_var, data_size, n_classes):
		#lasagne tutorial
		l_in = lasagne.layers.InputLayer(shape=(None, 1, 28, 28),input_var=self.input_var)

		# default paramaters are used now, if we improve on this later on, denseLayer takes an argument W for weight init
		network = lasagne.layers.InputLayer(shape=(None, 1, data_size[1], 1))
		hidden = lasagne.layers.DenseLayer(network, num_units=10, nonlinearity=lasagne.nonlinearities.sigmoid)
		output = lasagne.layers.DenseLayer(hidden, num_units=n_classes, nonlinearity=lasagne.nonlinearities.softmax)

		return output

	def readNetwork(self):
		#read in the previous network
		network = self.buildNetwork()

		# Load and set stored parameters from file
		npz = np.load('./' + self.network_name + '.npz')
		lasagne.layers.set_all_param_values(network, npz['params'])

		return network

	def trainNetwork(self, input_images):
		#train the network for 1 epoch

		return network

	def saveNetwork(self, network_name, params):
		#save the trained network
		np.savez(
			os.path.join('./', self.network_name + '.npz'),params=params)

