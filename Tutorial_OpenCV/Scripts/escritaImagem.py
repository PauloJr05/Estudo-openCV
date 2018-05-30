#!/urs/bin/ env python


from __future__ import print_function

import numpy as np
import cv2 as cv

img = cv.imread('../imagem/01.jpg', 0)

cv.namedWindow('Janela', cv.WINDOW_NORMAL)
cv.imshow('Janela', img)
k = cv.waitKey(0)

if (k == ord('e')):
    cv.destroyAllWindows()

elif (k == ord('s')):
    cv.imwrite('../imagem/01.png', img)
    cv.destroyAllWindows()
