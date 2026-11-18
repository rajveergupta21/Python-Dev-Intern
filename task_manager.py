import json
import os
from task import Task

class TaskManager:
    def __init__(self, storage_path="tasks.json"):
        self.storage_path = storage_path
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(self.storage_path):
            self.tasks = []
            return

        try:
            with open(self.storage_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.tasks = [Task.from_dict(item) for item in data]
        except (json.JSONDecodeError, OSError, KeyError):
            self.tasks = []

    def save_tasks(self):
        data = [task.to_dict() for task in self.tasks]
        with open(self.storage_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def get_next_id(self):
        if not self.tasks:
            return 1
        return max(task.task_id for task in self.tasks) + 1

    def add_task(self, title):
        cleaned_title = title.strip()
        if not cleaned_title:
            raise ValueError("Task title cannot be empty.")
        task = Task(self.get_next_id(), cleaned_title)
        self.tasks.append(task)
        self.save_tasks()
        return task

    def remove_task(self, task_id):
        for index, task in enumerate(self.tasks):
            if task.task_id == task_id:
                removed = self.tasks.pop(index)
                self.save_tasks()
                return removed
        return None

    def mark_task_completed(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.mark_completed()
                self.save_tasks()
                return task
        return None

    def get_all_tasks(self):
        return self.tasks
