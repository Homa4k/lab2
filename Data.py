import sqlite3
from datetime import datetime
DB_NAME = "tasks.db"


class DatabaseManager:
    def __init__(self, db_name=DB_NAME):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL,
        column INTEGER NOT NULL,
        created_at TEXT NOT NULL)
        """
        self.conn.execute(query)
        self.conn.commit()

    def add_task(self, description, column):
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        query = "INSERT INTO tasks (description, column, created_at) VALUES (?, ?, ?)"
        cur = self.conn.cursor()
        cur.execute(query, (description, column, created_at))
        self.conn.commit()
        return cur.lastrowid, created_at

    def update_task_column(self, task_id, column):
        query = "UPDATE tasks SET column = ? WHERE id = ?"
        self.conn.execute(query, (column, task_id))
        self.conn.commit()

    def update_task_description(self, task_id, new_description):
        query = "UPDATE tasks SET description = ? WHERE id = ?"
        self.conn.execute(query, (new_description, task_id))
        self.conn.commit()

    def delete_task(self, task_id):
        query = "DELETE FROM tasks WHERE id = ?"
        self.conn.execute(query, (task_id,))
        self.conn.commit()

    def fetch_tasks(self):
        query = "SELECT id, description, column, created_at FROM tasks"
        cur = self.conn.cursor()
        cur.execute(query)
        return cur.fetchall()
