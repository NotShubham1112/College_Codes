tasks = []

while True:
    print("\nTask Manager:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Update Task")
    print("4. Display Tasks")
    print("5. Sort Tasks")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        task_name = input("Enter task name: ")
        tasks.append((task_name, False))
        print(f"Added task: {task_name}")

    elif choice == "2":
        task_name = input("Enter task name to remove: ")
        tasks = [task for task in tasks if task[0] != task_name]
        print(f"Removed task: {task_name}")

    elif choice == "3":
        old_name = input("Enter task name to update: ")
        for i in range(len(tasks)):
            if tasks[i][0] == old_name:
                new_name = input("Enter new task name: ")
                tasks[i] = (new_name, tasks[i][1])
                print(f"Updated task: {old_name} -> {new_name}")
                break
        else:
            print("Task not found!")

    elif choice == "4":
        print("\nYour Tasks:")
        if not tasks:
            print("No tasks yet!")
        else:
            for i, (name, completed) in enumerate(tasks, 1):
                print(f"{i}. {name}")

    elif choice == "5":
        tasks.sort(key=lambda x: x[0])
        print("Tasks sorted!")

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, please try again!")
