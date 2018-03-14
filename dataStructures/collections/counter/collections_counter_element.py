from collections import Counter

c = Counter('extremely')
c['z'] = 0
print(c)
print(list(c.elements()))
