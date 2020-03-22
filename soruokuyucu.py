
#sadece resim okur
import numpy as np
import argparse
import pytesseract
import cv2
import os
from PIL import Image
"""
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image to be OCR'd")
ap.add_argument("-p", "--preprocess", type=str, default="thresh", help="type of preprocessing to be done")
args = vars(ap.parse_args())
"""

#resmin konumu
image_location = "/home/ege/Desktop/12600.png"
image = cv2.imread(image_location)


boundaries = [
	([175, 175, 175], [255, 255, 255])
]


	
for (lower, upper) in boundaries:
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")
 
	# find the colors within the specified boundaries and apply
	# the mask
	mask = cv2.inRange(image, lower, upper)
	output = cv2.bitwise_and(image, image, mask = mask)
 	

	filename = "{}.png".format(os.getpid())
	cv2.imwrite(filename, output)
	text = pytesseract.image_to_data(Image.open(filename), lang = "tur") 
	os.remove(filename)
	print(text)
	cv2.imshow("images", np.hstack([image, output]))
	cv2.waitKey(0)

