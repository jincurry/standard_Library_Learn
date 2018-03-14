from operator import *

a = -1
b = 5.0
c = [1, 2, 3]
d = ['a', 'b', 'c']

a = iadd(a, b)
print('a = iadd(a, b) ==>', a)
print()

c = iconcat(c, d)
print('c = iconcat(c, d) ==>', c)
