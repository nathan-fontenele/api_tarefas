from flask_restful import Resource
from flask import request
from app import api
from app.main_db import MainDB

class TaskManagement(Resource):
    def get(self):
        return {'tasks': MainDB().fetch_data()}

    def post(self):
        data = request.get_json()

        task_name = data.get('name')
        task_description = data.get('description')

        db = MainDB()
        db.insert_task(task_name, task_description)

        return {'message': 'Task created successfully!'}, 201
    
    def delete(self):
        data = request.get_json()

        task_id = data.get('id')

        db = MainDB()
        db.delete_task(task_id)
        return {'message': 'Task deleted successfully!'}, 200
    
    def put (self):
        data = request.get_json()

        task_id = data.get('id')
        task_name = data.get('name')
        task_description = data.get('description')

        db = MainDB()
        db.update_task(task_id, task_name, task_description)
        return {'message': 'Task updated successfully!'}, 200

# Adiciona a rota à API
api.add_resource(TaskManagement, '/tasks')
