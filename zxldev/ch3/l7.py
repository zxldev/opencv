#!/usr/bin/python2
# -*- coding: utf8 -*-
from zxldev.tools.common import *
import cv2

import numpy as np
# from matplotlib import pyplot as plt
"""
##############################################
##                边缘检测                  ##
##############################################
"""
src = cv2.imread('../src/reciept.jpg')
img = cv2.imread('../src/reciept.jpg',0)
mask = cv2.Canny(img,90,250)
# show_img(mask)
mask_inv = cv2.bitwise_not(mask)

# a,mask = cv2.threshold(mask,0,255,cv2.THRESH_BINARY)

# img1_bg = cv2.bitwise_and(mask_inv,mask_inv,mask = mask)
a,img2_fg = cv2.threshold(img,155,255,cv2.THRESH_TOZERO)
img2_fg = cv2.bitwise_and(img2_fg,img2_fg,mask = mask_inv)
show_img(img2_fg,'描边+加黑')
kernel = kernel = np.ones((6,6),np.uint8)
img2_fg =cv2.erode(img2_fg,kernel,iterations = 1)
show_img(img2_fg,'膨胀')

edges = cv2.Canny(img2_fg,200,1000,apertureSize = 5)

lines = cv2.HoughLines(edges,1,np.pi/180,200)
for rho,theta in lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 2000*(-b))
    y1 = int(y0 + 2000*(a))
    x2 = int(x0 - 2000*(-b))
    y2 = int(y0 - 2000*(a))

    cv2.line(src,(x1,y1),(x2,y2),(0,0,255),2)
#
#
# contours,hierarchy = cv2.findContours(img2_fg,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# show_img(img)
# for c in contours:
#     peri = cv2.arcLength(c, True)
#     approx = cv2.approxPolyDP(c, 0.1 * peri, True)
#     # if our approximated contour has four points, then
#     # we can assume that we have found our screen
#     if len(approx) == 4:
#         screenCnt = approx
#         # break
#
#         cv2.drawContours(src, [screenCnt], -1, (0, 255, 0), 1)
show_img(src)
# # dst = cv2.add(img1_bg,img2_fg)

