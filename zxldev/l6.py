#!/usr/bin/python2
# -*- coding: utf8 -*-
import cv2
import numpy as np
from zxldev.tools.common import *

"""
##############################################
##              图像基本操作                 ##
##############################################
"""

##############################################
## 图像像素操作1
##【使用“[]”直接访问某点操作非常耗时， 尽量不要使用】
##############################################
img = cv2.imread('src/RGB.jpg')
#获取某点的BGR颜色
px = img[100,100]
print  px
#获取某点的蓝色值
blue = img[100,100,0]
print  blue
#给图像某点直接赋值[运行较慢，暂时注释]
for i,row in enumerate(img):
    for j,pix in enumerate(row):
        if i % 100 == 0  or j % 50== 0:
            img[i][j] = [255,255,255]
show_img(img)

##############################################
## 图像像素操作2
##############################################
#获取某点的蓝色值
print img.item(100,100,0)
#给图像某点直接赋值
img.itemset((100,100,0),0)

##############################################
## 图像属性
##############################################
#图像形状，返回 高、宽、通道数量
print img.shape
#图像像素数量
print img.size
#图像dtype
print img.dtype

