import io
import pickle
import pprint


class SimpleObject:

    def __init__(self, name):
        self.name = name
        self.name_backwards = name[::-1]
        return


data = []
data.append(SimpleObject('pickle'))
data.append(SimpleObject('preserve'))
data.append(SimpleObject('last'))

out_s = io.BytesIO()
for o in data:
    print('Waring : {} ({})'.format(o.name, o.name_backwards))
    pickle.dump(o, out_s)
    out_s.flush()

in_s = io.BytesIO(out_s.getvalue())

while True:
    try:
        o = pickle.load(in_s)
    except EOFError:
        break
    else:
        print('Read : {}({})'.format(o.name, o.name_backwards))
