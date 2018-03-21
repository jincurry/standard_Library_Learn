import codecs
from codecs_to_hex import to_hex

with open('nonnative-encoded.txt', mode='rb') as f:
    raw_bytes = f.read()

print('Raw:', to_hex(raw_bytes, 2))

with codecs.open('nonnative-encoded.txt', mode='r', encoding='utf-16') as f:
    decoded_text = f.read()

print('Decoded text :', repr(decoded_text))
