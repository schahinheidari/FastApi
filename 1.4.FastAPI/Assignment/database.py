import sqlite3
from datetime import datetime

conn = sqlite3.connect('todo.db', check_same_thread=False)
my_cursor = conn.cursor()

def add_task(title: str, description: str, status: int = 0):
    try:
        created_time = datetime.now().isoformat()
        my_cursor.execute(f"INSERT INTO todo (title, description, status, created_at) VALUES (?, ?, ?, ?)", (title, description, status, created_time))
        conn.commit()
        return my_cursor.lastrowid
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback()


def get_all_tasks():
    try:
        my_cursor.execute("SELECT * FROM todo")
        results = my_cursor.fetchall()
        return results
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return []

def find_task(task_id):
    try:
        my_cursor.execute(f"SELECT * FROM todo WHERE id = {task_id}")
        result = my_cursor.fetchone()
        return result
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None

def update_task(task_id, title, description, status):
    try:
        my_cursor.execute(f"UPDATE todo SET title = '{title}', description = '{description}', status = {status} WHERE id = {task_id}")
        conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback()

def delete_task(task_id):
    try:
        my_cursor.execute(f"DELETE FROM todo WHERE id = {task_id}")
        conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback()




