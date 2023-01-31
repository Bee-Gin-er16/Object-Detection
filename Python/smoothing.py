import cv2 as cv
import numpy as np
# TODO STOPPED @1:44:28

img = cv.imread('OpenCV/Photos/Jisoo_Cropped.jpg')
# cv.imshow('Jisoo', img)

# BLUR
average = cv.blur(img, (2, 3))
cv.imshow('Ave Blur', average)

# GAUSS BLUR
gauss = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow('Gaussian Blur', gauss)

# MEDIAN BLUR
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# BILATERAL BLUR
bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)
