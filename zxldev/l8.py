#!/usr/bin/python2
# -*- coding: utf8 -*-
from zxldev.tools.common import *
import cv2

import numpy as np


"""
##############################################
##              图像基本操作                 ##
##############################################
"""

##############################################
## 打印所有事件
##############################################
frame = cv2.imread('src/fapiao.jpg')
# Convert BGR to HSV
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

# define range of blue color in HSV
lower_blue = np.array([130, 0, 0])
upper_blue = np.array([200, 255, 255])
lower_blue2 = np.array([0, 60, 60])
upper_blue2 = np.array([10, 255, 255])

# Threshold the HSV image to get only blue colors
mask = cv2.inRange(hsv, lower_blue, upper_blue)
mask2 = cv2.inRange(hsv, lower_blue2, upper_blue2)

# Bitwise-AND mask and original image
res = cv2.bitwise_and(frame, frame, mask=mask2)
show_img(frame)
show_img(mask)
show_img(mask2)
show_img(res)