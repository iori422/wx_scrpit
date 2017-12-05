#coding:utf-8
import os
import sys
from time import sleep

monkey=os.system('adb shell monkey -p com.example.examda --throttle 500 -v -v -v 10000 >c:\monkey.txt')
#quit_in = os.system('')


