import bz2

lorem = open('lorem.txt', 'rt').read().encode('utf-8')
compressed = bz2.compress(lorem)
combined = compressed + lorem

decompressor = bz2.BZ2Decompressor()
decompressed = decompressor.decompress(combined)

decompressed_matches = decompressed == lorem
print('let\'s see what contents in decompressed: \n{}'.format(decompressed))
print('Decompressed data matches lorem:', decompressed_matches)

unused_data = decompressor.unused_data == lorem
print('let\'s see what contents in unused: \n{}'.format(decompressor.unused_data))
print('Unused data matches lorem:', unused_data)
