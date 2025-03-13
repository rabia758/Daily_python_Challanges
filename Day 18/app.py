import tkinter as tk
from tkinter import messagebox

# Function to add a task
def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

# Function to mark a task as completed
def mark_completed():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(selected_task_index)
        listbox_tasks.delete(selected_task_index)
        listbox_tasks.insert(selected_task_index, f"✔ {task}")
        listbox_tasks.itemconfig(selected_task_index, {'fg': 'gray'})
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as completed!")

# Function to delete a task
def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

# Function to save tasks to a file
def save_tasks():
    tasks = listbox_tasks.get(0, tk.END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Function to load tasks from a file
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for task in file.readlines():
                listbox_tasks.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass

# Create the main window
root = tk.Tk()
root.title("To-Do List App")

# Create a frame for the task list
frame_tasks = tk.Frame(root)
frame_tasks.pack(pady=10)

# Create a Listbox to display tasks
listbox_tasks = tk.Listbox(frame_tasks, width=50, height=10, font=("Arial", 12))
listbox_tasks.pack(side=tk.LEFT, fill=tk.BOTH)

# Create a scrollbar for the Listbox
scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.BOTH)

# Attach the scrollbar to the Listbox
listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

# Create an entry widget to add tasks
entry_task = tk.Entry(root, width=50, font=("Arial", 12))
entry_task.pack(pady=10)

# Create buttons for adding, marking, and deleting tasks
button_add = tk.Button(root, text="Add Task", width=48, command=add_task)
button_add.pack(pady=5)

button_mark = tk.Button(root, text="Mark Completed", width=48, command=mark_completed)
button_mark.pack(pady=5)

button_delete = tk.Button(root, text="Delete Task", width=48, command=delete_task)
button_delete.pack(pady=5)

# Load tasks from the file when the app starts
load_tasks()

# Start the main event loop
root.mainloop()
