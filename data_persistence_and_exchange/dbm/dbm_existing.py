import dbm

with dbm.open('example.db', 'r') as db:
    print('key():', db.keys())
    for k in db.keys():
        print('iterating:', k, db[k])
    print('db["author"]=', db['author'])
