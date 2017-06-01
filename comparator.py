# -*- coding: utf-8 -*-
"""
Created on Wed May 17 11:20:12 2017

@author: WoutervanderWeel
"""

class Comparator:
	"""
	Calculates the error in predicted mobile movement
	"""
	def __init__(self, actual, predicted):
		self.actual = actual
		self.predicted = predicted

		self.error = self.actual - self.predicted



