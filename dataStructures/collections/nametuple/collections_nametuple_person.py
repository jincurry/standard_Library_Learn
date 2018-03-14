import collections

Person = collections.namedtuple('Person','name, age, sex')
Bob = Person(name='Bob', age=20, sex='male')
John = Person(name='John', age=21, sex='female')

for person in [Bob, John]:
    print('{} is a {} year old {}'.format(*person))
