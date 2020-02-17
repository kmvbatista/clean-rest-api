import settings
from flask import Blueprint, jsonify, request
from services import userService


app_users = Blueprint('users', __name__)

service = userService()

@app_users.route('/users', methods=['GET'])
def getUsers():
    users = service.getUsers()
    resp = jsonify(users)
    return resp
    

@app_users.route('/users/<id>', methods=['GET'])
def getUser(id):
    user = service.getUser(id)
    resp = jsonify(user)
    resp.status_code = 200
    return resp
    

@app_users.route('/users', methods=['POST'])
def add_user():
    json_comming = request.json
    user_id = service.add_user(json_comming)
    resp = jsonify('user added successfully. User id = {user_id}')
    resp.status_code = 200
    return resp

@app_users.route('/users/<id>', methods=['DELETE'])
def delete_user():
    resp = jsonify('User deleted successfully')
    resp.status_code = 200
    return resp

@app_users.route('/users/<id>', methods=['PUT'])
def update_user(id):
        new_user_json = request.json
        service.update_user(id, new_user_json)
        resp = jsonify('User updated successfully')
        resp.status_code = 200
        return resp

@app_users.errorhandler(404)
def not_found(error=None):
    message = {
        'status':404,
        'message': 'Not Found' + request.url
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp