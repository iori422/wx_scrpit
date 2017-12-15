# -*- coding: utf-8 -*-
# @File  : run_mnst.py
# @Author: tutubuhaoci
# @Date  : 2017/12/15
# @Desc  :

class questionner: #主菜单题库页面
    def remind_qustion(self,driver):
        driver.find_element_by_name('提醒做题').click()

    def VIP_1(self,driver):
        driver.find_element_by_name(u'高频考点题').click()

    def VIP_2(self,driver):
        driver.find_element_by_name(u'机考真题库').click()

    def VIP_3(self,driver):
        driver.find_element_by_name(u'考前押题').click()

    def free_qustion1(self,driver):
        driver.find_element_by_name(u'章节练习').click()

    def free_qustion2(self,driver):
        driver.find_element_by_name(u'每日一练').click()

    def free_qustion3(self,driver):
        driver.find_element_by_name(u'离线题库').click()

    def free_qustion4(self,driver):
        driver.find_element_by_name(u'挑战积分').click()

    def free_qustion5(self,driver):
        driver.find_element_by_name(u'易错题').click()

    def free_qustion6(self,driver):
        driver.find_element_by_name(u'历年真题').click()

    def free_qustion7(self,driver):
        driver.find_element_by_name(u'模拟试题').click()

    def my_qustion1(self,driver):
        driver.find_element_by_name(u'我的评估').click()

    def my_qustion2(self,driver):
        driver.find_element_by_name(u'试题收藏').click()

    def my_qustion3(self,driver):
        driver.find_element_by_name(u'错题集').click()

    def my_qustion4(self,driver):
        driver.find_element_by_name(u'做题记录').click()

    def my_qustion5(self,driver):
        driver.find_element_by_name(u'我的解析').click()








