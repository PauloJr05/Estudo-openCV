#!urs/bin/ env python

from __future__ import print_function

import numpy as np
import cv2

cap = cv2.VideoCapture('/dev/video0')

while(cap.isOpened()):
    ret,frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    draw = cv2.line(gray, (0,10),(511,511),(512,512,3),8)

    cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
    cv2.imshow('frame', draw)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


        
