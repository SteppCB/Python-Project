import sqlite3
import argparse
import sys
import re

# Initialize database
def initialize_db():
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            completed BOOLEAN NOT NULL CHECK (completed IN (0, 1))
        )
    """)
    conn.commit()
    conn.close()

# Add a new task
def add_task(description):
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (description, completed) VALUES (?, 0)", (description,))
    conn.commit()
    conn.close()
    print(f"Task added: {description}")

# List all tasks
def list_tasks(show_completed=False):
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    if show_completed:
        cursor.execute("SELECT id, description, completed FROM tasks")
    else:
        cursor.execute("SELECT id, description, completed FROM tasks WHERE completed = 0")
    tasks = cursor.fetchall()
    conn.close()
    
    if tasks:
        print("Your tasks:")
        for task in tasks:
            status = "Done" if task[2] else "Pending"
            print(f"[{task[0]}] {task[1]} - {status}")
    else:
        print("No tasks found.")

# Mark a task as completed
def complete_task(task_id):
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    print(f"Task {task_id} marked as completed.")

# Delete a task
def delete_task(task_id):
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    print(f"Task {task_id} deleted.")

# Command-line interface
def main():
    parser = argparse.ArgumentParser(description="A simple CLI Todo List Manager using SQLite.")
    parser.add_argument("-a", "--add", help="Add a new task. Provide a description.")
    parser.add_argument("-l", "--list", help="List tasks. Use 'all' to include completed tasks.", nargs="?", const="pending")
    parser.add_argument("-c", "--complete", help="Mark a task as completed. Provide the task ID.", type=int)
    parser.add_argument("-d", "--delete", help="Delete a task. Provide the task ID.", type=int)
    parser.add_argument("-h", "--help", action="help", help="Display this help message.")
    
    args = parser.parse_args()
    
    if args.add:
        if not re.match(r"\w+", args.add):
            print("Error: Task description must not be empty and should contain at least one word.")
            sys.exit(1)
        add_task(args.add)
    elif args.list:
        if args.list == "all":
            list_tasks(show_completed=True)
        else:
            list_tasks()
    elif args.complete:
        complete_task(args.complete)
    elif args.delete:
        delete_task(args.delete)
    else:
        parser.print_help()

if __name__ == "__main__":
    initialize_db()
    main()
