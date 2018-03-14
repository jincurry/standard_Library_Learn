from collections import ChainMap

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}
m = ChainMap(a, b)
print(m.maps)
print('c={}'.format(m['c']))

# reverse the list
m.maps = list(reversed(m.maps))

print(m.maps)
print('c={}'.format(m['c']))

t = ChainMap(b,a)
print(t.maps)
print('c={}'.format(t['c']))