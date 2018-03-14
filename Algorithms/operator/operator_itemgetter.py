from operator import *

l = [dict(val=-1 * i) for i in range(4)]
print('Dictionaries:')
print(' original:', l)
g = itemgetter('val')
vals = [g(i) for i in l]
print(' values:', vals)
print(' sorted:', sorted(l, key=g))

print()
l = [(i, i * -2) for i in range(4)]
print('\nTuples:')
print(' original:', l)
g = itemgetter(1)
k = itemgetter(0)
vals = [g(i) for i in l]
vals_2 = [k(i) for i in l]
print('keys:', vals_2)
print('Sorted:',sorted(l, key=k))
print('values:', vals)
print('sorted:', sorted(l, key=g))
