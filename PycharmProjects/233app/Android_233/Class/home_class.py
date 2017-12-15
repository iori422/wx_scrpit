# coding:utf-8
from _pytest import unittest
from Android_233.Class.login_class import login_pag
class home_page:  #主菜单个人信息页面
    def message(self,driver):
        driver.find_element_by_accessibility_id('消息中心').click()

    def servers(self,driver):
        driver.find_element_by_accessibility_id('客服').click()

    def table_1(self,driver):
        driver.find_element_by_name('选课试听').click()

    def table_2(self,driver):
        driver.find_element_by_name('我的课程').click()

    def table_3(self,driver):
        driver.find_element_by_name('离线课程').click()

    def table_4(self,driver):
        driver.find_element_by_name('课程答疑').click()

    def table_5(self,driver):
        driver.find_element_by_name('听课记录').click()

    def table_6(self,driver):
        driver.find_element_by_name('章节练习').click()

    def table_7(self,driver):
        driver.find_element_by_name('VIP题库').click()

    def table_8(self,driver):
        driver.find_element_by_name('做题记录').click()

    def table_9(self,driver):
        driver.find_element_by_name('错题集').click()

    def table_10(self,driver):
        driver.find_element_by_name('全部').click()

    def top_1(self,driver):
        driver.find_element_by_id('com.example.examda:id/e12_activitynews').click()

    def top_2(self,driver):
        driver.find_element_by_id('com.example.examda:id/e12_newsitemlayout').click()

    def top_3(self,driver):
        driver.find_element_by_id('com.example.examda:id/changenews').click()

    def home_coursemore(self,driver):
        driver.find_element_by_id('com.example.examda:id/viewmore').click()

    def home_mycourse(self,driver):
        driver.find_element_by_name('进入我的课程').click()

    def home_questionnairemore(self,driver):
        driver.find_element_by_id('com.example.examda:id/viewmore').click()

    def home_questionnaire(self,driver):
        driver.find_element_by_name('进入我的题库').click()

    def home_login(self,driver): #登录操作
        try:
            driver.find_element_by_id("com.example.examda:id/tvMy").click()
            driver.find_element_by_id('com.example.examda:id/no09_user_jifen_ll')#已登录
            driver.find_element_by_id('com.example.examda:id/ivQuestion').click()
            print '已登录'
        except:
            driver.find_element_by_id("com.example.examda:id/tvMy").click()
            driver.find_element_by_id('com.example.examda:id/no09_user_no_login').click()  # 我的注册
            t = login_pag()
            t.login(driver=driver)
            driver.find_element_by_id('com.example.examda:id/no01_loginbut').click()
            print '未登录'

        if __name__ == '__main__':
            unittest.main()









