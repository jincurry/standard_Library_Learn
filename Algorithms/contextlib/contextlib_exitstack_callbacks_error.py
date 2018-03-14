import contextlib


def callback(*args, **kwargs):
    print('closing callback({}, {})'.format(args, kwargs))


try:
    with contextlib.ExitStack() as stack:
        stack.callback(callback, 'arg1', 'arg2', arg3='val')
        raise RuntimeError('thrown error')
except RuntimeError as err:
    print('Error: {}'.format(err))
