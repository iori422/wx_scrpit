# coding:utf-8
import os
import re
from selenium import webdriver
from appium import webdriver
import time

class menu:
    def home(self,driver):
        driver.find_element_by_name('首页').click()

    def top(self,driver):
        driver.find_element_by_name('头条').click()

    def course(self,driver):
        driver.find_element_by_name('课程').click()

    def questions(self,driver):
        driver.find_element_by_id('com.example.examda:id/tvQuestion').click()

    def mymsg(self,driver):
        driver.find_element_by_name('我的').click()

class directorytow:
    def zjlx_directory(self,driver):
        time.sleep(3)
        click_drt = driver.find_elements_by_id('com.example.examda:id/nq02_lvitem_btn')
        click_drt[1].click()

