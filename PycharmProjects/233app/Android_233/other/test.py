#coding:utf-8
import random


class A(object):
    def __init__(self,name):
        self.name=name
    def getName(self):
        return 'A'+self.name
# class B(A):
#     def getName(self):
#         return 'B'+self.name
#
# if __name__ == '__main__':
#     b = B('hello')
#     print b.getName()

# kuku = "['FRD-AL00\\n']"
# kuku = kuku.replace('\r','').replace('\n','').replace('\t','')
# kuku = re.findall(r'\w', kuku[0])[0]
# print kuku
# class Washer:
#     def __init__(self):
#         self.water = 0
#         self.scour = 0
#     def add_water(self, water):
#         print('Add water:', water)
#         self.water = water
#     def add_scour(self, scour):
#         self.scour = scour
#         print('Add scour:', self.scour)
#     def start_wash(self):
#         print('Start wash...')
#
#
# w = Washer()
# w.start_wash()
#
#
# class Washer:
#
#     @staticmethod
#     def set_water(self, water):
#         self.water = water
#     @staticmethod
#     def set_scour(self, scour):
#         self.scour = scour
#     def add_water(self):
#         print('Add water:', self.water)
#     def add_scour(self):
#         print('Add scour:', self.scour)
#     def start_wash(self):
#         self.add_water()
#         self.add_scour()
#         print('Start wash...')
#
# if __name__ == '__main__':
#     w = Washer()
#     w.start_wash()

# print json.dumps({'a': 'Runoob', 'b': 7}, sort_keys=True, indent=4, separators=(',', ': '))


import time
from appium import webdriver

# desired_caps = {}
# desired_caps['deviceName'] = ''  # 通过adb devices -l查看设备标识#WTKDU16A17013707 #Q4JNPVO7CY7DAM6L
# desired_caps['platformName'] = 'Android'
# desired_caps['browserName'] = ''
# desired_caps['platformVersion'] = 'Y13'
# #desired_caps['app'] = PATH('E:/Android233_vs/Android2.6.2.apk')#这里手动把app装到手机里，就注释点即可，如果打开，会根据路径安装app
# desired_caps['appPackage'] = 'com.example.examda'  # app的包名，具体这块还不是很了解
# desired_caps['appActivity'] = 'com.example.examda.activity.E01_AccessActivity'  # 打开应用的第一个Activity，具体不了解
# time.sleep(3)
# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 连接设备并打开应用app
# time.sleep(15)
# driver.quit()
# a = ['1','2','3','5']
# t = random.choice(a)
# # print t
# a = '/1'
# a1 =a[1:]
# print a1
# class aaaa():
#     @classmethod
#     def aaa1(self,a1):
#         print a1
#     def aaa2(self,a1):
#         print self.aaa1(a1=a1)
#
# a1 =233
# #aaaa().aaa1(a1)
# aaaa().aaa2(a1)
# cc="2222"
# print "11111111111111111111  "+cc

a = ['1','2','3']
for i in range(1,4):
    c = random.choice(a)
    print i,c