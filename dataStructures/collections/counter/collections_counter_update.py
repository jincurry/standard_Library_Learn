from collections import Counter

c = Counter()
print("Initial:", c)
c.update('awesome')
print('Sequences', c)
c.update({'a': 2, 'e': 2})
print("Dict:", c)
