from operator import *

a = [1, 2, 3]
b = ['a', 'b', 'c']

print('a = ', a)
print('b = ', b)

print('\nConstructive:')
print(' concat(a, b):', concat(a, b))

print('\nSearching:')
print(' contains(a, 1):', contains(a, 1))
print(' contains(b, "b"):', contains(b, 'b'))
print(" countOf(a, 1):", countOf(a, 1))
print(' countOf(b, "b"):', countOf(b, 'b'))
print(' indexOf(a, 1):', indexOf(a, 1))

print('\nAccess Items:')
print(' getitem(b,1)        :', getitem(b, 1))
print(' getitem(b, slice(1, 3))     :', getitem(b, slice(1, 3)))
print(' setitem(b, 1, "d")      :', end=' ')
setitem(b, 1, "d")
print(b)

print(' setitem(a, slice(1, 3), [4, 5]      :', end=' ')
setitem(a, slice(1, 3), [4, 5])
print(a)

print('\nDestructive:')
print(' delitem(b, 1)       :', end=' ')
delitem(b, 1)
print(b)
print(' delitem(a, slice(1, 3):', end=' ')
delitem(a, slice(1, 3))
print(a)