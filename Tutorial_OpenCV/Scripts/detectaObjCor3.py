#!urs/bin env python

from __future__ import print_function
import cv2
import numpy as np



def detec():
    cam = cv2.VideoCapture('/dev/video0')
    while(True):

        _,frame = cam.read()

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #range RED
        redRangemin = np.array([136,87,111],np.uint8)
        redRangemax = np.array([180,255,255],np.uint8)

        # range BLUE
        blueRangemin = np.array([99,115,150],np.uint8)
        blueRangemax = np.array([110,255,255],np.uint8)

        # range YELLOW
        yellowRangemin = np.array([22,60,200],np.uint8)
        yellowRangemax = np.array([60,255,255],np.uint8)
        #mascaras

        redMask = cv2.inRange(hsv,redRangemin,redRangemax)
        blueMask = cv2.inRange(hsv,blueRangemin,blueRangemax)
        yellowMask = cv2.inRange(hsv,yellowRangemin,yellowRangemax)

        #filtro
        kernal = np.ones((5,5),"uint8")

        redMask = cv2.dilate(redMask,kernal)
        redRes = cv2.bitwise_and(frame, frame, mask=redMask)

        blueMask = cv2.dilate(blueMask,kernal)
        blueRes = cv2.bitwise_and(frame, frame, mask=blueMask)

        yellowMask = cv2.dilate(yellowMask,kernal)
        yellowRes = cv2.bitwise_and(frame, frame, mask=yellowMask)

        (_,contours,_) = cv2.findContours(redMask,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
        for i, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if (area > 300):
                x,y,w,h = cv2.boundingRect(contour)
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
                cv2.putText(frame,"RED",(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255)) 

        (_,contours,_) = cv2.findContours(blueMask,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
        for i, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if (area > 300):
                x,y,w,h = cv2.boundingRect(contour)
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
                cv2.putText(frame,"BLUE",(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,0,0))

        (_,contours,_) = cv2.findContours(yellowMask,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
        for i, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if (area > 300):
                x,y,w,h = cv2.boundingRect(contour)
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                cv2.putText(frame,"YELLOW",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1.0,(0,255,0))
    
        cv2.namedWindow('camera',cv2.WINDOW_NORMAL)
        cv2.imshow('camera',frame)
        
        if cv2.waitKey(10) & 0xFF == ord('q'):
            cam.release()
            cv2.destroyAllWindows()
            break
def main():
    detec()

if __name__ == '__main__':
    main()