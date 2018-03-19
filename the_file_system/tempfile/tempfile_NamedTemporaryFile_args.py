import tempfile
import pathlib

dir = pathlib.Path('.')
with tempfile.NamedTemporaryFile(suffix='_suffix',
                                 prefix='prefix_',
                                 dir=dir) as temp:
    print('temp:')
    print(' ', temp)
    print('temp.name:')
    print(' ', temp.name)
