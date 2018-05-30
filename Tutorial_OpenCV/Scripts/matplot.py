#!/urs/bin/ env python

from __future__ import print_function

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('../imagem/01.jpg', 0)

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])
plt.show()
