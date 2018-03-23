import pickle
import sqlite3

db_filename = 'todo.db'


def adapter_func(obj):
    print('adapter_func({})\n'.format(obj))
    return pickle.dumps(obj)


def converter_func(data):
    print('converter_func({})\n'.format(data))
    return pickle.loads(data)


class MyObj:

    def __init__(self, arg):
        self.arg = arg

    def __str__(self):
        return 'MyObj({!r})'.format(self.arg)


sqlite3.register_adapter(MyObj,adapter_func)
sqlite3.register_converter("MyObj", converter_func)

to_save = [
    (MyObj('this is a value to save'),),
    (MyObj(42),),
]

with sqlite3.connect(db_filename, detect_types=sqlite3.PARSE_COLNAMES) as conn:
    conn.execute("""
    CREATE TABLE if NOT EXISTS obj2(
    id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    data text
    )
    """)
    cursor = conn.cursor()

    cursor.executemany("insert INTO obj2 (data) VALUES (?)", to_save)

    cursor.execute('SELECT id, data as "pickle [MyObj]" from obj2')
    for obj_id, obj in cursor.fetchall():
        print('Retrieved', obj_id, obj)
        print('with type', type(obj))
        print()

