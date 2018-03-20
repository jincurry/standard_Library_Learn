import io
output = io.BytesIO()
wrapper = io.TextIOWrapper(
    output,encoding='utf-8', write_through=True,
)
wrapper.write('This goes into the buffer.')
wrapper.write('ÁÇÊ')

print(output.getvalue())

output.close()

input = io.BytesIO(
    b'Initial value for read buffer with unicode character' + ' ÁÇÊ'.encode('utf-8')
)

wrapper = io.TextIOWrapper(input, encoding='utf-8')

print(wrapper.read())
