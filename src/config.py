
class DATABASE:

    def __init__(self) -> None:
        self.tasks = []

    def generate_task_id(self):
        if self.tasks:
            return self.tasks[-1]['id'] + 1
        return 1

    def get_task(self, task_id):
        task = next((task for task in self.tasks if task['id'] == task_id), None)
        if task:
            return task
        return None
    
    def update_task(self, task_id, title, completed) -> bool:
        task = self.get_task(task_id)
        if task:
            if title:
                task['title'] = title
            if completed is not None:
                task['is_completed'] = completed

            self.tasks = [_task if task['id'] != task_id else task for _task in self.tasks]
        else:
            return False
        return True
    
    def create_task(self, data):

        title = data.get('title')
        completed = data.get('is_completed', False)

        task = {
            'id': self.generate_task_id(),
            'title': title,
            'is_completed': completed
        }
        self.tasks.append(task)

        return {
            'id': task['id']
        }
    
    def create_mass_tasks(self, tasks):
        tasksIds = []
        for data in tasks:
            task = self.create_task(data)
            tasksIds.append(task)
        return {
            'tasks': tasksIds
        }
    
    def delete_task(self, task_id):
        if isinstance(task_id, list):
            for task in task_id:
                self.tasks = [task for task in self.tasks if task['id'] != task_id]
        else:
            self.tasks = [task for task in self.tasks if task['id'] != task_id]
    
class Config:
    DATABASE = DATABASE()