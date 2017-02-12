# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 08:47:45 2017

@author: Matthew
"""

# Import packages
import argparse
import cv2

argparse = argparse.ArgumentParser()
argparse.add_argument("-i", "--image", required=True, help="path to the input image")
argparse.add_argument("-c", "--cascade", default="haarcascade_frontalcatface.xml", help="path to cat detector haar cascade")
args = vars(argparse.parse_args())

# Load the image and convert to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Load the cat detector Haar cascade, then detect cat faces
# in the input image
detector = cv2.CascadeClassifier(args["cascade"])
rects = detector.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=10, minSize=(75,75))

# Loop over the cat faces and draw a rectangle surrounding each
for (i, (x, y, w, h)) in enumerate(rects):
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.putText(image, "Cat #{}".format(i+1), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)
    
# Show the detected cat faces
cv2.imshow("Cat Faces", image)
cv2.waitKey(0)

