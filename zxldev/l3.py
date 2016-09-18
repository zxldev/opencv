#!/usr/bin/python2
# -*- coding: utf8 -*-
#
import cv2
import numpy as np
import math

"""
##############################################
##              鼠标事件                    ##
##############################################
"""

##############################################
## 打印所有事件
##############################################

events = [i for i in dir(cv2) if 'EVENT' in i]
print events


##############################################
## 全局变量
##############################################

drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1


##############################################
## 事件回调处理函数
##############################################

# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        statusBar(x,y)


    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),2)
        else:
            radis = int(math.sqrt((iy - y)*(iy - y) + (ix - x) * (ix - x)))
            cv2.circle(img,(ix,iy),radis,(0,0,255),2)
        statusBar()


##############################################
## 打印状态栏
##############################################

def statusBar(x=None,y=None):
    cv2.rectangle(img,(0,482),(512,512),(200,200,200),-1)
    if mode:
        shap = 'rectangle '
    else:
        shap = 'circle '
    text = "DrawShap:"+shap+"  start:("+str(ix)+","+str(iy)+")"
    if x:
        text = text + "  currentPoint:("+str(x)+","+str(y)+")"
    cv2.putText(img,text,(0,505),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0))

##############################################
## 定义画布，循环显示图像
##############################################

img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
    elif cv2.waitKey(1) & 0xFF == ord('m'):
        mode = not mode
        statusBar()
cv2.destroyAllWindows()