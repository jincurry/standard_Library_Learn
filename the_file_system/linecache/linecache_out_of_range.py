import linecache
from linecache_data import *

filename = make_tempfile()

not_there = linecache.getline(filename, 500)
print('NOT THERE: {!r} includes {} characters.'.format(
    not_there, len(not_there)
))

cleanup(filename)
