from collections import Counter

c = Counter('abcdaab')

for letter in 'abcde':
    print('{} : {}'.format(letter, c[letter]))
