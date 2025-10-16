import json
import os

TASK_FILE = "tasks.json"

# Load tasks from file if it exists
if os.path.exists(TASK_FILE):
    with open(TASK_FILE, "r") as f:
        tasks = json.load(f)
else:
    tasks = []

def save_tasks():
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(task):
    tasks.append({"task": task, "done": False})
    save_tasks()

def remove_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks()
        return True
    return False

def mark_done(index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks()
        return True
    return False

def list_tasks():
    if not tasks:
        print("No tasks available.")
    for i, t in enumerate(tasks):
        status = "✔" if t["done"] else "✖"
        print(f"{i+1}. [{status}] {t['task']}")
