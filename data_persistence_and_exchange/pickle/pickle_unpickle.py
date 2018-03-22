import pickle
import pprint

data1 = [{'a': 'A', 'b': 2, 'c': 3.0}]

print('Before:', end=' ')
pprint.pprint(data1)

data1_string = pickle.dumps(data1)

data2 = pickle.loads(data1_string)
print('After:', end=' ')
pprint.pprint(data2)

print('Same?:', data1 is data2)
print('Equal?:', data1 == data2)
