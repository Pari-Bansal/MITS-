import tkinter as tk
from tkinter import messagebox

# Main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")
root.resizable(False, False)

# ---- Title ----
tk.Label(root, text="My To-Do List", font=("Arial", 20)).pack(pady=(10, 5))

# ---- Input Area ----
input_frame = tk.Frame(root)
input_frame.pack(pady=(0, 10))

task_entry = tk.Entry(input_frame, font=("Arial", 12), width=25)
task_entry.pack(side=tk.LEFT, padx=(0, 5))

tk.Button(input_frame, text="Add", command=lambda: add_task(), width=8).pack(side=tk.LEFT)

# ---- Scrollable Task Area in Separate Frame ----
task_area_frame = tk.Frame(root)
task_area_frame.pack(pady=(0, 10), expand=True, fill="both")

canvas = tk.Canvas(task_area_frame, borderwidth=0)
task_frame = tk.Frame(canvas)
scrollbar = tk.Scrollbar(task_area_frame, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((0, 0), window=task_frame, anchor="nw")

def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))
task_frame.bind("<Configure>", on_frame_configure)

# ---- Task Management ----
tasks = []

def add_task():
    text = task_entry.get().strip()
    if text:
        var = tk.BooleanVar()
        cb = tk.Checkbutton(task_frame, text=text, variable=var, font=("Arial", 12), anchor='w', width=30)
        cb.var = var
        cb.pack(anchor='w', padx=10, pady=2)
        tasks.append(cb)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_selected():
    selected = [t for t in tasks if t.var.get()]
    if not selected:
        messagebox.showinfo("No Selection", "No tasks selected for deletion.")
        return
    for t in selected:
        t.destroy()
        tasks.remove(t)

def clear_all():
    if messagebox.askyesno("Clear All", "Are you sure you want to delete all tasks?"):
        for t in tasks:
            t.destroy()
        tasks.clear()

# ---- Control Buttons ----
control_frame = tk.Frame(root)
control_frame.pack(pady=5)

tk.Button(control_frame, text="Delete Selected", width=15, command=delete_selected).pack(side=tk.LEFT, padx=5)
tk.Button(control_frame, text="Clear All", width=10, command=clear_all).pack(side=tk.LEFT, padx=5)

# Start GUI loop
root.mainloop()
