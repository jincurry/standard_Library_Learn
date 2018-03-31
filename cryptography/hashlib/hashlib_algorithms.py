import hashlib

print('Guaranteed:\n{}\n'.format(
    ','.join(hashlib.algorithms_guaranteed)
))

print('Available:\n{}\n'.format(
    ','.join(hashlib.algorithms_available)
))
