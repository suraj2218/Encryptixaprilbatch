import tkinter as tk
from tkinter import ttk, messagebox
import os

# File to store tasks
TASKS_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from file"""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            tasks = file.readlines()
            for task in tasks:
                task_list.insert(tk.END, task.strip())

def save_tasks():
    """Save tasks to file"""
    with open(TASKS_FILE, "w") as file:
        tasks = task_list.get(0, tk.END)
        for task in tasks:
            file.write(task + "\n")

def add_task():
    """Add a new task"""
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    """Delete selected task"""
    try:
        selected_task = task_list.curselection()[0]
        task_list.delete(selected_task)
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def clear_tasks():
    """Clear all tasks"""
    task_list.delete(0, tk.END)
    save_tasks()

def mark_done():
    """Mark selected task as done"""
    try:
        selected_task = task_list.curselection()[0]
        task = task_list.get(selected_task)
        task_list.delete(selected_task)
        task_list.insert(tk.END, f"✔ {task}")
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as done!")

def move_up():
    """Move selected task up"""
    try:
        selected_task = task_list.curselection()[0]
        if selected_task > 0:
            task = task_list.get(selected_task)
            task_list.delete(selected_task)
            task_list.insert(selected_task - 1, task)
            task_list.selection_set(selected_task - 1)
            save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to move up!")

def move_down():
    """Move selected task down"""
    try:
        selected_task = task_list.curselection()[0]
        if selected_task < task_list.size() - 1:
            task = task_list.get(selected_task)
            task_list.delete(selected_task)
            task_list.insert(selected_task + 1, task)
            task_list.selection_set(selected_task + 1)
            save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to move down!")

def show_info():
    """Show project information"""
    messagebox.showinfo("About", "A To-Do List application is a useful project that helps users manage and organize their tasks efficiently. This project aims to create a command-line or GUI-based application using Python, allowing users to create, update, and track their to-do list.")

# GUI Setup
root = tk.Tk()
root.title("To-Do List")
root.geometry("450x600")
root.configure(bg="#2C3E50")  # Dark Background

# Styling
style = ttk.Style()
style.configure("TButton", font=("Arial", 10, "bold"), padding=5)
style.configure("TLabel", font=("Arial", 12, "bold"), background="#2C3E50", foreground="white")
style.configure("TEntry", font=("Arial", 12))

# Title Label
title_label = ttk.Label(root, text="To-Do List", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

# Info Button
info_button = ttk.Button(root, text="ℹ About", command=show_info)
info_button.pack(pady=5)

# Input Frame
frame = tk.Frame(root, bg="#2C3E50")
frame.pack(pady=10)

task_entry = ttk.Entry(frame, width=35)
task_entry.pack(side=tk.LEFT, padx=10)

add_button = ttk.Button(frame, text="Add Task", command=add_task)
add_button.pack(side=tk.RIGHT)

# Task List with Scrollbar
list_frame = tk.Frame(root, bg="#2C3E50")
list_frame.pack(pady=10)

task_list = tk.Listbox(list_frame, width=50, height=15, font=("Arial", 12), bg="#34495E", fg="white", selectbackground="#1ABC9C")
scrollbar = ttk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
task_list.pack(side=tk.LEFT)

# Linking Scrollbar
task_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_list.yview)

# Buttons Frame
buttons_frame = tk.Frame(root, bg="#2C3E50")
buttons_frame.pack(pady=10)

mark_done_button = ttk.Button(buttons_frame, text="✔ Mark Done", command=mark_done)
delete_button = ttk.Button(buttons_frame, text="🗑 Delete", command=delete_task)
clear_button = ttk.Button(buttons_frame, text="❌ Clear All", command=clear_tasks)
up_button = ttk.Button(buttons_frame, text="⬆ Move Up", command=move_up)
down_button = ttk.Button(buttons_frame, text="⬇ Move Down", command=move_down)

mark_done_button.grid(row=0, column=0, padx=5, pady=5)
delete_button.grid(row=0, column=1, padx=5, pady=5)
clear_button.grid(row=0, column=2, padx=5, pady=5)
up_button.grid(row=1, column=0, padx=5, pady=5)
down_button.grid(row=1, column=1, padx=5, pady=5)

# Load tasks on startup
load_tasks()

# Run the app
root.mainloop()

