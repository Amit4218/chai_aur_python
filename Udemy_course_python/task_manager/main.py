import os

TASK_FILE = "TaskFile.txt"

# load task


def load_task():

    tasks = []

    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r", encoding="utf-8") as file:
            for line in file:
                text, status = line.strip().rsplit("||", 1)
                tasks.append({"text": text, "done": status == "done"})
    return tasks


# show all the tasks


def show_tasks(tasks):
    if tasks:
        print("-" * 50)
        for i, task in enumerate(tasks, 1):
            check_box = f"✅" if task["done"] else ""
            print(f"\n{i}: [{check_box}] {task['text']}")
    else:
        print("\nNo Task....\n")


# save Task


def save_task(tasks):

    if tasks:
        with open(TASK_FILE, "w", encoding="utf-8") as file:
            for task in tasks:
                status = "done" if task["done"] else "not done"
                file.write(f"{task['text']} || {status}\n")


def task_manager():

    tasks = load_task()

    while True:

        print("\n------Task List Manager -------")
        print("1. Add task")
        print("2. View Tasks")
        print("3. Mark Task as complete")
        print("4. Delete task")
        print("5. Exit")

        choice = input("\nEnter your choise (1-5): ").strip()

        match choice:

            case "1":
                print("-" * 50)

                task = input("\nEnter your Task: ").strip()

                if task:
                    tasks.append({"text": task, "done": False})
                    save_task(tasks)

            case "2":
                show_tasks(tasks=tasks)

            case "3":
                show_tasks(tasks)

                try:
                    print("-" * 50)
                    num = int(input("\nEnter your task number for completion: "))

                    if 1 <= num <= len(tasks):
                        tasks[num - 1]["done"] = True
                        save_task(tasks)
                        print("Task marked as completed...")
                    else:
                        print("Invalid task number...")

                except ValueError:
                    print("Please enter a number...")

            case "4":
                show_tasks(tasks)

                try:
                    print("-" * 50)
                    num = int(input("\nEnter your task number for deletion: "))

                    if 1 <= num <= len(tasks):
                        deleted_task = tasks.pop(num - 1)
                        save_task(tasks)
                        print("\n")
                        print(f"Task: {deleted_task['text']}, has been deleted...")
                    else:
                        print("Invalid task number...")

                except ValueError:
                    print("Please enter a number...")

            case "5":
                print("Exiting now....")
                break


task_manager()
