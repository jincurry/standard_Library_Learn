import pathlib

# this file doesn't successfully run in my computer
# need to test in Linux system to see whether can run

p = pathlib.Path('example_link')
p.symlink_to('example.txt')

print(p)
print(p.resolve().name)
