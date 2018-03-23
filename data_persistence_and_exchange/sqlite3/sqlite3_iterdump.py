import sqlite3

schema_filename = 'todo_schema.sql'

with sqlite3.connect(':memory:') as conn:
    conn.row_factory = sqlite3.Row

    print('Creating schema')
    with open(schema_filename, 'rt') as f:
        schema = f.read()
        conn.executescript(schema)

    print('Inserting initial data')
    conn.execute("""
    insert INTO project (name, description, deadline)
    VALUES ('pymotw', 'Python Module fo the Week', '2018-12-01')
    """)
    data = [
        ('write about select', 'done', '2010-10-03', 'pymotw'),
        ('write about random', 'waiting', '2010-11-10', 'pymotw'),
        ('write about sqlite3', 'active', '2010-10-17', 'pymotw'),
    ]

    conn.executemany("""
    insert INTO task (details, status, deadline, project)
    VALUES (?, ?, ?, ?)
    """, data)

    print('Dumping:')
    for text in conn.iterdump():
        print(text)
