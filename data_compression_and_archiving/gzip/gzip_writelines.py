import gzip
import io
import itertools
import os

with gzip.open('example_lines.txt.gz', 'wb') as output:
    with io.TextIOWrapper(output, encoding='utf-8') as enc:
        enc.writelines(
            itertools.repeat('The same line, over and over.\n',
                             10)
        )

# this file doesn't run successfully in my laptop which run linux system.
# the hint is con't find gzcat.
os.system('gzcat example_lines.txt.gz')
