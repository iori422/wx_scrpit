#coding:utf-8
# -*- coding: utf-8 -*-
# @File  : run_mnst.py
# @Author: tutubuhaoci
# @Date  : 2017/12/15
# @Desc  :
import os
monkey=os.system('adb shell monkey -p com.example.examda --throttle 500 -v -v -v 10000 >c:\monkey.txt')
#quit_in = os.system('')

# staop =os.system('adb shell ps|grep monkey')
# os.system('kill ')

