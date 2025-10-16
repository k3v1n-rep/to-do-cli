# Handles task storage and operations

tasks = []

def add_task(task):
    tasks.append({"task": task, "done": False})

def remove_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
        return True
    return False

def mark_done(index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        return True
    return False

def list_tasks():
    if not tasks:
        print("No tasks available.")
    for i, t in enumerate(tasks):
        status = "✔" if t["done"] else "✖"
        print(f"{i+1}. [{status}] {t['task']}")
