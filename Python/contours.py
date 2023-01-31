import cv2 as cv
import numpy as np
# TODO CONFUSION AT 1:02:25

img = cv.imread('OpenCV/Photos/Jisoo_Cropped.jpg')
cv.imshow('Jisoo', img)

blank = np.zeros(img.shape, dtype='uint8')
# cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

canny = cv.Canny(img, 125, 175)
# cv.imshow('Canny', canny)

# THRESHOLDING
# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow('thresh', thresh)

# CONTOURS
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found')

# DRAW CONTOURS
cv.drawContours(blank, contours, -1, (216, 162, 171), 1)
cv.imshow('Contours Drawn w/select color', blank)

cv.waitKey(0)
