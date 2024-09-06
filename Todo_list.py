import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def remove_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except:
        messagebox.showwarning("Warning", "You must select a task to remove.")

# Set up the main window
root = tk.Tk()
root.title("To-Do List")

# Create and place widgets
entry_task = tk.Entry(root, width=50)
entry_task.pack(pady=10)

button_add = tk.Button(root, text="Add Task", command=add_task)
button_add.pack(pady=5)

listbox_tasks = tk.Listbox(root, width=50, height=10)
listbox_tasks.pack(pady=10)

button_remove = tk.Button(root, text="Remove Task", command=remove_task)
button_remove.pack(pady=5)

# Run the application
root.mainloop()
