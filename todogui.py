import tkinter as tk
from tkinter import messagebox

class ToDoList:
    def __init__(self, root):
        self.root = root
        self.tasks = []
        self.task_number = 0

        # Create GUI components
        self.task_list = tk.Listbox(self.root, width=40, height=10)
        self.task_list.pack(padx=10, pady=10)

        self.task_entry = tk.Entry(self.root, width=40)
        self.task_entry.pack(padx=10, pady=10)
       
        #button to add task
        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack(padx=10, pady=10)

        #button to delete task

        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(padx=10, pady=10)

        #button to update task

        self.update_button = tk.Button(self.root, text="Update Task", command=self.update_task)
        self.update_button.pack(padx=10, pady=10)

        #button to clear task
        self.clear_button = tk.Button(self.root, text="Clear All", command=self.clear_all)
        self.clear_button.pack(padx=10, pady=10)


    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.task_list.insert(self.task_number, task)
            self.task_number += 1
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter a task.")

    def delete_task(self):
        try:
            task_index = self.task_list.curselection()[0]
            self.task_list.delete(task_index)
            self.tasks.pop(task_index)
            self.task_number -= 1
        except IndexError:
            messagebox.showerror("Error", "Please select a task to delete.")

    def update_task(self):
        try:
            task_index = self.task_list.curselection()[0]
            new_task = self.task_entry.get()
            if new_task != "":
                self.tasks[task_index] = new_task
                self.task_list.delete(task_index)
                self.task_list.insert(task_index, new_task)
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Please enter a new task.")
        except IndexError:
            messagebox.showerror("Error", "Please select a task to update.")

    def clear_all(self):
        self.tasks = []
        self.task_list.delete(0, tk.END)
        self.task_number = 0

if __name__ == "__main__":
    root = tk.Tk()
    root.title("To-Do List")
    todo_list = ToDoList(root)
    root.mainloop()