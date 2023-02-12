import sqlite3

conn = sqlite3.connect('/Users/brian/Repositories/python-cert/pcpp1_file_processing/todo.db')
c = conn.cursor()
c.execute('DELETE FROM tasks WHERE id = ?', (6,))
conn.commit()
conn.close()