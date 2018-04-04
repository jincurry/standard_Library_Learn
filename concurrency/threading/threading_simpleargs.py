#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 18-4-4 下午2:27 
# @Author : jincurry
# @Site :  
# @File : threading_simpleargs.py
# @Software: PyCharm

import threading


def worker(num, greeting):
    print('worker: %s, %s' %(num, greeting))


threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i, 'hello'))
    threads.append(t)
    t.start()
