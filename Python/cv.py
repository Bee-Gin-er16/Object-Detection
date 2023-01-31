from turtle import width
import cv2 as cv
# Tutorial Link: 
# https://www.youtube.com/watch?v=oXlwWbU8l2o&ab_channel=freeCodeCamp.org
# STOPPED @ 20:25 on 11-Apr 2022

# FUNCTIONS
def rescaleFrame(frame, scale=0.75):
    #images, videos, live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    # live video only
    capture.set(3,width)
    capture.set(4,height)


# READING IMAGES
# --------------------------------------------------------------------->
# since code originates from softdev => python folder, 
# default start is where code is stored
# img = cv.imread('OpenCV/Photos/Jisoo_Cropped.jpg') 
# cv.imshow('Jisoo', img)

# resized_image = rescaleFrame(img)
# cv.imshow('Image', resized_image)
# --------------------------------------------------------------------->


# READING VIDEOS
# --------------------------------------------------------------------->
capture = cv.VideoCapture('OpenCV/Videos/Yve_exercise.mp4')

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, scale=.5)
    # cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
# --------------------------------------------------------------------->

#This statement will wait for a key to be pressed and will end any read/write of img or videos
cv.waitKey(0)

