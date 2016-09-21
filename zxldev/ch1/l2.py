#!/usr/bin/python2
# -*- coding: utf8 -*-
import cv2
import numpy as np
from zxldev.tools.common import *

"""
##############################################
##              画图工具函数                 ##
##############################################
"""

##############################################
## 创建一个黑色背景的图像
##############################################
img = np.zeros((812,812,3), np.uint8)

##############################################
## 直线
##############################################
'''
img, 图像
pt1, 直线起点
pt2, 直线终点
color, 颜色
thickness=None, 线宽度
lineType=None,
shift=None
'''
cv2.line(img,(10,10),(10,500),(255,0,0),3)

##############################################
## 圆
##############################################

'''
img, 图像
center, 中心坐标
radius, 半径
color, 颜色
thickness=None, 线宽度
lineType=None,
shift=None
'''
cv2.circle(img, (0, 0), 63, (0, 0, 255),-1)


##############################################
## 矩形
##############################################
'''
img,
pt1, 左上角坐标
pt2, 右下角坐标
color,
thickness=None,
lineType=None,
shift=None
'''
cv2.rectangle(img,(30,30),(150,150),(0,255,0),-1)

##############################################
## 椭圆
##############################################
'''
img,
center,
axes, 椭圆轴长(x轴,y轴)
angle, 顺时针转角
startAngle, 扇区开始角度
endAngle, 扇区结束角度
color,
thickness=None,
lineType=None,
shift=None
'''
cv2.ellipse(img,center=(160,80),axes=(80,40),angle=0,startAngle=30,endAngle=330,color=(255,0,255),thickness=-1)


##############################################
## 多边形
##############################################
'''
img,
pts, 点坐标数组
isClosed, 是否闭合
color,
thickness=None,
lineType=None,
shift=None
'''
pts = np.array([[210,205],[290,290],[370,320],[350,210]], np.int32)
#切分数组方法，如果原始数据格式正确，可以不调用
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255),3)


##############################################
## 写入字体
##############################################
'''
img,
text,
org, 字体左下角位置
fontFace,
fontScale,
color,
thickness=None,
lineType=None,
bottomLeftOrigin=None 反转?
'''
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV zqq',(10,500), font, 5,(255,255,255),2,bottomLeftOrigin=0)

show_img(img,flags=cv2.CV_WINDOW_AUTOSIZE)
