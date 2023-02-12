import sqlite3

conn = sqlite3.connect('/Users/brian/Repositories/python-cert/pcpp1_file_processing/todo.db')
c = conn.cursor()
c.execute('UPDATE tasks SET priority = ? WHERE id = ?', (20, 1))
conn.commit()
conn.close()