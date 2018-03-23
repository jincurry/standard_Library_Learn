import sqlite3

db_filename = 'todo.db'

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()

    cursor.execute("""
    SELECT name, description, deadline from project
    WHERE name = 'pymotw'
    """)

    name, description, deadline = cursor.fetchone()
    print('Project details for {}({})\n due {}'.format(
        description, name, deadline
    ))

    cursor.execute("""
    select id, priority, details, status, deadline from task
    WHERE project = 'pymotw' ORDER BY deadline
    """)

    print('\nNext 5 tasks:')
    for row in cursor.fetchmany(5):
        task_id, priority, details, status, deadline = row
        print('{:2d}[{:d}] {:<25}[{:<8}]({})'.format(
            task_id, priority, details, status, deadline
        ))
