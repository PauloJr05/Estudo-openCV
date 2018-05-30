#!/urs/bin/env python

from __future__ import print_function

import numpy as np
import cv2 as cv

img = cv.imread('../imagem/01.jpg',0) #Faz a leitura de uma imagem

cv.namedWindow('Imagem1',cv.WINDOW_NORMAL) #Especifica se a janela 
cv.imshow('Imagem1', img) #abri uma janela
cv.waitKey(0) #funcao que ativa o teclado
cv.destroyAllWindows() #fecha a janela
