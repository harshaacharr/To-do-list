import os
import json
from datetime import datetime, timedelta

# Constants
TODO_FILE = "todo_list.json"

# Function to load tasks from the file
def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            tasks = json.load(file)
        return tasks
    else:
        return []

# Function to save tasks to the file
def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=2)

# Function to display tasks in a list
def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task['title']} - Priority: {task['priority']}, Due Date: {task['due_date']}, Completed: {task['completed']}")

# Function to add a new task
def add_task(tasks):
    title = input("Enter task title: ")
    priority = input("Enter task priority (high/medium/low): ")
    due_date_str = input("Enter due date (YYYY-MM-DD): ")
    
    try:
        due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    new_task = {
        "title": title,
        "priority": priority,
        "due_date": due_date_str,
        "completed": False
    }

    tasks.append(new_task)
    save_tasks(tasks)
    print("Task added successfully.")

# Function to remove a task
def remove_task(tasks):
    display_tasks(tasks)
    task_idx = int(input("Enter the number of the task to remove: ")) - 1

    if 0 <= task_idx < len(tasks):
        removed_task = tasks.pop(task_idx)
        save_tasks(tasks)
        print(f"Task '{removed_task['title']}' removed successfully.")
    else:
        print("Invalid task number.")

# Function to mark a task as completed
def mark_completed(tasks):
    display_tasks(tasks)
    task_idx = int(input("Enter the number of the task to mark as completed: ")) - 1

    if 0 <= task_idx < len(tasks):
        tasks[task_idx]["completed"] = True
        save_tasks(tasks)
        print(f"Task '{tasks[task_idx]['title']}' marked as completed.")
    else:
        print("Invalid task number.")

# Main function
def main():
    tasks = load_tasks()

    while True:
        print("\nTODO List Application:")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Mark Task as Completed")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            mark_completed(tasks)
        elif choice == "5":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
