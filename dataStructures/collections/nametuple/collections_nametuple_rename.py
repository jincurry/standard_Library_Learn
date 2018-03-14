from collections import namedtuple

with_class = namedtuple('Person', 'name, class, age', rename=True)
print(with_class._fields)

two_age = namedtuple('Person', 'name, age, age', rename=True)
print(two_age._fields)
