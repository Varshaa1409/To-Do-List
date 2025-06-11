tasks = []

def show_tasks():
    print("\nYour To-Do List:")
    if not tasks:
        print("→ No tasks yet!")
    else:
        for idx, task in enumerate(tasks, start=1):
            status = "✅" if task['completed'] else "❌"
            print(f"{idx}. {task['task']} {status}")
    print()

def add_task():
    task_name = input("Enter the task: ")
    tasks.append({'task': task_name, 'completed': False})
    print("Task added!")

def mark_complete():
    show_tasks()
    try:
        task_num = int(input("Enter task number to mark complete: "))
        tasks[task_num - 1]['completed'] = True
        print("Task marked as completed!")
    except:
        print("Invalid input. Try again.")

def delete_task():
    show_tasks()
    try:
        task_num = int(input("Enter task number to delete: "))
        tasks.pop(task_num - 1)
        print("Task deleted!")
    except:
        print("Invalid input. Try again.")

def main():
    while True:
        print("------ To-Do List App ------")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            mark_complete()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting To-Do List App. Bye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
