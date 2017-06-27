# -*- coding: utf-8 -*-
"""
@author: WoutervanderWeel
@author: Pieter Wolfert
"""
import os
import numpy as np


class SensoriMotorSystem:
    """	Receives motor commands for each limb and
    predicts the amount of mobile movement
    Needs to be trained online, to become increasingly
    accurate during the experiment.
    """
    def __init__(self):
        """
        Class for sensorimotorsystem.
        """
        self.network_name = 'sensorimotorsystem'

    def getPrediction(self, mobile_movement, limb_movements):
        """
        Makes prediction based on mobile and limb movement.

        Keyword arguments:
        mobile_movement -- speed of ball attached to the mobile
        limb_movements -- speeds of limb movement
        """
        if np.argmax(limb_movevements) > 0.5:
            return 80
        elif np.argmax(limb_movements) < 0.5:
            return 20
