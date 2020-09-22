'''
 * @Author: wutian 
 * @Date: 2020-09-21 21:24:30 
 * @Last Modified by:   wutian 
 * @Last Modified time: 2020-09-21 21:24:30 
 * 参考网址：https://blog.csdn.net/HuangZhang_123/article/details/80511270?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-4.channel_param&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-4.channel_param
'''
import numpy as np
import cv2 as cv
from matplotlib import pyplot as pyplot
import sys


if __name__ == '__main__':
    path = input('Enter your path:\n')
    img = cv.imread(path,0)
    if img is None:
        print('can\'t open path')
    #高斯滤波
    blur = cv.cvtColor(img.copy(), cv.COLOR_BGR2GRAY)
    #Otsu 二值化
    ret,th = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
    #查找图形轮廓
    contours,hier = cv.findContours(th,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    for c in contours:
        #绘制轮廓矩形
        x,y,w,h = cv.boundingRect(c)
        cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        #绘制第二种矩形
        #查找最小面积矩形
        rect = cv.minAreaRect(c)
        box = cv.boxPoints(rect) 
        box = np.int0(box)
        print(box)
        cv.drawContours(img, [box], -1, (0, 0, 255), 3)
        #绘制轮廓圆
        (x,y),radius = cv.minEnclosingCircle(c)
        center = (int(x),int(y))
        radius = int(radius)
        cv.circle(img,center,radius,(0,255,0),2)
    #绘制紧贴的轮廓
    cv.drawContours(img,contours,-1,(255,0,0),2)
    cv.imshow('img',img)
    cv.waitKey(0)
    cv.destroyAllWindows()
    
