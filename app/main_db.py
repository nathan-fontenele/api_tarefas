import sqlite3

class MainDB:
    def __init__(self):
        self.conn = sqlite3.connect('meubanco.db')
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT NOT NULL,
                                description TEXT NOT NULL)''')
        self.conn.commit()

    def insert_task(self, name, description):
        self.cursor.execute("INSERT INTO tasks (name, description) VALUES (?, ?)", (name, description))
        self.conn.commit()

    def fetch_data(self):
        self.cursor.execute("SELECT * FROM tasks")
        tasks = self.cursor.fetchall()
        return tasks
    
    def update_task(self, id, name, description):
        self.cursor.execute("UPDATE tasks SET name=?, description=? WHERE id=?", (name, description, id))
        self.conn.commit()
        return {'message': 'Task updated successfully!'}, 200
    
    def delete_task(self, id):
        
        if not self.cursor.execute("SELECT * FROM tasks WHERE id=?", (id,)).fetchall():
            return {'message': 'Task not found!'}, 404
        
        self.cursor.execute("DELETE FROM tasks WHERE id=?", (id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
