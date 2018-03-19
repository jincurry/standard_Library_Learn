import tempfile
import os

print('Building a filename with PID:')
filename = '/tmp/guess_my_name.{}.txt'.format(os.getpgid())
with open(filename, 'w+b') as temp:
    print('temp:')
    print('{!r}'.format(temp))
    print('temp.name:')
    print('{!r}'.format(temp.name))

os.remove(filename)
print()
print('Temporary Files:')
with tempfile.TemporaryFile() as temp:
    print('temp:')
    print('{!r}'.format(temp))
    print('temp.name:')
    print('{!r}'.format(temp.name))
