# -*- coding: utf-8 -*-
"""
Created on Wed May 17 11:06:37 2017

@author: Pieter Wolfert
"""

import cv2
import numpy as np
import naoqi
import time
import matplotlib.pyplot as plt

class VisualSystem:
    """
    Calculates the amount of movement, given the images of the robot camera
    """
    def __init__(self, videoProxy):
        self.videoProxy = videoProxy

    def movement(self, images):
        print "hello world"

    def getMovement(self, frame1, frame2):
        """
        Calculates movement given two frames.
        TODO Movement calculation. Can be done using center detection.
        Returns derivative of the two centers of object in image.
        """
        movement = 0.0
        return movement

    def detectCenter(self, frame):
        """
        Detect center of red tracker square.
        """
        x = 0.0
        y = 0.0
        return x,y

    def capture_frame(self):
        """
        Captures frame (image).
        """
        cam_name = "camera"
        cam_type = 0
        resolution = 0
        colorspace = 13
        fps = 10
        try:
            self.videoProxy.unsubscribeCamera(cam_name, cam_type, resolution, colorspace, fps)
        except:
            pass
        camera = self.videoProxy.subscribeCamera(cam_name, cam_type, resolution, colorspace, fps)
        image_container = self.videoProxy.getImageRemote(camera)
        width = image_container[0]
        height = image_container[1]
        image = np.zeros((width, height, 3), np.uint8)
        values = map(ord, list(image_container[6]))
        i=0
        image = np.array(values, np.uint8).reshape((height, width, 3))
        t4 = time.time()
        self.videoProxy.unsubscribe(camera)
        plt.imshow(image)
        plt.show()

    def getCVversion(self):
        print "cv version" + cv2.__version__

    def loadImage(self):
        """
        Loading image which was captured. Needs some finetuning to detect red blob.
        """
        image = cv2.imread("firstimage.png")
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
    	circles = cv2.HoughCircles(gray_image, 3 , 1, 1, param1 = 200, param2=20, minRadius=5, maxRadius=100)
    	circle = circles[0, :][0]
    	cv2.circle(image, (circle[0], circle[1]), circle[2], (0, 255, 0), 2)
    	circle = circles[0, :][1]
    	cv2.circle(image, (circle[0], circle[1]), circle[2], (0, 255, 0), 2)
    	embed()
    	cv2.imshow("Main", image)
    	cv2.waitKey()


if __name__ == "__main__":
	capture_frame()
	imload()
