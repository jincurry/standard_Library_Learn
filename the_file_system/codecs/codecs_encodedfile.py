from codecs_to_hex import to_hex

import codecs
import io

data = 'français'

utf8 = data.encode('utf-8')
print("Start as UTF-8:", to_hex(utf8, 1))

output = io.BytesIO()

encoded_file = codecs.EncodedFile(output, data_encoding='utf-8', file_encoding='utf-16')
encoded_file.write(utf8)

utf16 = output.getvalue()
print('Encoded to UTF-16:   ', to_hex(utf16, 2))

buffer = io.BytesIO(utf16)
encoded_file = codecs.EncodedFile(buffer, data_encoding='utf-8', file_encoding='utf-16')
recoded = encoded_file.read()
print('Back to UTF-8:   ', to_hex(recoded, 1))
