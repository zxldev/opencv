#!/usr/bin/python2
# -*- coding: utf8 -*-
import imutils
from zxldev.tools.common import *

"""
##############################################
##               图像算法                    ##
##############################################
"""

##############################################
## 图像合并
##############################################
img1 = cv2.imread('src/RGB.jpg')
img2 = cv2.imread('src/RGB2.jpg')
show_img(img1+img2)
show_img(cv2.add(img1,img2))
dst = cv2.addWeighted(img1 , 0.7,img2,0.3,0)
show_img(dst)

