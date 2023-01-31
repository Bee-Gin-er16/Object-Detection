import cv2 as cv
from cv2 import rectangle
import numpy as np

# Tutorial Link:
# https://www.youtube.com/watch?v=oXlwWbU8l2o&ab_channel=freeCodeCamp.org
# STOPPED @ 31:54 on 14-Apr 2022

# THIS WILL MAKE YOUR SCREEN BLACK
blank = np.zeros((500, 500, 3), dtype='uint8')
# cv.imshow('Blank', blank)  # One instance of the image in window

# 1 Paint image a certain image
# ----------------------------------------------------->
# blank[200:300, 300:400] = 0,0,255
# cv.imshow('Green', blank)

# 2 Draw rectangle
# ----------------------------------------------------->
# cv.rectangle(blank, (0, 0), (blank.shape[1] // 2, blank.shape[0] // 2),
#              (0, 255, 0), thickness=-1)
# cv.imshow('Green', blank)

# # Draw a circle
# ----------------------------------------------------->
# cv.circle(blank, (blank.shape[1] // 2, blank.shape[0] // 2), 40,
#           (0, 0, 255), thickness=3)
# cv.imshow('Green', blank)

# Draw a line
# ----------------------------------------------------->
# cv.line(blank, (100, 250), (300, 400),
# (255,255,255), thickness=3)
# cv.imshow('Line', blank)

# Write test
# ----------------------------------------------------->
cv.putText(blank, 'Hello my name is Hans', (0, 225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2)
cv.imshow('Text', blank)

cv.waitKey(0)
