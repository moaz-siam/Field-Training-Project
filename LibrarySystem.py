import tkinter as tk
from tkinter import messagebox
import os

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("قائمة المهام")
        self.root.geometry("400x400")
        self.tasks = []
        self.file_name = "tasks_ar.txt"  # File for saving tasks

        # Task listbox
        self.task_listbox = tk.Listbox(
            self.root,
            height=10,
            width=50,
            selectmode=tk.SINGLE,
            bg="#f7f7f7",
            fg="#333333",
            font=("Arial", 12),
            justify="right"  # Align text to the right
        )
        self.task_listbox.pack(pady=20)

        # Task entry field
        self.add_task_entry = tk.Entry(self.root, width=52, justify="right")
        self.add_task_entry.pack(pady=5)

        # Add Task button
        self.add_task_button = tk.Button(
            self.root,
            text="إضافة مهمة",
            width=20,
            bg="green",
            fg="white",
            command=self.add_task
        )
        self.add_task_button.pack(pady=5)

        # Remove Task button
        self.remove_task_button = tk.Button(
            self.root,
            text="حذف مهمة",
            width=20,
            bg="red",
            fg="white",
            command=self.remove_task
        )
        self.remove_task_button.pack(pady=5)

        # Update Task button
        self.update_task_button = tk.Button(
            self.root,
            text="تعديل مهمة",
            width=20,
            bg="blue",
            fg="white",
            command=self.update_task
        )
        self.update_task_button.pack(pady=5)

        # Load tasks from file at startup
        self.load_tasks_from_file()

        # Save tasks to file on exit
        self.root.protocol("WM_DELETE_WINDOW", self.on_exit)

    def add_task(self):
        task = self.add_task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.add_task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("خطأ في الإدخال", "يرجى إدخال مهمة.")

    def remove_task(self):
        selected_task = self.task_listbox.curselection()
        if selected_task:
            task = self.task_listbox.get(selected_task)
            self.tasks.remove(task)
            self.update_task_listbox()
        else:
            messagebox.showwarning("خطأ في الاختيار", "يرجى اختيار مهمة لحذفها.")

    def update_task(self):
        selected_task = self.task_listbox.curselection()
        if selected_task:
            task = self.task_listbox.get(selected_task)
            new_task = self.add_task_entry.get().strip()
            if new_task:
                self.tasks[self.tasks.index(task)] = new_task
                self.update_task_listbox()
                self.add_task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("خطأ في الإدخال", "يرجى إدخال الوصف الجديد للمهمة.")
        else:
            messagebox.showwarning("خطأ في الاختيار", "يرجى اختيار مهمة لتعديلها.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def load_tasks_from_file(self):
        """Load tasks from a file."""
        if os.path.exists(self.file_name):
            with open(self.file_name, "r", encoding="utf-8") as file:
                for line in file:
                    self.tasks.append(line.strip())
            self.update_task_listbox()

    def save_tasks_to_file(self):
        """Save tasks to a file."""
        with open(self.file_name, "w", encoding="utf-8") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def on_exit(self):
        """Handle saving tasks before application exits."""
        self.save_tasks_to_file()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
