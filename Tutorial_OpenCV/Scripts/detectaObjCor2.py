#!urs/bin env python

from __future__ import print_function
import cv2
import numpy as np

def detec():
    img = cv2.VideoCapture('/dev/video0')
    kernel = np.ones((5,5),np.uint8)

    while(True):
        _, frame = img.read()

        blueRangemin = np.array([110,50,50])
        blueRangemax = np.array([130,255,255])
        blueMask = cv2.inRange(frame,blueRangemin,blueRangemax)

        opening = cv2.morphologyEx(blueMask,cv2.MORPH_OPEN,kernel)
        x,y,w,h = cv2.boundingRect(opening)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
        cv2.circle(frame,(x+w/2,y+h/2),5,(0,0,255),-1)
        cv2.namedWindow('camera',cv2.WINDOW_NORMAL)
        cv2.imshow('camera',frame)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
def main():
    detec()

if __name__ == '__main__':
    main()


