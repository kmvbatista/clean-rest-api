from repository import userRepository
from entity  import User

class userService:
    def __init__(self):
        self.repository = userRepository() 

    def getUsers(self):
        users = self.repository.get_users()
        return users

    def getUser(self, id):
        user_found = self.repository.get_user(id)
        return user_found

    def delete_user(self, id):
        self.repository.delete_user(id)
    
    def update_user(self, id, new_user_json):
        hashed_password = hash(new_user_json['password'])
        new_user = User(new_user_json['name'],new_user_json['email'], hashed_password, id)
        self.repository.update_user(id, new_user)

    def add_user(self, user_json):
        hashed_password = hash(user_json['password'])
        user = User( user_json['name'], user_json['email'], hashed_password, id)
        return self.repository.add_user(user)