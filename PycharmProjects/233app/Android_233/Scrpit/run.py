# coding:utf-8
import time
from Android_233.Class.ChapterPracticeScreening_class import module_exam
from Android_233.Class.answer_class import answer
from Android_233.Class.home_class import home_page
from Android_233.Class.login_class import login_pag
from Android_233.Class.menu_class import menu, directorytow
from Android_233.Class.questionner_class import questionner
from Android_233.Scrpit.Boot_page import sett_1, permission, Boot_1, Boot_2, Boot_gps, app_hanginfo, app_servers
from Android_233.Scrpit.Masked_page import masked


#-------------------------------------------登录--------------------------------------
driver = sett_1()
app_servers(driver=driver, select=2)  # 选择api环境 1=183 2=t 3=正式

try:
    driver.find_element_by_name(u'权限请求')
    permission(driver)
except:
    pass
    #print "跳过权限选择"

try:
    driver.find_element_by_name(u'全新首页')
    Boot_1(driver)
except:
    pass
    #print"跳过第一次登录流程"
time.sleep(2)
try:
    driver.find_element_by_name(u'考试分类')
    Boot_2(course=u'证券从业', driver=driver)
except:
    pass
    #print"跳过考试分类"
time.sleep(3)
try:
    driver.find_element_by_name(u'报考地区')
    Boot_gps(city=u'湖南', driver=driver)
    masked(driver=driver)
except:
    pass
    #print"跳过报考地区"
time.sleep(3)
home_page().home_login(driver)# 登录页面
time.sleep(3)
menu().questions(driver)  #进入题库
questionner().free_qustion1(driver)  #章节练习
time.sleep(3)
directorytow().zjlx_directory(driver)  #目录选择
module_exam().all_type(driver)  #全部题型
module_exam().amount10(driver)  #10题
time.sleep(2)
module_exam().start_exam(driver)  #开始做题

time.sleep(7)
amount = answer().amount(driver)
amount = int(amount)
for amount in range(amount):
        answer().answer_type(driver)#答题提交问卷
try:
        driver.find_element_by_id('com.example.examda:id/right_ques_btn').click()
except:
        driver.find_element_by_id('com.example.examda:id/nq03_answerll_answertv').click()
print  "over"



