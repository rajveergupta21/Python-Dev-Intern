class Task:
    def __init__(self, task_id, title, completed=False):
        self.task_id = task_id
        self.title = title
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def to_dict(self):
        return {
            "id": self.task_id,
            "title": self.title,
            "completed": self.completed
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["id"], data["title"], data.get("completed", False))
