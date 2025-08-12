def generate_numbered_tasks(tasks: list):

    numbered_task = []

    for idx, task in enumerate(tasks, start=1):
        numbered_task.append(f"{idx}. {task}")

    return numbered_task


task_list = [
    "task",
    "task",
    "task",
    "task",
]

generate_numbered_tasks(task_list)
