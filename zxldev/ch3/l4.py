#!/usr/bin/python2
# -*- coding: utf8 -*-
from zxldev.tools.common import *
from matplotlib import pyplot as plt
import cv2

import numpy as np

"""
##############################################
##                柔化模糊                  ##
##############################################
"""


##############################################
## Convolution 2d过滤
##############################################
img = cv2.imread('../src/opencv_logo.png')
kernel = np.ones((5,5),np.float32)/25
blurAveraging = cv2.filter2D(img,-1,kernel)

##############################################
## 平均模糊
##############################################
blurBlurred = cv2.blur(img,(5,5))

##############################################
## 高斯模糊
##############################################
blurGaussian = cv2.GaussianBlur(img,(5,5),0)

plt.subplot(221),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(blurAveraging),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(blurBlurred),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(blurGaussian),plt.title('Gaussian')
plt.xticks([]), plt.yticks([])
plt.show()

##############################################
## 中值滤波器
##############################################
img = cv2.imread('../src/RGB.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
blurMedian = cv2.medianBlur(img,9)

##############################################
## 双侧滤波器
##############################################
blurBilateral = cv2.bilateralFilter(img,9,75,75)

plt.subplot(221),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(blurMedian),plt.title('Median')
plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(blurBilateral),plt.title('Bilateral')
plt.xticks([]), plt.yticks([])
plt.show()