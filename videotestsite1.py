# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 17:41:52 2022

@author: thall
"""


# Importing all necessary libraries
import cv2
import os

# Read the video from specified path
#cam = cv2.VideoCapture("C:\\vidoetestdt\\testvideo.mp4")
cam = cv2.VideoCapture("C:\\vidoetestdt\\1009FF65-359F-4D06-9AD5-D8FF36E681A3.mov")

try:
	
	# creating a folder named data
	if not os.path.exists('data3'):
		os.makedirs('data3')

# if not created then raise error
except OSError:
	print ('Error: Creating directory of data3')

# frame
currentframe = 0

while(True):
	
	# reading from frame
	ret,frame = cam.read()

	if ret:
		# if video is still left continue creating images
		name = './data3/frame' + str(currentframe) + '.jpg'
		print ('Creating...' + name)

		# writing the extracted images
		cv2.imwrite(name, frame)

		# increasing counter so that it will
		# show how many frames are created
		currentframe += 1
	else:
		break

# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()


