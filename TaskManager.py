import json
from Task import Task

class TaskManager:
    def __init__(self, filename):
        # here the file name refers to the json file
        self.filename = filename
        # here the tasks refers to the list of task objects
        self.tasks = self.load_tasks()
        # each task has an id, and the id is auto-incremented, this function is used to update the id counter
        self.update_id_counter()

    def update_id_counter(self):
        max_id = 0
        # find the max id in the current tasks
        for task in self.tasks:
            if task.id:
                max_id = max(max_id, task.id)
        Task.id_counter = max_id + 1

    def load_tasks(self):
        # load the tasks from the json file
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                # here transfer the json data to the task objects
                return [Task.from_dict(task) for task in data]
        # if the file does not exist or the json is invalid, create a new task file
        except (FileNotFoundError, json.JSONDecodeError):
            print(f"Warning: Could not load tasks from '{self.filename}'. A new task list will be created.")
            return []

    def save_tasks(self):
        # save the tasks to the json file
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump([t.to_dict() for t in self.tasks], f, indent=2)

    def add_task(self, task):
        # here add a new task to the list of tasks
        self.tasks.append(task)
        self.save_tasks()

    def delete_task(self, task_id):
        self.tasks = [t for t in self.tasks if t.id != task_id]
        self.save_tasks()

    def update_task(self, task_id, **kwargs):
        for task in self.tasks:
            if task.id == task_id:
                for key, value in kwargs.items():
                    if hasattr(task, key):
                        setattr(task, key, value)
                task.price = task.calculate_price()
                break
        self.save_tasks()

    def get_all_tasks(self):
        #get all tasks sorted by shoot date
        sorted_tasks = sorted(self.tasks, key=lambda x: x.shoot_date)
        return sorted_tasks
    
    # The following functions are used to get the total price and count of uncompleted tasks
    def get_total_price(self):
        # calculate the total price of all tasks
        return sum(task.price for task in self.tasks if not task.completed)

    def count_tasks(self):
        # count the number of tasks that are not completed
        total_not_completed_count = len([t for t in self.tasks if not t.completed])
        total_completed_count = len([t for t in self.tasks if t.completed])
        return total_not_completed_count, total_completed_count

if __name__ == "__main__":
    # Example usage
    manager = TaskManager("data.json")

    # task = Task(2, "day", "indoor", "Tokyo", "Naruto", "2023-10-15")
    # manager.add_task(task)
    # new_task_3 = Task(1, 'day', 'outdoor', 'sydney opera house', 'free', '2025-10-01')
    # manager.add_task(new_task_3)
    # manager.delete_task(new_task_2)
    # print(manager.get_all_tasks())
    # print(f"Total price: {manager.get_total_price()}")

    # test delete task
    # manager.delete_task(1)

    # test count task
    print(manager.count_tasks())