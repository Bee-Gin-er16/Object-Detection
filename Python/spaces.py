import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('OpenCV/Photos/Jisoo_Cropped.jpg')
# cv.imshow('Jisoo', img)

# BGR to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to L=a+b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('LAB', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# cv.imshow('RGB', rgb)

# Grayscale to HSV is not possible so, Gray->BGR->HSV
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV->BGR', hsv_bgr)

# plt.imshow(rgb)
# plt.show()

cv.waitKey(0)
