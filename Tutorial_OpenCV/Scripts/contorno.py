#!urs/bin/ env python

import cv2

import numpy as np


cam = cv2.VideoCapture('/dev/video0')
cam.set(3, 420)
cam.set(4, 340)

while(cam.isOpened()):
    _,frame = cam.read()
    im = cv2.GaussianBlur(frame, (5, 5), 0)
    imageGray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    #ret, th = cv2.threshold(imageGray, 127, 255, 0)

    ret, th = cv2.threshold(imageGray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    hierarchy, contours, _ = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame,contours, -1, (0, 255, 0), 3)

    cv2.imshow('frame', frame)
    cv2.imshow('th',th)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyWindow()