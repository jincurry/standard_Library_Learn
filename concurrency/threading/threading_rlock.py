#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 18-4-4 下午3:41 
# @Author : jincurry 
# @Site : https://github.com/jincurry/standard_Library_Learn 
# @File : threading_rlock.py
# @Software: PyCharm
import threading

lock = threading.RLock()
print('First try:', lock.acquire())
print('Second try:', lock.acquire())