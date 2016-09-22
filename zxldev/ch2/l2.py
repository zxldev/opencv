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
img1 = cv2.imread('../src/RGB.jpg')
img2 = cv2.imread('../src/RGB2.jpg')
show_img(img1+img2)
show_img(cv2.add(img1,img2))
dst = cv2.addWeighted(img1 , 0.7,img2,0.3,0)
show_img(dst)

##############################################
## 按位运算合并
##############################################
img1 = cv2.imread('../src/RGB2.jpg')
img2 = cv2.imread('../src/opencv_logo.png')

# Load two images
# img1 = cv2.imread('messi5.jpg')
# img2 = cv2.imread('opencv_logo.png')

# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]

# Now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 254, 255, cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask)
# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)
# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst

show_img(img1)


img = cv2.imread('../src/reciept.jpg')
imggray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
show_img(imggray)
ret, mask = cv2.threshold(imggray, 160, 255, cv2.THRESH_BINARY_INV)
img_fg = cv2.bitwise_and(img,img,mask = mask)
show_img(img_fg,flags=cv2.WINDOW_NORMAL)