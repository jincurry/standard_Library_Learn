import signal
import os
import time

def received_signal(signum, stack):
    print('Received:', signum)

signal.signal(signal.SIGUSR1, received_signal)
signal.signal(signal.SIGUSR2, received_signal)

print('My PID is :', os.getpid())

while True:
    print('Waiting...')
    time.sleep(3)
