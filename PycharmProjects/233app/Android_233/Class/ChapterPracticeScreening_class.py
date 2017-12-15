# -*- coding: utf-8 -*-
# @File  : run_mnst.py
# @Author: tutubuhaoci
# @Date  : 2017/12/15
# @Desc  :
class module_exam:#章节练习页面
    def all_type(self,driver):  #选择题型
        driver.find_element_by_name('全部').click()

    def dx_type(self,driver):
        driver.find_element_by_name('单选题').click()

    def dx_type(self,driver):
        driver.find_element_by_name('多选题').click()

    def pd_type(self,driver):
        driver.find_element_by_name('判断题').click()

    def tk_type(self,driver):
        driver.find_element_by_name('填空题').click()

    def jd_type(self,driver):
        driver.find_element_by_name('简答题').click()

    def amount5(self,driver):# 选择题目数量
        driver.find_element_by_name('5').click()

    def amount10(self,driver):
        driver.find_element_by_name('10').click()

    def amount15(self,driver):
        driver.find_element_by_name('15').click()

    def amount20(self,driver):
        driver.find_element_by_name('20').click()

    def amount25(self,driver):
        driver.find_element_by_name('25').click()

    def amount30(self,driver):
        driver.find_element_by_name('30').click()

    def amount35(self,driver):
        driver.find_element_by_name('35').click()

    def start_exam(self,driver): #开始做题
        driver.find_element_by_id('com.example.examda:id/nq02_startdo_btn').click()