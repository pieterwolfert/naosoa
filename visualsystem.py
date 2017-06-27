# -*- coding: utf-8 -*-
"""
@author: WoutervanderWeel
@author: Pieter Wolfert
"""
import cv2
import math
import numpy as np
import naoqi
import time
from scipy.spatial import distance
import matplotlib.pyplot as plt
from IPython import embed

class VisualSystem:
    """Visualsystem processing video in- and output."""
    def __init__(self, videoProxy):
        """Initialize the visualsystem.

        Keyword arguments:
        videoProxy -- containing a naoqi ALProxy object for video
        """
        self.videoProxy = videoProxy
        self.cam_name = "camera"
        self.cam_type = 0
        self.resolution = 0
        self.colorspace = 13
        self.fps = 30
        self.circlePrev = False
        self.prevCircleX = 0
        self.Xcenter = 0
        self.Ycenter = 0
        self.Xcenter_old = 0
        self.Ycenter_old = 0

    def unsubscribe(self):
        """Unsubscribe the videoProxy"""
        self.videoProxy.unsubscribe(self.cam_name)

    def capture_frame(self):
        """
        Captures frame (image).
        """
        try:
            self.videoProxy.unsubscribeCamera(self.cam_name, self.cam_type,\
                             self.resolution, self.colorspace, self.fps)
        except:
            pass
        camera = self.videoProxy.subscribeCamera(self.cam_name,\
                 self.cam_type, self.resolution, self.colorspace, self.fps)
        image_container = self.videoProxy.getImageRemote(camera)
        width = image_container[0]
        height = image_container[1]
        image = np.zeros((width, height, 3), np.uint8)
        values = map(ord, list(image_container[6]))
        i=0
        image = np.array(values, np.uint8).reshape((height, width, 3))
        self.videoProxy.unsubscribe(camera)
        return image

    def updateCenter(self, x, y):
        """Sets new center coordinates derived from image.

        Keyword arguments:
        x -- x coordinate(float)
        y -- y coordinate(float)
        """
        self.Xcenter_old = self.Xcenter
        self.Ycenter_old = self.Ycenter
        self.Xcenter = x
        self.Ycenter = y

    def getDifference(self):
        """Calculates euclidean distance between two centers. """
        return istance.euclidean((self.Xcenter_old, self.Ycenter_old),\
                                 (self.Xcenter, self.Ycenter))

    def getBall(self, image):
        """Detects the blue ball in a given image.

        Keyword arguments:
        image -- image in cv2 format
        """
    	lower_blue = np.array([70, 50, 50], dtype = np.uint8)
    	upper_blue = np.array([170, 255, 255], dtype = np.uint8)
    	hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    	color_mask = cv2.inRange(hsv_image, lower_blue, upper_blue)
    	kernel = np.ones((9,9), np.uint8)
    	opening = cv2.morphologyEx(color_mask, cv2.MORPH_OPEN, kernel)
    	closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
    	smoothed_mask = cv2.GaussianBlur(closing, (9,9), 0)
    	blue_image = cv2.bitwise_and(image, image, mask = smoothed_mask)
    	gray_image = blue_image[:, :, 2]
    	circles = cv2.HoughCircles(gray_image, 3 , 1, 1, param1 = 200,\
                                   param2=20, minRadius=5, maxRadius=100)
        if circles is not None:
            circle = circles[0, :][0]
            self.updateCenter(circle[0], circle[1])
            cv2.circle(image, (circle[0], circle[1]), circle[2], (0, 255, 0), 2)
            if self.circlePrev == False:
                print "don't see a thing"
            self.circlePrev = True
            self.prevCircleX = circle[0]
            return image
        return image

if __name__ == "__main__":
    """Main(ly) for testing purposes"""
    capture_frame()
    imload()
