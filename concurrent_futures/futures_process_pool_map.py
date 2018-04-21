from concurrent import futures
import os


def task(n):
    return n, os.getpid()


ex = futures.ProcessPoolExecutor(max_workers=3)
results = ex.map(task, range(10, 0, -1))
for n, pid in results:
    print('ran task {} in process {}'.format(n, pid))
