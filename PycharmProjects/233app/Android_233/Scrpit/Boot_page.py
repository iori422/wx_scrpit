# coding:utf-8
# -*- coding: utf-8 -*-
# @File  : run_mnst.py
# @Author: tutubuhaoci
# @Date  : 2017/12/15
# @Desc  :
import re
from selenium import webdriver
from appium import webdriver
import time
import os
from Operate import swipLeft


def sett_1(): #获取手机相关信息 并配置appium
    # 测试的包的路径和包名
    # appLocation = " E:\Android233_vs\Android2.6.3.apk "
    # 读取设备 id
    readDeviceId = list(os.popen('adb devices -l').readlines())
    # 正则表达式匹配出 id 信息
    deviceId = re.findall(r'^\w*\b', readDeviceId[1])[0]
    # 读取设备系统版本号
    deviceAndroidVersion = list(os.popen('adb shell getprop ro.build.version.release').readlines())
    deviceVersion = re.findall(r'^\w*\b', deviceAndroidVersion[0])[0]
    deviceVersion = float(deviceVersion.replace('\r', '').replace('\n', '').replace('\t', ''))
    brand = list(os.popen('adb shell getprop ro.product.brand').readlines())
    brand = re.findall(r'^\w*\b', brand[0])[0]
    model = list(os.popen('adb shell getprop ro.product.model').readlines())
    model = re.findall(r'\w*\s\B', model[0])[0]
    model = model.replace('\r', '').replace('\n', '').replace('\t', '')
    PATH = lambda p: os.path.abspath(
        os.path.join(os.path.dirname(__file__), p)
    )
    print model, deviceId, deviceVersion
    desired_caps = {}
    desired_caps['deviceName'] = deviceId  # 通过adb devices -l查看设备标识#WTKDU16A17013707 #Q4JNPVO7CY7DAM6L
    desired_caps['platformName'] = 'Android'
    desired_caps['browserName'] = ''
    desired_caps['platformVersion'] = deviceVersion
    # desired_caps['app'] = PATH('E:/Android233_vs/Android2.6.2.apk')#这里手动把app装到手机里，就注释点即可，如果打开，会根据路径安装app
    desired_caps['appPackage'] = 'com.example.examda'  # app的包名，具体这块还不是很了解
    desired_caps['appActivity'] = 'com.example.examda.activity.E01_AccessActivity'  # 打开应用的第一个Activity，具体不了解
    time.sleep(3)
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 连接设备并打开应用

    return driver


def permission (driver): #权限
    time.sleep(5)
    try: # 检查权限请求
        for i in range(5):
            time.sleep(2)
            driver.find_element_by_name(u'允许').click()
    except:
        print "权限选择完毕"

def Boot_1(driver): #引导页1
    time.sleep(5)
    try:
        for i in range(3):# 左侧滑动
            swipLeft(driver=driver, t=800)
            time.sleep(2)
        driver.find_element_by_class_name('android.widget.Button').click()
        driver.find_element_by_name(u'开启新体验').click()
        driver.get_screenshot_as_file(r"C:\Users\Administrator\Desktop\登录\1.png")
    except:
        print 'Boot_1输出完毕'

def Boot_2(course,driver): #引导页面选择课程
    try:
        driver.find_element_by_class_name('android.widget.EditText').send_keys(course)
        time.sleep(3)
        driver.find_element_by_name(u'请输入考试类别').send_keys(course)
    except:
        print '222'
    try:
        driver.find_element_by_name(course).click()
        time.sleep(3)
        t = driver.find_elements_by_class_name('android.widget.TextView').click()
        driver.find_element_by_class_name(t[0]).click()
        driver.get_screenshot_as_file(r"C:\Users\Administrator\Desktop\登录\1.png")
    except:
        print '222'
    print "Boot_2,输出完毕"


def Boot_gps(city,driver): #引导页面定位
    try:
        driver.find_element_by_name(u'请输入报考地址').send_keys(city)
        time.sleep(3)
        driver.find_element_by_class_name('android.widget.EditText').send_keys(city)
    except:
        print '33333'
    try:
        driver.find_element_by_name(city).click()
        time.sleep(3)
        driver.find_element_by_class_name('com.example.examda:id/locationtext').click()
        driver.get_screenshot_as_file(r"C:\Users\Administrator\Desktop\登录\1.png")
    except:
        print '44444'
    print "Boot_gps,输出完毕"


def app_hanginfo():
    psid = list(os.popen('adb shell ps | find "com.example.examda"').readlines())
    return psid

def app_servers(driver,select):
    print select
    if select==1:
        driver.find_element_by_id("com.example.examda:id/dialog_189").click()
    elif select==2:
        driver.find_element_by_id('com.example.examda:id/dialog_t').click()
        time.sleep(2)
    else:
        driver.find_element_by_id('com.example.examda:id/dialog_api').click()




# a = app_hanginfo()
# print a
# # sett_1()