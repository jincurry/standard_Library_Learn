from codecs_to_hex import to_hex

import codecs
import sys

encoding = sys.argv[1]
filename = encoding + '.txt'

print('writing to >', filename)
with codecs.open(filename, mode='w', encoding=encoding) as f:
    f.write('français')


nbytes = {
    'utf-8': 1,
    'utf-16': 2,
    'utf-32': 4,
}.get(encoding, 1)


print('File contents:')
with open(filename, mode='rb') as f:
    print(to_hex(f.read(), nbytes))
