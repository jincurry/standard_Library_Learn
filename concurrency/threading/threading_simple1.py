#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 18-4-4 下午2:23 
# @Author : Aries 
# @Site :  
# @File : threading_simple1.py.py 
# @Software: PyCharm

import threading


def worker():
    print('Working', threading.current_thread())


threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()
