# coding:utf-8
import random
class lnzt_class():
    def kemu1_catalog(self,driver):
        driver.find_element_by_id('com.example.examda:id/nq07_subject_tv').click()


    def kemu2_catalog(self,driver):
        text = driver.find_elements_by_id('com.example.examda:id/nq02_pop_chaptername')
        random.choice(text).click()
        print text

    def catalog_click(self,driver):#历年真题入口
        self.kemu1_catalog(driver)
        self.kemu2_catalog(driver)


    def zt_year(self,driver):#年份
        button =driver.find_element_by_id('com.example.examda:id/nq07_year_tv')
        button.click()
        text = driver.find_elements_by_id('com.example.examda:id/nq02_pop_chaptername')
        random.choice(text).click()

    def zt_list(self,driver):#历年真题列表
        text =driver.find_elements_by_id('com.example.examda:id/nq07_paper_btn')
        random.choice(text).click()







