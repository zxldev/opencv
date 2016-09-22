#!/usr/bin/python2
# -*- coding: utf8 -*-
from zxldev.tools.common import *
import cv2

import numpy as np
from matplotlib import pyplot as plt
"""
##############################################
##                形态变换                  ##
##############################################
"""


##############################################
## 腐蚀
##############################################
img = cv2.imread('../src/j.png',0)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)

##############################################
## 膨胀
##############################################
dilation = cv2.dilate(img,kernel,iterations = 1)

##############################################
## 等高
##############################################
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

##############################################
## tophat
##############################################
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

##############################################
## blackhat
##############################################
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)


plt.subplot(231),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(232),plt.imshow(erosion),plt.title('erosion')
plt.xticks([]), plt.yticks([])
plt.subplot(233),plt.imshow(dilation),plt.title('dilation')
plt.xticks([]), plt.yticks([])
plt.subplot(234),plt.imshow(gradient),plt.title('gradient')
plt.xticks([]), plt.yticks([])
plt.subplot(235),plt.imshow(tophat),plt.title('tophat')
plt.xticks([]), plt.yticks([])
plt.subplot(236),plt.imshow(blackhat),plt.title('blackhat')
plt.xticks([]), plt.yticks([])
plt.show()

toOpen = cv2.imread('../src/toOpen.png',0)
toClose = cv2.imread('../src/toClose.png',0)

opening = cv2.morphologyEx(toOpen, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(toClose, cv2.MORPH_CLOSE, kernel)

plt.subplot(221),plt.imshow(toOpen),plt.title('toOpen')
plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(opening),plt.title('opening')
plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(toClose),plt.title('toClose')
plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(closing),plt.title('closing')
plt.xticks([]), plt.yticks([])

plt.show()


print (cv2.getStructuringElement(cv2.MORPH_RECT,(9,9)))
print (cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(9,9)))
print (cv2.getStructuringElement(cv2.MORPH_CROSS,(9,9)))