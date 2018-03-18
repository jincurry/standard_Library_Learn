import pathlib

# this file doesn't support windows system
# I will try it on linux system

p = pathlib.Path(__file__)

print('{} is owned by {}/{}.'.format(p, p.owner(), p.group()))
