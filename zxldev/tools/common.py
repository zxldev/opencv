#!/usr/bin/python2
# -*- coding: utf8 -*-
import cv2
from zxldev.tools.osUtils import *
import os
import time

global PJ_ROOT_PATH
PJ_ROOT_PATH=os.getcwd()


'''
显示图片
'''
def show_img( img,title = 'image',closeAll = True,flags = cv2.WINDOW_NORMAL,usematplotlib = False):
    if usematplotlib:
        show_img_matplotlib(img, title, closeAll, flags)
    else:
        show_img_common(img,title,closeAll,flags)

'''
显示多张图片
'''
def show_imgs(imgMap):
    from matplotlib import pyplot as plt
    import math
    lenImg = len(imgMap)
    column = math.ceil(math.sqrt(lenImg))
    #计算行数
    row = column - math.floor((column*column - lenImg)/column)
    counter = 1
    if isinstance(imgMap,list):
        for img in imgMap:
            plt.subplot(row,column,counter), plt.imshow(img), plt.title(str(counter))
            plt.xticks([]), plt.yticks([])
            counter = counter + 1
    if isinstance(imgMap, dict):
        for title in imgMap:
            plt.subplot(row, column, counter), plt.imshow(imgMap[title]), plt.title(title)
            plt.xticks([]), plt.yticks([])
            counter = counter + 1
    plt.show()

def show_img_common(img,title = 'image',closeAll = True,flags = cv2.WINDOW_NORMAL):
    # cv2.WINDOW_AUTOSIZE 自适应图片
    # cv2.WINDOW_NORMAL 正常展示
    # cv2.WINDOW_OPENGL 需要OPENGL支持
    cv2.namedWindow(title, flags=flags)
    cv2.imshow(title, img)
    k = cv2.waitKey(0)
    # 如果是64位系统，执行操作
    if os_bits() == 64:
        k = k & 0xFF
    if k == ord('s'):  # wait for 's' key to save and exit
        timeStr = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
        if title == 'image':
            fileName = 'autoSave' + timeStr
        else:
            fileName = title + timeStr
        cv2.imwrite(os.path.join(PJ_ROOT_PATH, '../dest/' + fileName + '.png'), img)
    if closeAll or k == 27:
        cv2.destroyAllWindows()

def show_img_matplotlib( img,title = 'image',closeAll = True,flags = cv2.WINDOW_NORMAL):
    from matplotlib import pyplot as plt
    plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB), cmap='gray', interpolation='bicubic')
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()
