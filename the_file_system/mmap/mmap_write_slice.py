import mmap
import shutil

shutil.copy('lorem.txt', 'lorem_copy.txt')

word = b'consectetuer'

reversed = word[::-1]
print('Looking for  :', word)
print('Replacing with   :', reversed)

with open('lorem_copy.txt', 'r+') as f:
    with mmap.mmap(f.fileno(), 0) as m:
        print('Before   :\n{!r}'.format(m.readline().rstrip()))
        m.seek(0)

        loc = m.find(word)
        m[loc:loc+ len(word)] = reversed
        m.flush()

        m.seek(0)
        print('After    :\n{!r}'.format(m.readline().rstrip()))

        f.seek(0)
        print('File :\n{!r}'.format(f.readline().rstrip()))
