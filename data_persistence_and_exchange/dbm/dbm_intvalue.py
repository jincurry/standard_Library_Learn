import dbm

with dbm.open('example.db', 'w') as db:
    try:
        db['one'] = 1
    except TypeError as err:
        print(err)
    try:
        db['two'] = b'2'
    except TypeError as err:
        print(err)

with dbm.open('example.db', 'r') as db:
    print('db["two"]=',db['two'])

