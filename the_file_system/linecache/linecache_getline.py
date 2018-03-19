import linecache
from linecache_data import *

filename = make_tempfile()

print('SOURCES:')
print('{!r}'.format(lorem.split('\n')[4]))
print()
print('CACHE:')
print('{!r}'.format(linecache.getline(filename, 5)))
