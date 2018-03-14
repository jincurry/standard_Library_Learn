import contextlib


@contextlib.contextmanager
def make_context():
    print(' entering')
    try:
        yield {}
    except RuntimeError as err:
        print(' ERROR:', err)
    finally:
        print(' exiting')


print('Normal:')
with make_context() as value:
    print(' inside with statement:', value)

print('\nHandled error:')
with make_context() as value:
    raise RuntimeError('Showing example of handling an error')

print('\nUnhandled error:')
with make_context() as value:
    raise ValueError('This exception is not handled')
