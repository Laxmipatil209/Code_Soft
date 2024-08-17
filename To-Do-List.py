import tkinter as tk
from tkinter import messagebox

# Function to add a task to the to-do list
def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to remove a selected task from the to-do list
def remove_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")

# Function to delete all tasks from the to-do list
def delete_all_tasks():
    listbox.delete(0, tk.END)

# Function to exit the application
def exit_app():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create an Entry widget for adding tasks
entry = tk.Entry(root)
entry.pack(pady=10)

# Create a Listbox widget to display tasks
listbox = tk.Listbox(root)
listbox.pack()

# Create buttons for adding and removing tasks
add_button = tk.Button(root, text="Add Task", command=add_task)
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
delete_all_button = tk.Button(root, text="Delete All Tasks", command=delete_all_tasks)
exit_button = tk.Button(root, text="Exit", command=exit_app)

# Pack the buttons
add_button.pack(pady=5)
remove_button.pack(pady=5)
delete_all_button.pack(pady=5)
exit_button.pack(pady=5)

# Run the application
root.mainloop()
