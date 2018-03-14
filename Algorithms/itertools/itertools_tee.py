from itertools import tee, islice, count

r = islice(count(), 5)
print(r)
i1, i2 = tee(r)

print('i1:', list(i1))
print('i2:', list(i2))
