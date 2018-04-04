import signal
import os
import time

def do_exit(sig, stack):
    raise SystemExit('Exiting')

signal.signal(signal.SIG_IGN, signal.SIG_IGN)
signal.signal(signal.SIGUSR1, do_exit)

print('My Pid:', os.getpid())

signal.pause()
