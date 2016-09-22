#!/usr/bin/python2
# -*- coding: utf8 -*-
from zxldev.tools.common import *
import cv2

import numpy as np

"""
##############################################
##               图片几何变换               ##
##############################################
"""


##############################################
## 缩放
##############################################
img = cv2.imread('../src/RGB.jpg',0)
imgScale = cv2.resize(img,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_CUBIC)
show_img(img,flags=cv2.WINDOW_AUTOSIZE)
show_img(imgScale,flags=cv2.WINDOW_AUTOSIZE)
#OR
height, width = img.shape[:2]
imgScale = cv2.resize(img,(int(0.2*width), int(0.2*height)), interpolation = cv2.INTER_CUBIC)
show_img(imgScale,flags=cv2.WINDOW_AUTOSIZE)

##############################################
## 平移
##############################################
img = cv2.imread('../src/RGB.jpg',0)
rows,cols = img.shape

M = np.float32([[1,0,300],[0,1,100]])
dst = cv2.warpAffine(img,M,(cols*2,rows*2))
show_img(dst)

##############################################
## 旋转
##############################################
img = cv2.imread('../src/RGB.jpg',0)
rows,cols = img.shape

M = cv2.getRotationMatrix2D((cols/2,rows/2),60,1)
dst = cv2.warpAffine(img,M,(cols,rows))
show_img(dst)

##############################################
## 仿射变换
##############################################
img = cv2.imread('../src/RGB.jpg')
rows,cols,ch = img.shape

pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])

M = cv2.getAffineTransform(pts1,pts2)

dst = cv2.warpAffine(img,M,(cols,rows))

show_img(img)
show_img(dst)
