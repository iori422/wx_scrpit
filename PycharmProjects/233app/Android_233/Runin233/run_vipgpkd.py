#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : run_vipgpkd.py
# @Author: tutubuhaoci
# @Date  : 2017/12/18
# @Desc  : 
import time

from Android_233.Class.VipMenu_class import vipmenu
from Android_233.Class.answer_class import answer
from Android_233.Class.home_class import home_page
from Android_233.Class.lnzt_class import lnzt_class
from Android_233.Class.menu_class import menu
from Android_233.Class.paper_class import paper
from Android_233.Class.questionner_class import questionner
from Android_233.Scrpit.Boot_page import sett_1, app_servers


driver = sett_1()
time.sleep(5)
try:
        app_servers(driver=driver, select=2)  # 选择api环境 1=183 2=t 3=正式
except:
        pass
time.sleep(2)
home_page().home_login(driver)
time.sleep(3)
question = menu().questions(driver)
time.sleep(1)
question_zj = questionner().VIP_1(driver)
time.sleep(2)
vipmenu().questionslist(driver)
time.sleep(3)
vipmenu().question_gpkd_list(driver)
time.sleep(3)
paper().paper_click(driver)
time.sleep(3)
amount = answer().amount(driver)
time.sleep(3)
amount = int(amount)
for amount in range(amount):
        answer().answer_type(driver)
# time.sleep(3)
# try:
#         driver.find_element_by_id('com.example.examda:id/right_ques_btn').click()
# except:
#         driver.find_element_by_id('com.example.examda:id/nq03_answerll_answertv').click()
time.sleep(2)
paper().paper_wdgf(driver)
