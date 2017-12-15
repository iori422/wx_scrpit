#coding:utf-8
import os


def gsize(driver):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    print x,y
    return x,y

def swipeup(driver,t): #屏幕向上滑动
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    x1 = int(x * 0.5)  # x坐标
    y1 = int(y * 0.25)  # 起始y坐标
    y2 = int(x * 0.75)  # 终点y坐标
    driver.swipe(x1,y1,x1,y2,t)

def swipeDown(driver,t): #屏幕向下滑动
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    x1 = int(x * 0.5)  # x坐标
    y1 = int(y * 0.25)  # 起始y坐标
    y2 = int(x * 0.75)  # 终点y坐标
    driver.swipe(x1, y1, x1, y2,t)
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
    x1=int(x*0.25)
    y1=int(y*0.5)
    x2=int(x*0.75)
    print x2
    driver.swipe(x1,y1,x2,y1,t)

def swip_downformadb(): #调取adb命令滑动屏幕操作
    swipd=os.system('adb shell input swipe 0 1600 300 300')
    return swipd
