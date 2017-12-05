#coding:utf-8
import os
from selenium import webdriver
from appium import webdriver
import time
def gsize(driver):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    print x,y
    return x,y
def swipeup(driver): #屏幕向上滑动
    l = gsize()
    x1 = int(l[0]*0.5)
    y1 = int(l[1]*0.75)
    y2 = int(l[1]*0.25)
    driver.swipe(x1,y1,x1,y2,t)

def swipeDown(driver): #屏幕向下滑动
    l = gsize()
    x1 = int(l[0] * 0.5)  # x坐标
    y1 = int(l[1] * 0.25)  # 起始y坐标
    y2 = int(l[1] * 0.75)  # 终点y坐标
    driver.swipe(x1, y1, x1, y2, t)
    print "滑动下"

def swipLeft(driver,t):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    x1=int(x*0.75)
    y1=int(y*0.5)
    x2=int(x*0.02)
    driver.swipe(x1,y1,x2,y1,t)
    #print "滑动右"

def swipRight(driver,t):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    print x, y
    x1=int(x*0.25)
    print x1
    y1=int(y*0.5)
    print y1
    x2=int(x*0.75)
    print x2
    driver.swipe(x1,y1,x2,y1,t)






