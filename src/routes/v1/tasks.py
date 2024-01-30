from flask import Blueprint, jsonify, request, current_app
from typing import Optional

api = Blueprint('api', __name__)

# 1. Create a new task
@api.route('/tasks', methods=['POST'])
def create_task():
    data = request.json

    tasksToCreate = data.get('tasks', None)

    if tasksToCreate:
        tasksIds = current_app.config['DATABASE'].create_mass_tasks(tasksToCreate)
    else:
        tasksIds = current_app.config['DATABASE'].create_task(data)

    return jsonify(tasksIds), 201

# 2. List all tasks
@api.route('/tasks', methods=['GET'])
def list_tasks():
    return jsonify({
        'tasks': current_app.config['DATABASE'].tasks
    }), 200

# 3. Get a specific task
@api.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = current_app.config['DATABASE'].get_task(task_id)
    if task:
        return jsonify(task)
    return jsonify({'error': 'Task not found'}), 404

# 4. Delete a specified task
@api.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id: Optional[int]):
    if task_id is None:
        task_id = request.json.get('tasks')
    current_app.config['DATABASE'].delete_task(task_id)
    return '', 200

# 5. Edit the title or completion of a specific task
@api.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.json
    title = data.get('title')
    completed = data.get('is_completed')

    task = current_app.config['DATABASE'].update_task(task_id, title, completed)

    if not task:
        return jsonify({'error': 'There is no task at that id'}), 404

    return '', 200