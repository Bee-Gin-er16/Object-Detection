import cv2 as cv
import numpy as np

img = cv.imread('OpenCV/Photos/Jisoo_Cropped.jpg')
# cv.imshow('Jisoo', img)


# TRANSLATION
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)


# x/-x ---LEFT/RIGHT, y/-y ---UP/DOWN
translated = translate(img, -100, 100)
# cv.imshow('Translated', translated)


# ROTATION
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width // 2, height // 2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)


rotated = rotate(img, 4)
# cv.imshow('Rotated', rotated)

# REVERSE/MIRROR
rotated_rotated = rotate(rotated, -45)
# cv.imshow('Rotated Rotation', rotated_rotated)

# RESIZING
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
# cv.imshow('Resized', resized)

# FLIPPING
flip = cv.flip(img, 0)
# cv.imshow('Flip', flip)

# CROPPING
cropped = img[200:400, 300:400]
# cv.imshow('Cropped', cropped)

cv.waitKey(0)
