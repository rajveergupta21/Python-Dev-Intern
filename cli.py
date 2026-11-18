import sys
from task_manager import TaskManager

class TodoCLI:
    def __init__(self):
        self.manager = TaskManager()

    def print_menu(self):
        print("\n=== TO-DO LIST MANAGER ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Remove Task")
        print("5. Exit")
        print("==========================")

    def view_tasks(self):
        tasks = self.manager.get_all_tasks()
        if not tasks:
            print("\nNo tasks found. Your to-do list is empty.")
            return

        print("\nYour Tasks:")
        print("-" * 50)
        for task in tasks:
            status = "[X]" if task.completed else "[ ]"
            print(f"{task.task_id}. {status} {task.title}")
        print("-" * 50)

    def add_task(self):
        title = input("\nEnter task description: ").strip()
        if not title:
            print("Error: Task description cannot be blank.")
            return

        try:
            task = self.manager.add_task(title)
            print(f"Success: Task '{task.title}' added with ID {task.task_id}.")
        except ValueError as e:
            print(f"Error: {e}")

    def prompt_task_id(self, action_name):
        user_input = input(f"\nEnter task ID to {action_name}: ").strip()
        if not user_input.isdigit():
            print("Error: Please enter a valid numerical ID.")
            return None
        return int(user_input)

    def mark_task(self):
        self.view_tasks()
        if not self.manager.get_all_tasks():
            return

        task_id = self.prompt_task_id("mark as completed")
        if task_id is None:
            return

        task = self.manager.mark_task_completed(task_id)
        if task:
            print(f"Success: Task {task_id} marked as completed.")
        else:
            print(f"Error: Task with ID {task_id} does not exist.")

    def remove_task(self):
        self.view_tasks()
        if not self.manager.get_all_tasks():
            return

        task_id = self.prompt_task_id("remove")
        if task_id is None:
            return

        task = self.manager.remove_task(task_id)
        if task:
            print(f"Success: Task '{task.title}' (ID {task_id}) was removed.")
        else:
            print(f"Error: Task with ID {task_id} does not exist.")

    def run(self):
        actions = {
            "1": self.view_tasks,
            "2": self.add_task,
            "3": self.mark_task,
            "4": self.remove_task
        }

        while True:
            self.print_menu()
            choice = input("Enter your choice (1-5): ").strip()

            if choice == "5":
                print("\nGoodbye!")
                sys.exit(0)
            elif choice in actions:
                actions[choice]()
            else:
                print("Invalid selection. Please choose an option from 1 to 5.")
