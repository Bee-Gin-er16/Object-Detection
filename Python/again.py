from turtle import width
import cv2 as cv
from outcome import capture

# The ui of the vid/photo will change using this function
# non-live video, use this to change resolution
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# live video, use this to change resolution
def changeRes(width,height):
    capture.set(3, width)
    capture.set(4, height)

# Reading image
# <-------------------------------->
img=cv.imread('OpenCV\Photos\Jisoo_Cropped.jpg')
cv.imshow('Jisoo' ,img)
resized_image = rescaleFrame(img)
cv.imshow('Image',resized_image)
# <-------------------------------->

# Reading Videos by frames
# <-------------------------------->
# capture = cv.VideoCapture(0) 
# 0 willl open your webcam, 1-n is the external camera

capture = cv.VideoCapture('OpenCV\Videos\Yve_exercise.mp4')

while True:
    isTrue, frame = capture.read()

    # Using the resize fxn
    # frame_resized = rescaleFrame(frame, scale=.2)
    # cv.imshow('Video Resized', frame_resized)
    # cv.imshow('Video' ,frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
# <-------------------------------->