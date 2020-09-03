# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 18:45:08 2020

@author: Neeraj
"""

import cv2
import numpy as np

num_down=2
num_bilateral=50

img_rgb=cv2.imread("stunning-latest-pics-of-Kajal-Agarwal.jpg")    #image path
img_rgb=cv2.resize(img_rgb,(800,800))

img_color=img_rgb

for _ in range(num_down):
    img_color=cv2.pyrDown(img_color)
    
for _ in range(num_bilateral):
    img_color=cv2.bilateralFilter(img_color,d=9,
                                  sigmaColor=9,
                                  sigmaSpace=7)


for _ in range(num_down):
    img_color=cv2.pyrUp(img_color)
    
img_gray=cv2.cvtColor(img_rgb,cv2.COLOR_RGB2GRAY)
img_blur=cv2.medianBlur(img_gray,7)

img_edge=cv2.adaptiveThreshold(img_blur,255,
                               cv2.ADAPTIVE_THRESH_MEAN_C,
                               cv2.THRESH_BINARY,
                               blockSize=9,
                               C=2)
img_edge=cv2.cvtColor(img_edge,cv2.COLOR_GRAY2RGB)
img_sketch=cv2.bitwise_and(img_color,img_edge)

#displaying the actual and sketched images

stack=np.hstack([img_rgb,img_sketch])
# cv2.imshow("stacked",stack)
# cv2.waitKey(0)

cv2.imwrite("cartoon1.jpg",stack)      #to save the image
