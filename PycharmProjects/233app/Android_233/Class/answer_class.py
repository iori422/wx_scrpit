# coding:utf-8
import os
import re
import random

from selenium import webdriver
from appium import webdriver
import time

from Android_233.Scrpit.Operate import swipLeft, swipeDown, swipeup


class answer():
    def messagWrong_answer(self,driver):
        try:
            driver.find_element_by_id('com.example.examda:id/charmsg_tv')
            driver.find_element_by_id('com.example.examda:id/knewitbtn').click()
        except:
            pass
    def jd_answer(self,driver):  #简答页面处理
        try:
            swipeup(driver, t=800)
        except:
            pass
        self.messagWrong_answer(driver)
        text = 111
#       driver.find_element_by_id('com.example.examda:id/onlydo_ckb').click()
        driver.find_element_by_id('com.example.examda:id/nq03_fillblank_tv').click()
        time.sleep(1)
        driver.find_element_by_class_name('android.widget.EditText').send_keys(text)
        driver.hide_keyboard()
        try:
            driver.find_element_by_id('com.example.examda:id/savedialog').click()
        except:
            driver.find_element_by_name(u'保存').click()
        time.sleep(1)
        swipLeft(driver=driver, t=800)
        return driver

    def danx_answer(self,driver): #单选题页面处理
        try:
            swipeup(driver=driver, t=800)
        except:
            pass
        self.messagWrong_answer(driver)
        option = driver.find_elements_by_id('com.example.examda:id/nq03_noritem_uppercase')
        random.choice(option).click()
        time.sleep(1)
        #driver.find_element_by_id('com.example.examda:id/right_ques_iv').click()
        swipLeft(driver=driver, t=800)
        return driver

    def danx2_answer(self,driver): #单选题页面处理
        try:
            swipeup(driver=driver, t=1500)
        except:
            pass
        self.messagWrong_answer(driver)
        option = driver.find_elements_by_id('com.example.examda:id/nq03_button_option')
        random.choice(option).click()
        time.sleep(1)
        #driver.find_element_by_id('com.example.examda:id/right_ques_iv').click()
        swipLeft(driver=driver, t=800)
        return driver



    def duox1_answer(self,driver): #多选题页面处理
        try:
            swipeup(driver=driver, t=1500)
        except:
            pass
        self.messagWrong_answer(driver)
        option = driver.find_elements_by_id('com.example.examda:id/nq03_checkbox_option')
        print option
        for i in range(1,4):
            random.choice(option).click()
        swipLeft(driver=driver, t=800)
        return driver

    def duox2_answer(self,driver): #多选题页面处理2
        try:
            swipeup(driver=driver, t=1500)
        except:
            pass
        self.messagWrong_answer(driver)
        option = driver.find_elements_by_id('com.example.examda:id/nq03_multiitem_uppercase')
        print option
        for i in range(1, 4):
            random.choice(option).click()
        swipLeft(driver=driver, t=800)
        return driver

    def tk_answer(self,driver): #填空题页面处理
        try:
            swipeup(driver=driver, t=1500)
        except:
            pass
        self.messagWrong_answer(driver)
        text = 111
        driver.find_element_by_id('com.example.examda:id/onlydo_ckb').click()
        driver.find_element_by_id('com.example.examda:id/nq03_fillblank_tv').click()
        driver.find_element_by_class_name('android.widget.EditText').send_keys(text)
        try:
            driver.find_element_by_id('com.example.examda:id/savedialog').click()
        except:
            driver.find_element_by_name(u'保存').click()
        time.sleep(1)
        driver.hide_keyboard()#隐藏键盘
        swipLeft(driver=driver, t=800)
        return driver

    def tl_answer(self,driver): #听力题页面处理
        try:
            swipeup(driver=driver, t=1500)
        except:
            pass
        self.messagWrong_answer(driver)
        driver.find_element_by_id('com.example.examda:id/playpausebtn').click()
        time.sleep(8)
        option = driver.find_elements_by_id('com.example.examda:id/nq03_noritem_uppercase')
        random.choice(option).click()
        swipLeft(driver=driver, t=800)
        return driver

    def pd_answer(self,driver): #判断题页面处理
        try:
            swipeup(driver=driver, t=1500)
        except:
            pass
        self.messagWrong_answer(driver)
        right = driver.find_element_by_id('com.example.examda:id/judgeitem_right_ll')
        wrong = driver.find_element_by_id('com.example.examda:id/judgeitem_wrong_ll')
        slct = [right,wrong]
        random.choice(slct).click()
        swipLeft(driver=driver, t=800)
        return driver



    def solution(self,driver): #答案和收藏
        driver.find_element_by_name('答案').click()
        time.sleep(2)
        driver.find_element_by_name('收藏').click()
        return driver

    def answer_type(self,driver):
        time.sleep(2)
        titletxt= driver.find_element_by_id('com.example.examda:id/nq03_choice_questype_tv').text
        print titletxt
        #titletxt=str(titletxt)
        time.sleep(2)
        if titletxt ==u'简答题':
            self.jd_answer(driver=driver)
        elif titletxt ==u'单选题':
            try:
                self.danx_answer(driver=driver)
            except:
                self.danx2_answer(driver=driver)
        elif titletxt ==u'多选题':
            try:
                self.duox1_answer(driver=driver)
            except:
                self.duox2_answer(driver=driver)
        elif titletxt ==u'判断题':
            self.pd_answer(driver=driver)
        elif titletxt ==u'不定项选择题':
            try:
                self.duox1_answer(driver=driver)
            except:
                self.duox2_answer(driver=driver)
        elif titletxt ==u"填空题":
            self.jd_answer(driver=driver)  # 填空题

        try:
            driver.find_element_by_id('com.example.examda:id/dialog_but_r').click()
            print '提交试卷'
        except:
            pass

    def amount(self,driver):
        amount = driver.find_element_by_id('com.example.examda:id/nq03_choice_ques_total').text
        amount =str(amount)
        amount =str(amount[1:])
        return amount









