# This file contains the core logic for managing the to-do list.

import json
from pathlib import Path

todo_file = Path.home() / ".todoApp.json"

# a function to load the to-do list from the JSON file.
def load_todos():
    try:
        if todo_file.exists():
            with open(todo_file, "r") as file:
                return json.load(file)
        else:
            return []
    except Exception as e:
        print(f"Error loading tasks: {e}")
        return None

# a function to save the to-do list to the JSON file.
def save_todos(todos):
    with open(todo_file, "w") as file:
        json.dump(todos, file)  # Writes the list as JSON to the file.

# a function to add a new task.
def add_task(task):
    todos = load_todos()  # Loads the current to-do list.
    todos.append({"task": task, "done": False})  # Appends a new task dictionary to the list.
    save_todos(todos)  # Saves the updated to-do list.

# a function to remove a task.
def remove_task(task_index):
    todos = load_todos()
    if 0 < task_index <= len(todos):
        todos.pop(task_index - 1)
        save_todos(todos)
    else:
        print("Invalid task index")

# a function to list all tasks.
def list_tasks():
    todos = load_todos()
    for i, todo in enumerate(todos, 1):  # Iterates over the to-do list with index starting at 1.
        status = "✓" if todo["done"] else "✗"
        print(f"{i}. {todo['task']} [{status}]")

# a function to mark a task as done.
def mark_done(task_number):
    todos = load_todos()
    if 0 < task_number <= len(todos):
        todos[task_number - 1]["done"] = True
        save_todos(todos)
    else:
        print("Invalid task number")

# a function to mark a task as undone.
def mark_undone(task_number):
    todos = load_todos()
    if 0 < task_number <= len(todos):
        todos[task_number - 1]["done"] = False
        save_todos(todos)
    else:
        print("Invalid task number")

# # a function to clear all tasks
# def clear_tasks():
#     confirm = input("Are you sure you want to clear all tasks? (yes/no): ").lower()
#     if confirm == 'yes':
#         todos = []
#         save_todos(todos)
#         print("All tasks cleared.")
#     else:
#         print("Clear operation canceled.")
