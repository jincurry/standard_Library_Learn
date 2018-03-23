import sqlite3

db_filename = 'todo.db'


def show_projects(conn):
    cursor = conn.cursor()
    cursor.execute('select name, description from project')
    for name, desc in cursor.fetchall():
        print('',name)


with sqlite3.connect(db_filename) as conn1:
    print('Before changes:')
    show_projects(conn1)
    cursor1 = conn1.cursor()
    cursor1.execute("""
    insert INTO project (name, description, deadline)
    VALUES ('virtualenvwrapper', 'virtualenv extensions', '2018-01-01')
    """)

    print('\nAfter changes in conn1:')
    show_projects(conn1)

    print('\nBefore commit:')
    with sqlite3.connect(db_filename) as conn2:
        show_projects(conn2)

    conn1.commit()
    print('\nAfter commit:')
    with sqlite3.connect(db_filename) as conn3:
        show_projects(conn3)

