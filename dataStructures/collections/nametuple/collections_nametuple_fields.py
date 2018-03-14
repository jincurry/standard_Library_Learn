from collections import namedtuple

Person = namedtuple('Person', 'name, age')
Bob = Person(name='Bob', age=12)
print(Bob._fields)
print('presentation:', Bob)
