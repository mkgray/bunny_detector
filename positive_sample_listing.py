# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 12:19:55 2017

@author: Matthew

This program loads in each positive sample image, adding the image directory
into a list with the specified image size, ASSUMING 1 positive image per sample
ASSUMING the images are pre-cropped to only contain rectangles bounding the
complete positive image

Used to auto-generate the positive sample list for OpenCV cascade training
"""

import argparse
import scipy.ndimage
import os

if __name__ == "__main__":

    argparse = argparse.ArgumentParser()
    argparse.add_argument("source_directory", nargs=1)
    #argparse.add_argument("-i", "--image", required=True, help="path to the input image")
    #argparse.add_argument("-c", "--cascade", default="haarcascade_frontalcatface.xml", help="path to cat detector haar cascade")
    args = argparse.parse_args()
    
    with open(args.source_directory[0] + "/info.dat", 'w') as f:
    
        for file in os.listdir(args.source_directory[0]):
            if file.endswith(".jpg"):
            
                width, height, depth = scipy.ndimage.imread(args.source_directory[0] + '/' + file).shape
            
                f.write(args.source_directory[0] + '/' + file + " 1 0 0 " + str(width) + " " + str(height) + '\n')                               

#    with open(args.source_directory) as f:
#        
#        for line in f:
#            
#            print(line)