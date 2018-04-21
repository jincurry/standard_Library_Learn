from concurrent import futures
import time


def task(n):
    print('{}:sleeping'.format(n))
    time.sleep(0.5)
    print('{}: done'.format(n))
    return n/10


def done(fn):
    if fn.cancelled():
        print('{}: cancelled'.format(fn.arg))
    elif fn.done():
        error = fn.exception()
        if error:
            print('{}: error returned: {}'.format(fn.arg, error))
        else:
            result = fn.result()
            print('{}: value returned: {}'.format(fn.arg, result))


if __name__ == '__main__':
    ex = futures.ThreadPoolExecutor(max_workers=6)
    print('main: starting')
    tasks = []

    for i in range(10, 0, -1):
        print('main: submitting {}'.format(i))
        f = ex.submit(task, i)
        f.arg = i
        f.add_done_callback(done)
        tasks.append((i, f))

    for i, t in reversed(tasks):
        if not t.cancel():
            print('main: did not cancel {}'.format(i))

    ex.shutdown()
