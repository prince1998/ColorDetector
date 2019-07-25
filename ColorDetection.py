# importing the needed packages
# To run - python3 ColorDetection.py --image imageName

import numpy as np
import cv2
import argparse


# constructing the argument and parsing the arguments
argumentParse = argparse.ArgumentParser()
argumentParse.add_argument("-i", "--image", help = "path to the image")
argument = vars(argumentParse.parse_args())

# reading the image
img = cv2.imread(argument["image"])

# defining the list of boundaries
boundaries = [
	([18, 16, 101], [51, 57, 201]),
	([87, 32, 5], [221, 89, 51]),
	([26, 147, 191], [63, 175, 251]),
	([104, 87, 66], [146, 134, 129])
]


# looping over the boundaries
for (lower, upper) in boundaries:
	# creating NumPy arrays from the boundaries
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")

	# finding the colors within the specified boundaries and apply
	# the mask
	mask = cv2.inRange(img, lower, upper)
	output = cv2.bitwise_and(img, img, mask = mask)

	# displaying the images
	cv2.imshow("images", np.hstack([img, output]))
	cv2.waitKey(0)
