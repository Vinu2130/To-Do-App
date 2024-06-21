import tkinter as tk
from tkinter import messagebox
from todoApp import add_task, remove_task, list_tasks, mark_done, mark_undone, load_todos

# Function to refresh the task list in the listbox
def refresh_task_list(listbox):
    listbox.delete(0, tk.END)  # Clear the current listbox content
    tasks = load_todos()
    if tasks is None:
        messagebox.showerror("Error", "Failed to load tasks.")
        return
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["done"] else "✗"
        listbox.insert(tk.END, f"{i}. {task['task']} [{status}]")

# Function to add a task from the GUI
def add_task_gui(entry, listbox):
    task = entry.get()
    if task:
        add_task(task)
        refresh_task_list(listbox)  # Refresh listbox after adding task
        entry.delete(0, tk.END)     # Clear entry widget after adding task
    else:
        messagebox.showwarning("Input Error", "Task cannot be empty")

# Function to mark a task as done from the GUI
def mark_done_gui(entry, listbox):
    task_number = entry.get()
    if task_number.isdigit():
        mark_done(int(task_number))
        refresh_task_list(listbox)  # Refresh listbox after marking task as done
        entry.delete(0, tk.END)     # Clear entry widget after marking task as done
    else:
        messagebox.showwarning("Input Error", "Invalid task number")

# Function to mark a task as undone from the GUI
def mark_undone_gui(entry, listbox):
    task_number = entry.get()
    if task_number.isdigit():
        mark_undone(int(task_number))
        refresh_task_list(listbox)  # Refresh listbox after marking task as undone
        entry.delete(0, tk.END)     # Clear entry widget after marking task as undone
    else:
        messagebox.showwarning("Input Error", "Invalid task number")

# Function to remove a task from the GUI
def remove_task_gui(entry, listbox):
    task_number = entry.get()
    if task_number.isdigit():
        remove_task(int(task_number))
        refresh_task_list(listbox)  # Refresh listbox after removing task
        entry.delete(0, tk.END)     # Clear entry widget after removing task
    else:
        messagebox.showwarning("Input Error", "Invalid task number")

# Function to display current tasks in a messagebox
def display_tasks(listbox):
    tasks = load_todos()
    if tasks is None:
        messagebox.showerror("Error", "Failed to load tasks.")
        return
    task_list = "\n".join([f"{i+1}. {task['task']}" for i, task in enumerate(tasks)])
    messagebox.showinfo("Current Tasks", task_list)

# Function to display help information
def show_help():
    help_text = (
        "To-Do List Application\n\n"
        "Commands:\n"
        "1. Add Task: Enter a task in the entry field and click 'Add Task'.\n"
        "2. Mark Done: Enter the task number in the entry field and click 'Mark Done'.\n"
        "3. Mark Undone: Enter the task number in the entry field and click 'Mark Undone'.\n"
        "4. Remove Task: Enter the task number in the entry field and click 'Remove Task'.\n"
        "5. Display Tasks: Click 'Display Tasks' to see the current tasks in a messagebox.\n"
    )
    messagebox.showinfo("Help", help_text)

# def clear_tasks_gui(listbox):
#     confirm = messagebox.askyesno("Confirm", "Are you sure you want to clear all tasks?")
#     if confirm:
#         clear_tasks()
#         refresh_task_list(listbox)



# Main function to set up the GUI
def main():
    root = tk.Tk()
    root.title("To-Do List")  # Set the title of the GUI window

    # Create a menu bar
    menubar = tk.Menu(root)
    root.config(menu=menubar)

    # Add Help menu
    help_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="Help", command=show_help)

    # Frame for task list and scrollbar
    frame = tk.Frame(root)
    frame.pack(pady=10)

    listbox = tk.Listbox(frame, width=70, height=10)
    listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
    scrollbar.config(command=listbox.yview)
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Frame for entry widget and action buttons
    entry_frame = tk.Frame(root)
    entry_frame.pack(pady=10)

    entry = tk.Entry(entry_frame, width=30)
    entry.pack(side=tk.LEFT, padx=5)

    add_button = tk.Button(entry_frame, text="Add Task", command=lambda: add_task_gui(entry, listbox))
    add_button.pack(side=tk.LEFT)

    done_button = tk.Button(entry_frame, text="Mark Done", command=lambda: mark_done_gui(entry, listbox))
    done_button.pack(side=tk.LEFT)

    undone_button = tk.Button(entry_frame, text="Mark Undone", command=lambda: mark_undone_gui(entry, listbox))
    undone_button.pack(side=tk.LEFT)

    remove_button = tk.Button(entry_frame, text="Remove Task", command=lambda: remove_task_gui(entry, listbox))
    remove_button.pack(side=tk.LEFT)

    display_button = tk.Button(root, text="Display Tasks", command=lambda: display_tasks(listbox))
    display_button.pack(pady=10)

    # clear_button = tk.Button(root, text="Clear Tasks", command=lambda: clear_tasks_gui(listbox))
    # clear_button.pack(pady=10)


    # Refresh task list on startup
    refresh_task_list(listbox)

    root.mainloop()

if __name__ == "__main__":
    main()
