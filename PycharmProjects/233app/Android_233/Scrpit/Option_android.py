# -*- coding: utf-8 -*-
# @File  : run_mnst.py
# @Author: tutubuhaoci
# @Date  : 2017/12/15
# @Desc  :
import os
import time
from selenium import webdriver


class Option_operate(object):
    def __init__(self,deviceName,platformVersion,app,appPackage,appActivity):
        self.deviceName='WTKDU16A17013707'
        self.platformVersion='4.4.2'
        self.app="r'E:\Android233_vs\Android2.6.3.apk'"
        self.appPackage = 'com.example.examda'
        self.appActivity ='com.example.examda.activity.E01_AccessActivity'

    def option_appium(self,selenium):
        PATH = lambda p: os.path.abspath(
            os.path.join(os.path.dirname(__file__), p)
        )
        desired_caps = {}
        desired_caps['deviceName'] = 'WTKDU16A17013707'  # 通过adb devices -l查看设备标识#WTKDU16A17013707 #Q4JNPVO7CY7DAM6L
        desired_caps['platformName'] = 'Android'
        desired_caps['browserName'] = ''
        desired_caps['platformVersion'] = '4.4.2'  # 4.4.2
        desired_caps['app'] = PATH(r'E:\Android233_vs\Android2.6.3.apk')#这里手动把app装到手机里，就注释点即可，如果打开，会根据路径安装app
        desired_caps['appPackage'] = 'com.example.examda'  # app的包名，具体这块还不是很了解
        desired_caps['appActivity'] = 'com.example.examda.activity.E01_AccessActivity'  # 打开应用的第一个Activity，具体不了解
        time.sleep(3)
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 连接设备并打开应用
        time.sleep(10)
        return driver


    def permission(self,driver):
        try:
            for i in range(100):
                button_name = u'允许'
                time.sleep(3)
                driver.find_element_by_name(button_name).click()


        except:
                print '权限已选择完毕！'
        return button_name

#if __name__ == '__main__':
    #driver = Option_operate(deviceName='WTKDU16A17013707',platformVersion='4.4.2',app="r'E:\Android233_vs\Android2.6.3.apk'",
                            #appPackage = 'com.example.examda',appActivity ='com.example.examda.activity.E01_AccessActivity').option_appium()
#button_name = Option_operate().permission(driver)
    def app_hanginfo(self):
        self.psid = list(os.popen('adb shell ps').readlines())
        return self.psid




