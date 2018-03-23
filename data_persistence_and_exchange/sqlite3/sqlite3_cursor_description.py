import sqlite3

db_filename = 'todo.db'

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()

    cursor.execute("""
    select * from task WHERE project ='pymotw'
    """)

    print('Task table has these columns')
    for colinfo in cursor.description:
        print(colinfo)
