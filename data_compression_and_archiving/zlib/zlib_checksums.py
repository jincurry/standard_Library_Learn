import zlib

data = open('lorem.txt', 'rb').read()

cksums = zlib.adler32(data)

print('Adler32: {:12d}'.format(cksums))
print('     :{:12d}'.format(zlib.adler32(data, cksums)))

cksums = zlib.crc32(data)
print('CRC-32: {:12d}'.format(cksums))
print('     :{:12d}'.format(zlib.adler32(data, cksums)))
