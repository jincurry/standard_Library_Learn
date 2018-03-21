import codecs
import sys

error_handling = sys.argv[1]

text = 'français'
print('Original     :', text)

with codecs.open('decode_error.txt', mode='w', encoding='utf-16') as f:
    f.write(text)

with open('decode_error.txt', 'r', encoding='utf-8', errors=error_handling) as f:
    try:
        data = f.read()
    except UnicodeDecodeError as err:
        print('Error:', err)
    else:
        print('Read  :', repr(data))

