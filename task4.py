#Task 4: Simple To-Do List
#Build a command-line to-do list app with add, remove, and view functionalities.
# Simple To-Do List App

todo_list = []

def show_menu():
    print("\n----- To-Do List Menu -----")
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Remove a Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        if not todo_list:
            print("Your to-do list is empty.")
        else:
            print("\nYour To-Do List:")
            for idx, task in enumerate(todo_list, start=1):
                print(f"{idx}. {task}")
                
    elif choice == '2':
        task = input("Enter the task to add: ")
        todo_list.append(task)
        print(f"Task '{task}' added.")
        
    elif choice == '3':
        if not todo_list:
            print("Your to-do list is empty. Nothing to remove.")
        else:
            for idx, task in enumerate(todo_list, start=1):
                print(f"{idx}. {task}")
            try:
                task_num = int(input("Enter the number of the task to remove: "))
                if 1 <= task_num <= len(todo_list):
                    removed_task = todo_list.pop(task_num - 1)
                    print(f"Task '{removed_task}' removed.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
                
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
