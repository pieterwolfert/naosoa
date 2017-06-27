# -*- coding: utf-8 -*-
"""
@author: WoutervanderWeel
@author: Pieter Wolfert
"""

class Comparator:
	"""Comparing predicted and actual values."""
	def __init__(self, name):
		"""Init comparator object."""
		self.name = name

	def calculate_error(self, actual, predicted):
		"""Returns the error based on difference actual - predicted.

		Keyword arguments:
		actual -- actual value of movement speed
		predicted -- predicted value for movement speed.
		"""
		return actual - predicted
