# coding:utf-8
import os
import re

import tmp as tmp
from selenium import webdriver
from appium import webdriver
import time

def screshot(driver):
    try:
        driver.find_element_by_id("kwsss").send_keys("selenium")
        driver.find_element_by_id("su1").click()
    except:
        driver.get_screenshot_as_file("/home/fnngj/python/error_png.png")