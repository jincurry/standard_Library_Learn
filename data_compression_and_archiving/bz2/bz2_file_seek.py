import bz2
import io

with bz2.BZ2File('example.bz2', 'rb') as input:
    print('Entire file:')
    all_data  = input.read()
    print(all_data)

    expected = all_data[5:15]

    input.seek(0)
    input.seek(5)
    partial = input.read(10)
    print(partial)

    print()
    print(partial == expected)
