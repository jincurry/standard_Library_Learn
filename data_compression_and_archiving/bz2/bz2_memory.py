import bz2
import binascii

original_data = b'This is the original text.'
print('Original data : {}bytes.'.format(len(original_data)))

print(original_data)

print()
compressed_data = bz2.compress(original_data)
print('Compressed: {}bytes.'.format(len(compressed_data)))
hex_version = binascii.hexlify(compressed_data)
for i in range(len(hex_version) // 40 + 1):
    print(hex_version[i*40:(i+1)*40])

print()
decompressed = bz2.decompress(compressed_data)
print("Decompressed {}bytes.".format(len(decompressed)))
print(decompressed)
