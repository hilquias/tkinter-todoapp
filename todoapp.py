#!/usr/bin/env python3
"""A small in-memory todo list with a Tkinter interface."""

import tkinter as tk
from tkinter import ttk


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo List")
        self.root.minsize(360, 280)
        self.todos = []

        main = ttk.Frame(root, padding=16)
        main.pack(fill="both", expand=True)

        ttk.Label(main, text="My tasks", font=("TkDefaultFont", 16, "bold")).pack(
            anchor="w", pady=(0, 12)
        )

        add_row = ttk.Frame(main)
        add_row.pack(fill="x", pady=(0, 12))
        self.task_entry = ttk.Entry(add_row)
        self.task_entry.pack(side="left", fill="x", expand=True)
        self.task_entry.bind("<Return>", self.add_task)
        ttk.Button(add_row, text="Add", command=self.add_task).pack(
            side="left", padx=(8, 0)
        )

        list_frame = ttk.Frame(main)
        list_frame.pack(fill="both", expand=True)
        self.task_list = tk.Listbox(
            list_frame, activestyle="none", selectmode="browse", height=8
        )
        self.task_list.pack(side="left", fill="both", expand=True)
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.task_list.yview)
        scrollbar.pack(side="right", fill="y")
        self.task_list.configure(yscrollcommand=scrollbar.set)
        self.task_list.bind("<Double-Button-1>", self.toggle_done)

        actions = ttk.Frame(main)
        actions.pack(fill="x", pady=(12, 0))
        ttk.Button(actions, text="Mark done / undo", command=self.toggle_done).pack(
            side="left"
        )
        ttk.Button(actions, text="Remove", command=self.remove_task).pack(side="right")

        self.status = ttk.Label(main, text="Add a task to get started.", anchor="w")
        self.status.pack(fill="x", pady=(10, 0))
        self.task_entry.focus_set()

    def add_task(self, _event=None):
        task = self.task_entry.get().strip()
        if not task:
            self.status.config(text="Enter a task first.")
            return "break"
        self.todos.append([task, False])
        self.task_entry.delete(0, tk.END)
        self.refresh()
        self.task_list.selection_clear(0, tk.END)
        self.task_list.selection_set(tk.END)
        self.task_entry.focus_set()
        self.status.config(text=f"Added: {task}")
        return "break"

    def toggle_done(self, _event=None):
        selection = self.task_list.curselection()
        if not selection:
            self.status.config(text="Select a task first.")
            return
        index = selection[0]
        self.todos[index][1] = not self.todos[index][1]
        self.refresh()
        self.task_list.selection_set(index)
        state = "Completed" if self.todos[index][1] else "Reopened"
        self.status.config(text=f"{state}: {self.todos[index][0]}")

    def remove_task(self):
        selection = self.task_list.curselection()
        if not selection:
            self.status.config(text="Select a task to remove.")
            return
        task, _done = self.todos.pop(selection[0])
        self.refresh()
        self.status.config(text=f"Removed: {task}")

    def refresh(self):
        self.task_list.delete(0, tk.END)
        for task, done in self.todos:
            mark = "✓" if done else "○"
            self.task_list.insert(tk.END, f"{mark}  {task}")


def main():
    root = tk.Tk()
    TodoApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
