#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 18-4-4 下午2:55 
# @Author : jincurry 
# @Site : https://github.com/jincurry/standard_Library_Learn 
# @File : threading_timer.py
# @Software: PyCharm
import logging
import threading
import time


def delayed():
    logging.debug('worker running')


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s'
)

t1 = threading.Timer(0.3, delayed)
t1.setName('T1')
t2 = threading.Timer(0.3, delayed)
t2.setName('T2')

logging.debug('Starting timers')
t1.start()
t2.start()

logging.debug('waiting before conceling %s', t2.getName())
time.sleep(0.2)
logging.debug('canceling %s', t2.getName())
t2.cancel()
logging.debug('Done')
