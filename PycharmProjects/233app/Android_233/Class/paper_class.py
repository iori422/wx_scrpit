# -*- coding: utf-8 -*-
# @File  : run_mnst.py
# @Author: tutubuhaoci
# @Date  : 2017/12/15
# @Desc  :
import random
from _pytest import unittest
import time
from Android_233.Class.answer_class import answer
from Android_233.Scrpit.Operate import swipLeft
class paper():
    def paper_practice(self,driver):
        driver.find_element_by_id('com.example.examda:id/nq08_exercisemode_btn').click()

    def paper_examination(self,driver):
        driver.find_element_by_id('com.example.examda:id/nq08_exammode_btn').click()

    def paper_click(self,driver):
        try:
            t1 =driver.find_element_by_id('com.example.examda:id/nq08_exercisemode_btn')
        except:
            t1 =driver.find_element_by_id('com.example.examda:id/vip_lxms')
        try:
            t2 =driver.find_element_by_id('com.example.examda:id/nq08_exammode_btn')
        except:
            t2 =driver.find_element_by_id('com.example.examda:id/vip_ksms')
        slc=[t1,t2]
        random.choice(slc).click()
        print u'选择模式'
        return driver

    def paper_wdgf(self,driver):
        try:
            driver.find_element_by_id('com.example.examda:id/question_pop_submit_btn').click()
            amount = answer().amount(driver)
            amount = int(amount)
            print "问答评估分sssssssssssssss s%"+str(amount)
            for amount in range(amount+1):
                try:
                    time.sleep(2)
                    driver.find_element_by_id('com.example.examda:id/nq04_usergradeselfet').send_keys('1')
                    driver.find_element_by_id('com.example.examda:id/nq04_savegradebtn').click()
                    time.sleep(2)
                    swipLeft(driver=driver,t=300)
                except:
                    pass
            driver.find_element_by_id('com.example.examda:id/nq03_choice_answerll').click()#提交试卷
        except:
            print "没有找到元素"
        time.sleep(2)
        self.check_answer(driver) #

        if __name__ == '__main__':
            unittest.main()

    def check_answer(self,driver): #查看答案解析
        try:
            elem = driver.find_element_by_id('com.example.examda:id/nq06_seeanalyze_btn')
            time.sleep(1)
            elem.click()
        except:
            elem2 = driver.find_element_by_id('com.example.examda:id/seeanalyze_tv')
            time.sleep(1)
            elem2.click()

    def retest_answer(self,driver): #重新测试

        elem =driver.find_element_by_id('com.example.examda:id/nq06_retest_btn')
        for i in range(3):
            try:
                time.sleep(1)
                elem.click()
            except:
                pass

    def assess_answer(self,driver): #评价试卷

        elem =driver.find_element_by_name(u'评价试卷')
        for i in range(3):
            try:
                time.sleep(1)
                elem.click()
            except:
                pass








