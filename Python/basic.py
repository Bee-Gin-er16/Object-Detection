import cv2 as cv

img = cv.imread('OpenCV/Photos/Jisoo_Cropped.jpg')
# cv.imshow('Jisoo', img)

# GRAYSCALE
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# BLUR
blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# EDGE CASCADE
canny = cv.Canny(img, 125, 175)
# cv.imshow('Canny', canny)

# EDGE CASCADE ON BLUR
cannyb = cv.Canny(blur, 125, 175)
# cv.imshow('Cannyb', cannyb)

# DILATE AN IMAGE
dilated = cv.dilate(canny, (7, 7), iterations=1)
# cv.imshow('Dilated', dilated)

# ERODING
eroded = cv.erode(dilated, (3, 3), iterations=1)
# cv.imshow('Eroded', eroded)

# RESIZE
resized = cv.resize(img, (600, 600), interpolation=cv.INTER_CUBIC)
# cv.imshow('Resized', resized)

# CROPPED
cropped = img[50:200, 200:400]
# cv.imshow('Cropped', cropped)

cv.waitKey(0)
