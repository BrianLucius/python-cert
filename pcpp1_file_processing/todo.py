import sqlite3

conn =sqlite3.connect('./pcpp1_file_processing/todo.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    priority INTEGER NOT NULL);''')
# c.execute('INSERT INTO tasks (name, priority) VALUES (?,?)', ('My first task', 1))
tasks = [
    ('My second task', 5),
    ('My third task', 10),
]
c.executemany('INSERT INTO tasks (name, priority) values (?,?)', tasks)
conn.commit()
conn.close()

