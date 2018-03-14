import contextlib

class Tracker:
    """Base class for noisy context managers"""

    def __init__(self, i):
        self.i = i

    def msg(self, s):
        print('     {}({}): {}'.format(
            self.__class__.__name__, self.i, s))

    def __enter__(self):
        self.msg('entering')


class HandleError(Tracker):
    """If an exception is received, treat it as handled."""

    def __exit__(self, *exc_details):
        received_exc = exc_details[1] is not None
        if received_exc:
            self.msg('handling exception {!r}'.format(
                exc_details[1]
            ))
        self.msg('exiting {}'.format(received_exc))
        return received_exc


class PassError(Tracker):
    """If an exception is received , propagate it."""

    def __exit__(self, *exc_details):
        received_exc = exc_details[1] is not None
        if received_exc:
            self.msg('passing exception {!r}'.format(
                exc_details[1]
            ))
        self.msg('exiting')
        return False


class ErrorOnExit(Tracker):
    """Cause an exception"""

    def __enter__(self):
        self.msg('throwing error on enter')
        raise RuntimeError('from {}'.format(self.i))

    def __exit__(self, *exc_info):
        self.msg('exiting')

class ErrorOnEnter(Tracker):
    "Cause an exception."

    def __enter__(self):
        self.msg('throwing error on enter')
        raise RuntimeError('from {}'.format(self.i))

    def __exit__(self, *exc_info):
        self.msg('exiting')
