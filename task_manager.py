tasks = []


def show_tasks():
    print("\n--- My Tasks ---")

    if len(tasks) == 0:
        print("No tasks yet.")
        return

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def add_task():
    task = input("Enter your task: ").strip()

    if task == "":
        print("Task cannot be empty.")
    else:
        tasks.append(task)
        print("Task added!")


def complete_task():
    show_tasks()

    if len(tasks) == 0:
        return

    try:
        task_number = int(input("Enter the task number to complete: "))

        if task_number >= 1 and task_number <= len(tasks):
            print(f"Completed: {tasks[task_number - 1]}")
            tasks.pop(task_number - 1)
        else:
            print("That task number does not exist.")

    except ValueError:
        print("Please enter a number.")


def delete_task():
    show_tasks()

    if len(tasks) == 0:
        return

    try:
        task_number = int(input("Enter the task number to delete: "))

        if task_number >= 1 and task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)
            print(f"Deleted: {deleted_task}")
        else:
            print("That task number does not exist.")

    except ValueError:
        print("Please enter a number.")


def main():
    while True:
        print("\n===== TaskMate CLI =====")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
