from todo_manager import add_task, remove_task, mark_done, list_tasks

def show_menu():
    print("\n==== TO-DO LIST ====")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Mark Task as Done")
    print("4. View Tasks")
    print("5. Exit")

if __name__ == "__main__":
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            task = input("Enter task description: ").strip()
            add_task(task)
            print(f"Task '{task}' added!")

        elif choice == "2":
            list_tasks()
            index = int(input("Enter task number to remove: ")) - 1
            if remove_task(index):
                print("Task removed successfully!")
            else:
                print("Invalid task number.")

        elif choice == "3":
            list_tasks()
            index = int(input("Enter task number to mark as done: ")) - 1
            if mark_done(index):
                print("Task marked as done!")
            else:
                print("Invalid task number.")

        elif choice == "4":
            print("\nYour Tasks:")
            list_tasks()

        elif choice == "5":
            print("Exiting To-Do List. Bye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
