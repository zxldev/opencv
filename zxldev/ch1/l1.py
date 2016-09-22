#!/usr/bin/python2
# -*- coding: utf8 -*-
import cv2
from zxldev.tools.common import show_img

"""
##############################################
##              图像读写展示                  ##
##############################################
"""

##############################################
## 读取图像
##############################################

# cv2.IMREAD_ANYCOLOR
# cv2.IMREAD_ANYDEPTH
# cv2.IMREAD_COLOR 正常彩色图片
# cv2.IMREAD_GRAYSCALE 灰白模式
# cv2.IMREAD_UNCHANGED alpha通道模式
img = cv2.imread('../src/RGB.jpg')



##############################################
## 显示图像
##############################################

show_img(img,usematplotlib=False)

##############################################
## 写入图像
##############################################
# img = img[..., ::-1]
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

