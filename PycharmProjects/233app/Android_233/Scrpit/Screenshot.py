# -*- coding: utf-8 -*-
# @File  : run_mnst.py
# @Author: tutubuhaoci
# @Date  : 2017/12/15
# @Desc  : 
def screshot(driver):
    try:
        driver.find_element_by_id("kwsss").send_keys("selenium")
        driver.find_element_by_id("su1").click()
    except:
        driver.get_screenshot_as_file("/home/fnngj/python/error_png.png")