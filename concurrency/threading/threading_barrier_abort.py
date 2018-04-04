#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 18-4-4 下午4:03 
# @Author : jincurry 
# @Site : https://github.com/jincurry/standard_Library_Learn 
# @File : threading_barrier_abort.py
# @Software: PyCharm
import threading
import time


def worker(barrier):
    print(threading.current_thread().name,
          'waiting for barrier with {} others'.format(
              barrier.n_waiting
          ))
    try:
        worker_id = barrier.wait()
    except threading.BrokenBarrierError:
        print(threading.current_thread().name, 'aborting')
    else:
        print(threading.current_thread().name, 'after barrier',
          worker_id)


NUM_THREADS = 3

barrier = threading.Barrier(NUM_THREADS + 1)

threads = [
    threading.Thread(
        name='worker-%s' % i,
        target=worker,
        args=(barrier,),
    )
    for i in range(NUM_THREADS)
]

for t in threads:
    print(t.name, 'starting')
    t.start()
    time.sleep(0.1)

barrier.abort()

for t in threads:
    t.join()