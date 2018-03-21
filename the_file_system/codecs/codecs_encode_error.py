import codecs
import sys

error_handling = sys.argv[1]

text = 'français'

try:
    with codecs.open('encode_error.txt', 'w', encoding='ascii', errors=error_handling) as f:
        f.write(text)

except UnicodeEncodeError as err:
    print('Error:', err)

else:
    with open('encode_error.txt', 'rb') as f:
        print('file contents: {!r}'.format(f.read()))
