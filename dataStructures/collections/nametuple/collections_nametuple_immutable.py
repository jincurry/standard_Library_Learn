from collections import namedtuple

Person = namedtuple('Person', 'name, age')

Bob = Person(name='Bob', age=12)

try:
    Bob.age = 21
except AttributeError as e:
    print('nametuple is not mutable\nthe reason is :', e)
else:
    print('nametple is mutable')