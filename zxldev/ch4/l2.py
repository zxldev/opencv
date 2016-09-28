#!/usr/bin/python2
# -*- coding: utf8 -*-
from zxldev.tools.common import *
import cv2

import numpy as np
# from matplotlib import pyplot as plt
"""
##############################################
##                轮廓功能                  ##
##############################################
"""

##############################################
## Moments
##############################################
img = cv2.imread('../src/j.png',0)
imgSrc = img.copy()
ret,thresh = cv2.threshold(img,127,255,0)
# cv2.RETR_EXTERNAL表示只检测外轮廓
# cv2.RETR_LIST检测的轮廓不建立等级关系
# cv2.RETR_CCOMP建立两个等级的轮廓，上面的一层为外边界，里面的一层为内孔的边界信息。如果内孔内还有一个连通物体，这个物体的边界也在顶层。
# cv2.RETR_TREE建立一个等级树结构的轮廓。

# cv2.CHAIN_APPROX_NONE存储所有的轮廓点，相邻的两个点的像素位置差不超过1，即max（abs（x1 - x2），abs（y2 - y1）） == 1
# cv2.CHAIN_APPROX_SIMPLE压缩水平方向，垂直方向，对角线方向的元素，只保留该方向的终点坐标，例如一个矩形轮廓只需4个点来保存轮廓信息
# cv2.CHAIN_APPROX_TC89_L1，CV_CHAIN_APPROX_TC89_KCOS使用teh - Chinlchain近似算法
contours,hierarchy = cv2.findContours(thresh, cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img,contours,-1,(255,255,3),3)
# show_imgs([imgSrc,img])
cnt = contours[0]
M = cv2.moments(cnt)
print M

cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

print (cx,cy)

##############################################
## 轮廓面积
##############################################
area = cv2.contourArea(cnt)
print ('面积：'+str(area))

##############################################
## 轮廓周长
##############################################
perimeter = cv2.arcLength(cnt,True)
print ('周长：'+str(perimeter))

##############################################
## 近似轮廓
##############################################
epsilon = 0.1*cv2.arcLength(cnt,True)
approx = cv2.approxPolyDP(cnt,epsilon,True)
