# Project Requirements
# User Interface (UI):
# Create a command-line interface (CLI) for the To-Do List Application.
# Display a welcoming message and a menu with the following options:
#         Welcome to the To-Do List App!

#         Menu:
#         1. Add a task
#         2. View tasks
#         3. Mark a task as complete
#         4. Delete a task
#         5. Quit


import datetime

# Function to display the welcome message and menu
def display_menu():
    print("\nWelcome to the To-Do List App!")
    print("\nMenu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")

# Function to add a task
def add_task(tasks):
    task = input("Enter a new task: ")
    priority = input("Enter the task priority (low, medium, high): ").lower()
    due_date = input("Enter the due date (YYYY-MM-DD): ")
    try:
        due_date = datetime.datetime.strptime(due_date, '%Y-%m-%d')
    except ValueError:
        print("Invalid date format. Task will have no due date.")
        due_date = None
    tasks.append({'description': task, 'priority': priority, 'due_date': due_date, 'completed': False})
    print("Task added successfully.")

# Function to view tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for idx, task in enumerate(tasks, start=1):
            status = "Completed" if task['completed'] else "Incomplete"
            due_date = task['due_date'].strftime('%Y-%m-%d') if task['due_date'] else "No due date"
            print(f"{idx}. {task['description']} - Priority: {task['priority'].capitalize()} - Due Date: {due_date} - Status: {status}")

# Function to mark a task as complete by adding "X" to the end of the task description
def mark_task_complete(tasks):
    if not tasks:
        print("No tasks available to mark as complete.")
        return
    try:
        task_num = int(input("Enter the task number to mark as complete: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]['description'] += " X"
            tasks[task_num - 1]['completed'] = True
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Function to delete a task
def delete_task(tasks):
    if not tasks:
        print("No tasks available to delete.")
        return
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            del tasks[task_num - 1]
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main function to run the To-Do List Application
def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_complete(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Quitting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option from the menu.")

if __name__ == "__main__":
    main()