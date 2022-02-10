# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 23:54:05 2022

"""

import cv2
 
src = cv2.imread('grace_1.png', cv2.IMREAD_UNCHANGED)

#percent by which the image is resized
scale_percent = 50

#calculate the 50 percent of original dimensions
width = int(src.shape[1] * scale_percent / 100)
height = int(src.shape[0] * scale_percent / 100)

# dsize
dsize = (width, height)

# resize image
output = cv2.resize(src, dsize)

cv2.imwrite('image-50.png',output) 