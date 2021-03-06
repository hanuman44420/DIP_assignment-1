# -*- coding: utf-8 -*-
"""DIP_1.ipyn

Automatically generated by Colaboratory.


#code start from here

from google.colab import drive
drive.mount('/content/drive')

import cv2
import numpy as np

img = cv2.imread("/content/drive/MyDrive/myimg.jpg")
print(np.shape(img))
print(type(img[0][0][0]))
#shape (1080, 1080, 3)

gray = np.zeros([1080, 1080], dtype=np.uint8)
for i in range(0,1080):
    for j in range(0, 1080):
        s = 0
        for k in range(0,3):
            s += img[i][j][k]
        gray[i][j] = s/3

cv2.imwrite('myimg.jpg',gray)
from google.colab.patches import cv2_imshow
cv2_imshow(gray)