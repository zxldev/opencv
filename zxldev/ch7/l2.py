#!/usr/bin/python2
# -*- coding: utf8 -*-
import cv2
import numpy as np
from zxldev.tools.common import *

##############################################
## 直线检测
##############################################
img = cv2.imread('../src/reciept.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)

lines = cv2.HoughLinesP(edges,1,np.pi/180,200,1000,15)
for x1,y1,x2,y2 in lines[0]:
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

show_img(img)