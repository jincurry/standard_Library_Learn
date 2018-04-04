#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 18-4-4 下午2:51 
# @Author : jincurry 
# @Site : https://github.com/jincurry/standard_Library_Learn 
# @File : treading_subclass.py
# @Software: PyCharm

import threading
import logging


class MyThread(threading.Thread):

    def run(self):
        logging.debug('running')


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

for i in range(5):
    t = MyThread()
    t.start()
