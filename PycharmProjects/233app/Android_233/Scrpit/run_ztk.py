# coding:utf-8
import os
import re
import time
from Android_233.Class.ChapterPracticeScreening_class import module_exam
from Android_233.Class.answer_class import answer
from Android_233.Class.home_class import home_page
from Android_233.Class.lnzt_class import lnzt_class
from Android_233.Class.login_class import login_pag
from Android_233.Class.menu_class import menu, directorytow
from Android_233.Class.paper_class import paper
from Android_233.Class.questionner_class import questionner
from Android_233.Scrpit.Boot_page import sett_1, permission, Boot_1, Boot_2, Boot_gps, app_hanginfo, app_servers
from Android_233.Scrpit.Masked_page import masked

driver = sett_1()
time.sleep(3)
try:
        app_servers(driver=driver, select=2)  # 选择api环境 1=183 2=t 3=正式
except:
        pass
time.sleep(2)
home_page().home_login(driver)# 登录页面
time.sleep(3)
question = menu().questions(driver)
question_zj = questionner().free_qustion6(driver)
lnzt_class().zt_list(driver)# 点击选择试卷做题页面
paper().paper_click(driver)
time.sleep(2)
amount = answer().amount(driver)
amount = int(amount)
for amount in range(amount):
        answer().answer_type(driver)#答题提交问卷
try:
        driver.find_element_by_id('com.example.examda:id/right_ques_btn').click()
except:
        driver.find_element_by_id('com.example.examda:id/nq03_answerll_answertv').click()
paper().paper_wdgf(driver)
print  "over"






