import collections

try:
    Person = collections.namedtuple('Person', 'name, age, class')
except ValueError as err:
    print(err)

try:
    Person = collections.namedtuple('Person', 'name, age, age')
except ValueError as err:
    print(err)

Person = collections.namedtuple('person', 'name, age')

try:
    Bob = Person(name='Bob', age=12)
except ValueError as e:
    print('error!', e)
else:
    print('{} is {} year old'.format(*Bob))
