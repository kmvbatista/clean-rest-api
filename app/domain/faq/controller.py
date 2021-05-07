from flask import Blueprint, jsonify, request
from .service import FaqService

controller_name = 'faqs'

controller = Blueprint(controller_name, __name__)

@controller.before_app_first_request
def init():
    global service
    service = FaqService()

@controller.route('/{controller_name}/<id>', methods=['GET'])
def get_by_id(id):
    user = service.get_one(id)
    resp = jsonify(user)
    resp.status_code = 200
    return resp

@controller.route('/{controller_name}', methods=['GET'])
def get_all():
        users = service.get_all()
        resp = jsonify(users)
        return resp

@controller.route('/{controller_name}', methods=['POST'])
def add_user():
    json_comming = request.json
    service.add__one(json_comming)
    resp = jsonify('Added successfully')
    resp.status_code = 200
    return resp

@controller.route('/{controller_name}/<id>', methods=['DELETE'])
def delete_user(id):
    service.delete_one(id)
    resp = jsonify('Deleted successfully')
    resp.status_code = 200
    return resp

@controller.route('/{controller_name}/<id>', methods=['PUT'])
def update_user(id):
    new_user_json = request.json
    service.update_one(id, new_user_json)
    resp = jsonify('Updated successfully')
    resp.status_code = 200
    return resp