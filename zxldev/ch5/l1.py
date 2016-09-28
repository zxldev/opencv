#!/usr/bin/python2
# -*- coding: utf8 -*-
from zxldev.tools.common import *
import cv2

import numpy as np
# from matplotlib import pyplot as plt
"""
##############################################
##        直方图:查找、定位、分析            ##
##############################################
"""

img = cv2.imread('../src/reciept.jpg',0)
show_img(img)
a,img = cv2.threshold(img,155,255,cv2.THRESH_TOZERO)
show_img(img)
a,img = cv2.threshold(img,157,255,cv2.THRESH_BINARY)
# a,img = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
show_img(img)
equ = cv2.equalizeHist(img)
res = np.hstack((img,equ)) #stacking images side-by-side
show_img(res)