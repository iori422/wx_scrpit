#coding:utf-8
import time
from Android_233.Class.menu_class import menu
from Android_233.Scrpit.Boot_page import sett_1, app_servers
from Android_233.Scrpit.Operate import swipeDown, swip_downformadb

driver = sett_1()
time.sleep(3)
try:
        app_servers(driver=driver, select=2)  # 选择api环境 1=183 2=t 3=正式
except:
        pass
time.sleep(5)
menu().top(driver)
time.sleep(5)
swip_downformadb()


