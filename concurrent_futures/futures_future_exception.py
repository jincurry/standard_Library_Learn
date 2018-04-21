from concurrent import futures


def task(n):
    print('{}: starting'.format(n))
    if n == 5:
        raise ValueError('the value {} is no good'.format(n))
    print('{}: done'.format(n))
    return n / 10


ex = futures.ThreadPoolExecutor(max_workers=2)
print('main: starting')
# f = ex.submit(task, 5)
for i in range(6):
    f = ex.submit(task, i)
    error = f.exception()
    print('main: error: {}'.format(error))

    try:
        results = f.result()
    except ValueError as err:
        print('main: saw error "{}" when accessing result'.format(err))
    finally:
        print(results)