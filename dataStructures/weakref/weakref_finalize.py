import weakref


class ExpensiveObj:
    def __del__(self):
        print('Deleting {}'.format(self))


def on_finalize(*args):
    print('on_finalize({!r})'.format(args))

obj = ExpensiveObj()
weakref.finalize(obj, on_finalize, 'extra argument')

del obj
