
from extensions import mongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from entity import User

class userRepository:
    def get_users(self):
        users = mongo.db.users.find()
        resp = dumps(users)
        return resp
    
    def get_user(self, id):
        user = mongo.db.users.find_one(
            {'_id':ObjectId(id)})
        resp = dumps(user)
        return resp
    
    def add_user(self, user: User):
        user_id = mongo.db.users.insert(
            {'name': user.name, 'email': user.email, 'password': user.password})
        return user_id
    
    def delete_user(self, id):
        mongo.db.users.delete_one({'_id': ObjectId(id)})

    def update_user(self, id, new_user):
        mongo.db.users.update_one(
            {'_id': ObjectId(id)}, {'$set':{'name': new_user.name, 'email': new_user.email, 'password': new_user.password}})