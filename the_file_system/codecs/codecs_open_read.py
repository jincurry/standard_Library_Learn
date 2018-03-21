import codecs
import sys

encoding = sys.argv[1]
filename = encoding + '.txt'

print('Reading from:', filename)
with codecs.open(filename, mode='r', encoding=encoding) as f:
    t = f.read()
    print(repr(t))
