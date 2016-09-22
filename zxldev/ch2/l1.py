#!/usr/bin/python2
# -*- coding: utf8 -*-
import cv2
import numpy as np
from zxldev.tools.common import *
from matplotlib import pyplot as plt
"""
##############################################
##              图像基本操作                 ##
##############################################
"""

##############################################
## 图像像素操作1
##【使用“[]”直接访问某点操作非常耗时， 尽量不要使用】
##############################################
img = cv2.imread('../src/RGB.jpg')
#获取某点的BGR颜色
px = img[100,100]
print(px)
#获取某点的蓝色值
blue = img[100,100,0]
print(blue)
#给图像某点直接赋值[运行较慢，暂时注释]
for i,row in enumerate(img):
    for j,pix in enumerate(row):
        if i % 100 == 0  or j % 50== 0:
            img[i][j] = [255,255,255]
show_img(img,usematplotlib=True)

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



##############################################
## 添加边框
##############################################
BLUE = (255,0,0)

img1 = cv2.imread('../src/opencv-logo.png')

replicate = cv2.copyMakeBorder(img1,20,20,20,20,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1,20,20,20,20,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1,20,20,20,20,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1,20,20,20,20,cv2.BORDER_WRAP)
constant= cv2.copyMakeBorder(img1,20,20,20,20,cv2.BORDER_CONSTANT,value=BLUE)

plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')

plt.show()