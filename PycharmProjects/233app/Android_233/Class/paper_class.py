# coding:utf-8
import os
import random
import re
from selenium import webdriver
from appium import webdriver
import time

from Android_233.Class.answer_class import answer
from Android_233.Scrpit.Operate import swipLeft


class paper():
    def paper_practice(self,driver):
        driver.find_element_by_id('com.example.examda:id/nq08_exercisemode_btn').click()

    def paper_examination(self,driver):
        driver.find_element_by_id('com.example.examda:id/nq08_exammode_btn').click()

    def paper_click(self,driver):
        t1 =driver.find_element_by_id('com.example.examda:id/nq08_exercisemode_btn')
        t2 =driver.find_element_by_id('com.example.examda:id/nq08_exammode_btn')
        slc=[t1,t2]
        random.choice(slc).click()
        print u'选择模式'
        return driver

    def paper_wdgf(self,driver):
        driver.find_element_by_id('com.example.examda:id/question_pop_submit_btn').click()
        amount = answer().amount(driver)
        amount = int(amount)
        try:
            for i in range(amount):
                driver.find_element_by_id('com.example.examda:id/nq04_usergradeselfet').send_keys('6')
                driver.find_element_by_id('com.example.examda:id/nq04_savegradebtn').click()
                swipLeft(driver=driver, t=800)
        except:
            pass

        #driver.find_element_by_id('com.example.examda:id/nq03_answerll_answertv').click()











