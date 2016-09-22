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

img = cv2.imread('../src/reciept.jpg',0)
edges = cv2.Canny(img,100,200)

show_img(edges)