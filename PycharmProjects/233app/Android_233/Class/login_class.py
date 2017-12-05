# coding:utf-8
import os
import re
from selenium import webdriver
from appium import webdriver
import time


class login_pag:
    def registered_button(self, driver):
        driver.find_element_by_name('注册').click()

    @staticmethod
    def memberid_edit(driver, menber):
        driver.find_element_by_name('帐号/邮箱/手机号').send_keys(str(menber))

    @staticmethod
    def psw_edit(driver, psw):
        driver.find_element_by_xpath("//android.widget.LinearLayout[contains(@index,2)]/android.widget."
                                     "EditText[contains(@index,1)]").send_keys(str(psw))

    @staticmethod
    def login_button(driver):
        try:
            for i in range(5):
                driver.find_element_by_name(u'登录').click()
                print driver.find_element_by_name(u'登录')
        except:
            print '登录成功'

    @staticmethod
    def forgot_psw(driver):
        driver.find_element_by_name('忘记密码').click()

    @staticmethod
    def memberid_clear(driver):
        # driver.find_element_by_xpath("//android.widget.LinearLayout[contains(@index,0)]/"
        #                            "android.widget.EditText").clear()
        driver.find_element_by_id('com.example.examda:id/no01_accountet').clear()

    def login(self, driver):
        menber = "of005"
        self.memberid_clear(driver=driver)
        time.sleep(1)
        self.memberid_edit(driver=driver, menber=menber)
        time.sleep(2)
        paswd = 111111
        self.psw_edit(driver=driver, psw=paswd)
        try:
            driver.hide_keyboard()
        except:
            return

        self.login_button(driver=driver)
