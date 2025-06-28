import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    """Loads tasks from the file."""
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            for line in f:
                task, status = line.strip().split("|")
                tasks.append({"task": task, "completed": status == "True"})
    return tasks

def save_tasks(tasks):
    """Saves tasks to the file."""
    with open(TASKS_FILE, "w") as f:
        for task_item in tasks:
            f.write(f"{task_item['task']}|{task_item['completed']}\n")

def display_tasks(tasks):
    """Displays all tasks with their status."""
    if not tasks:
        print("No tasks in the list.")
        return
    print("\n--- Your To-Do List ---")
    for i, task_item in enumerate(tasks):
        status = "[x]" if task_item["completed"] else "[ ]"
        print(f"{i + 1}. {status} {task_item['task']}")
    print("-----------------------\n")

def add_task(tasks):
    """Adds a new task to the list."""
    task_description = input("Enter the task description: ")
    tasks.append({"task": task_description, "completed": False})
    save_tasks(tasks)
    print("Task added successfully!")

def mark_task_completed(tasks):
    """Marks a task as completed."""
    display_tasks(tasks)
    if not tasks:
        return

    try:
        task_num = int(input("Enter the number of the task to mark as completed: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_task(tasks):
    """Deletes a task from the list."""
    display_tasks(tasks)
    if not tasks:
        return

    try:
        task_num = int(input("Enter the number of the task to delete: "))
        if 1 <= task_num <= len(tasks):
            deleted_task = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Task '{deleted_task['task']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    tasks = load_tasks()

    while True:
        print("To-Do List Application")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()