# -*- coding: utf-8 -*-
# @File  : run_mnst.py
# @Author: tutubuhaoci
# @Date  : 2017/12/15
# @Desc  :
import time
from Android_233.Class.ChapterPracticeScreening_class import module_exam
from Android_233.Class.answer_class import answer
from Android_233.Class.home_class import home_page
from Android_233.Class.menu_class import menu, directorytow
from Android_233.Class.questionner_class import questionner
from Android_233.Scrpit.Boot_page import sett_1, permission, Boot_1, Boot_2, Boot_gps, app_hanginfo, app_servers
from Android_233.Scrpit.Masked_page import masked
driver = sett_1()
app_servers(driver=driver, select=2)  # 选择api环境 1=183 2=t 3=正式

try:
    driver.find_element_by_name(u'权限请求')
    permission(driver)
except:
    pass
try:
    driver.find_element_by_name(u'全新首页')
    Boot_1(driver)
except:
    pass
time.sleep(2)
try:
    driver.find_element_by_name(u'考试分类')
    Boot_2(course=u'证券从业', driver=driver)
except:
    pass
time.sleep(3)
try:
    driver.find_element_by_name(u'报考地区')
    Boot_gps(city=u'湖南', driver=driver)
    masked(driver=driver)
except:
    pass
time.sleep(3)
home_page().home_login(driver)
time.sleep(3)
menu().questions(driver)
questionner().free_qustion1(driver)
time.sleep(3)
directorytow().zjlx_directory(driver)
module_exam().all_type(driver)
module_exam().amount10(driver)
time.sleep(2)
module_exam().start_exam(driver)

time.sleep(7)
amount = answer().amount(driver)
amount = int(amount)
for amount in range(amount):
        answer().answer_type(driver)
try:
        driver.find_element_by_id('com.example.examda:id/right_ques_btn').click()
except:
        driver.find_element_by_id('com.example.examda:id/nq03_answerll_answertv').click()
print  "over"



