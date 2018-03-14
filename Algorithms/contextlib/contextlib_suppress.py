import contextlib


class NonFatalError(Exception):
    pass


class FatalError(Exception):
    pass


def non_idempotent_operation():
    raise NonFatalError(
        'The operation failed because of exising state'
    )


def fatal_operation():
    raise FatalError(
        'the operation is fatal!!!'
    )

# with contextlib.suppress(NonFatalError, FatalError):
# with contextlib.suppress((NonFatalError, FatalError)):
# also are available statement
with contextlib.suppress(*[NonFatalError, FatalError]):
    print('Trying non-idempotent operation')
    non_idempotent_operation()
    fatal_operation()
    print('succeeded!!')
print('done')
