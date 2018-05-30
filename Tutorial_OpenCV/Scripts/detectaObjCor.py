#!urs/bin/ env python

from __future__ import print_function
import cv2
import numpy as np 


def detec():
    im = cv2.VideoCapture('/dev/video0')
    kernel = np.ones((5,5),np.uint8)
    #kernel = np.ones((5,5),np.float32)/25
    while(1):
        _, frame = im.read()
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_blue = np.array([110,50,50])
        upper_blue = np.array([130,255,255])
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        opening = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        #frame = cv2.dilate(frame,kernel)
        #frame = cv2.filter2D(frame,-1,kernel)
        #frame = cv2.bilateralFilter(frame,9,75,75)
        res = cv2.bitwise_and(opening, opening,mask=mask)

        cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
        cv2.imshow('frame',frame)
        #cv2.imshow('mask',mask)
        cv2.namedWindow('res',cv2.WINDOW_NORMAL)
        cv2.imshow('res',res)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            im.release()
            cv2.destroyAllWindows()
            break

cv2.destroyAllWindows()

def main():
    detec()
    

if __name__ == '__main__':
    main()
