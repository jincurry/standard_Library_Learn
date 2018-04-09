#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 18-4-9 下午2:04 
# @Author : jincurry 
# @Site : https://github.com/jincurry/standard_Library_Learn 
# @File : multiprocessing_sample.py
# @Software: PyCharm
import multiprocessing


def worker():
    print('worker')


if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker)
        jobs.append(p)
        p.start()
