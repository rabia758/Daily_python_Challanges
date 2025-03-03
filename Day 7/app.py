def show_menu():
    print("\nWelcome to To-Do List! 📝")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Delete Task")
    print("4. Exit")

def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    print("Task Added! ✅")

def show_tasks(tasks):
    if tasks:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("No tasks available. Add a task first. 📋")

def delete_task(tasks):
    show_tasks(tasks)
    if tasks:
        task_num = int(input("Enter the task number to delete: "))
        if 0 < task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task}' deleted! ❌")
        else:
            print("Invalid task number. Please try again.")

def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Enter choice: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            show_tasks(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            print("Exiting To-Do List. Have a productive day! 👋")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
