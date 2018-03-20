import io

output = io.StringIO()
output.write('This goes into the buffer.')
print('And so does this.', file=output)

print(output.getvalue())

input = io.StringIO('Initial value for read buffer')

print(input.read())
