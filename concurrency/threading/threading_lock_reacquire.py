#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 18-4-4 下午3:39 
# @Author : jincurry 
# @Site : https://github.com/jincurry/standard_Library_Learn 
# @File : threading_lock_reacquire.py
# @Software: PyCharm
import threading

lock = threading.Lock()

print('First try:', lock.acquire())
print('Second try:', lock.acquire(0))
