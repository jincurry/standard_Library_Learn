from collections import ChainMap

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

m = ChainMap(a, b)
print(m.maps)
print('Before:\n\tc={}'.format(m['c']))
m['c'] = 'E'
print(m.maps)
print('After:\n\tc={}'.format(m['c']))
