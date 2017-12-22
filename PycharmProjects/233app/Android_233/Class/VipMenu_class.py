#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : VipMenu_class.py
# @Author: tutubuhaoci
# @Date  : 2017/12/19
# @Desc  :
import random


class vipmenu():
    def questionslist(self,driver): #VIP课程列表
        s = driver.find_elements_by_id('com.example.examda:id/quesCount_tv')
        random.choice(s).click()

    def question_gpkd(self,driver):#高频考点
        driver.find_element_by_id('com.example.examda:id/view01').click()

    def question_jdqh(self,driver):#阶段强化
        driver.find_element_by_id('com.example.examda:id/view01').click()

    def question_ctcz(self,driver):#错题重做
        driver.find_element_by_id('com.example.examda:id/view01').click()

    def question_gpkd_list(self,driver):#高频考点列表做题
        s = driver.find_elements_by_id('com.example.examda:id/doquesbtn')
        random.choice(s).click()

    def question_jdqh_list(self,driver):#阶段强化列表做题
        s = driver.find_elements_by_id('com.example.examda:id/viptest_btn')
        random.choice(s).click()

    def question_ctcz_list(self,driver):#错题重做列表做题
        s = driver.find_elements_by_id('com.example.examda:id/question_wrongfolder_tvReview')
        random.choice(s).click()




