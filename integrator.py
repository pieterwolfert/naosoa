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
		# input tensors for data and targets
		input_var = T.fmatrix('input')
		target_var = T.dmatrix('targets')

	def train(self, input_images,):
		x = 1

	# function to split training set into training and validation subsets
	def split_training_validation_datasets(x, y, n_classes, val_percentage=0.3, val_balanced=True):
		"""
        Derive a training and a validation datasets from a given dataset with
        data (x) and labels (y). By default, the validation set is 30% of the
        training set, and it has balanced samples across classes. When balancing,
        it takes the 30% of the class with less samples as reference.
        """
		multiplier = 1 - val_percentage
		x_train = []
		y_train = []
		x_validation = []
		y_validation = []

		if val_balanced:
			nClasses = max(y) + 1
			lengths = [sum(y == i) for i in range(int(nClasses))]
			print lengths
			minimum = min(lengths)
			print minimum
			print val_percentage
			valSize = int(round(val_percentage * minimum))
			for i in range(int(nClasses)):
				print valSize
				indices = np.argwhere(y == i)
				indices = indices.flatten()
				x_validation.extend(x[indices[:valSize]])
				y_validation.extend(y[indices[:valSize]])
				x_train.extend(x[indices[valSize + 1:]])
				y_train.extend(y[indices[valSize + 1:]])

		else:
			length = int(round(multiplier * len(x)))
			for i in range(len(x)):
				if i <= length:
					x_train.extend(x[i])
					y_train.extend(y[i])
				else:
					x_validation.extend(x[i])
					y_validation.extend(y[i])
		x_validation = np.asarray(x_validation)
		y_validation = np.asarray(y_validation)
		return x_train, y_train, x_validation, y_validation

	def shuffle_training_set:
		# shuffle training dataset
		# EXTREMELY UGLY CODE PLS FIX
		indTrain = range(len(x_train))
		np.random.shuffle(indTrain)
		n_features = np.array(x_train).shape[1]

		xplaceholder = np.zeros((len(x_train), n_features))
		yplaceholder = np.zeros(len(y_train))
		for i in indTrain:
			xplaceholder[i] = x_train[i]
			yplaceholder[i] = y_train[i]
		x_train = np.asarray(xplaceholder)
		y_train = np.asarray(yplaceholder)


