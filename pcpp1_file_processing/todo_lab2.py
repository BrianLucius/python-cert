import sqlite3

class Todo:
    def __init__(self):
        self.conn =sqlite3.connect('/Users/brian/Repositories/python-cert/pcpp1_file_processing/todo.db')
        self.c = self.conn.cursor()
        self.create_task_table()
    
    def create_task_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        priority INTEGER NOT NULL);''')
        
    def add_task(self):
        name = ''
        while name == '':
            name = input('Enter task name: ')
            if self.find_task_by_name(name) is not None:
                print('Task already exists.')
                name = ''
        
        priority = 0
        while priority < 1:
            priority = int(input('Enter priority: '))
        
        self.c.execute('INSERT INTO tasks (name, priority) VALUES (?,?)', (name, priority))
        self.conn.commit()
    
    def display_tasks(self):
        for row in self.c.execute('SELECT * FROM tasks'):
            print(row)
    
    def find_task_by_name(self, task):
        self.c.execute("SELECT * FROM tasks WHERE name = ?", (task,))
        row = self.c.fetchone()
        if row == []:
            return None
        else:
            return row

    def find_task_by_id(self, id):
        self.c.execute("SELECT * FROM tasks WHERE id = ?", (id,))
        row = self.c.fetchone()
        if row == []:
            return None
        else:
            return row
    
    def change_priority(self):
        id = 0
        while id == 0:
            id = int(input('Enter task ID to change priority: '))
            if self.find_task_by_id(id) is None:
                print('Task id not found.')
                id = 0
        
        priority = 0
        while priority < 1:
            priority = int(input('Enter new priority: '))
        
        self.c.execute('UPDATE tasks SET priority=? WHERE id=?', (priority, id))
        self.conn.commit()
    
    def delete_task(self):
        id = 0
        while id == 0:
            id = int(input('Enter task ID to delete: '))
            if self.find_task_by_id(id) is None:
                print('Task id not found.')
                id = 0
        
        self.c.execute('DELETE FROM tasks WHERE id = ?', (id, ))
        self.conn.commit()
    
    def main_menu(self):
        selection = 0
        while selection < 1 or selection > 5:
            print('''\n1. Show Tasks\n2. Add Task\n3. Change Priority\n4. Delete Task\n5. Exit''')
            selection = int(input('Enter selection: '))
            print('')
            match selection:
                case 1:
                    self.display_tasks()
                case 2:
                    self.add_task()
                case 3:
                    self.change_priority()
                case 4:
                    self.delete_task()
                case 5:
                    return
            selection = 0
    
    def close_conn(self):
        self.conn.close()

app = Todo()
app.main_menu()
app.close_conn()

