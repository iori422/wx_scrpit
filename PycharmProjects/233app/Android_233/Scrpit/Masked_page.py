# coding:utf-8
import os
import re
from selenium import webdriver
from appium import webdriver
import time
def masked(driver):
    try:
        for i in range(3):
            time.sleep(1)
            driver.find_element_by_xpath('//android.widget.LinearLayout/android.widget.ImageView[contains(@index,1)]').click()
    except:

        print "尝试蒙版1"
    try:
        for i in range(3):
            time.sleep(1)
            driver.find_element_by_xpath('//android.widget.RelativeLayout/android.widget.Button[contains(@index,2)]').click()
    except:

        print "尝试蒙版2"

    try:
        for i in range(3):
            time.sleep(1)
            driver.find_element_by_xpath('//android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.Button').click()
    except:

        print "尝试蒙版3"
