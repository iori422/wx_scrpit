# coding:utf-8
import os
import re
from selenium import webdriver
from appium import webdriver
import time
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    pass

@app.route('/login')
def login():
    pass

if __name__ == '__main__':
    app.run(debug=True)