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

    try:
        cursor = conn1.cursor()
        cursor.execute("""
        DELETE  FROM project WHERE name = 'virtualenvwrapper'
        """)
        print('\nAfter delete:')
        show_projects(conn1)
        raise RuntimeError('simulated Error')
    except Exception as err:
        print('Error:', err)
        conn1.rollback()
    print('\nAfter rollback:')
    show_projects(conn1)
