import array
import binascii

s = b'this is the array.'
a = array.array('b', s)

print('As byte string:', s)
print('As array     :', a)
print('As hex       :', binascii.hexlify(a))
