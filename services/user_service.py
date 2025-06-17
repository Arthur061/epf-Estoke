from bottle import request
from models.user import user_repository, User
import sqlite3

class UserService:
    def __init__(self):
        self.repo = user_repository
    
    def get_all(self):
        users = self.repo.get_all()
        return users
    
    def get_by_id(self, user_id):
        return self.repo.get_by_id(user_id)
    
    def save(self, name, email, birthdate, password):
        user = User(None, name, email, birthdate)
        user.set_password(password)
        
        try:
            new_user_id = self.repo.add_user(user)
            return new_user_id is not None
        except sqlite3.IntegrityError:
            return False
    
    def update_user(self, user_id, name, email, birthdate):
        user = self.repo.get_by_id(user_id)
        if not user:
            return False
        
        user.name = name
        user.email = email
        user.birthdate = birthdate
        
        try:
            return self.repo.update_user(user)
        except sqlite3.IntegrityError:
            return False
    
    def delete_user(self, user_id):
        return self.repo.delete_user(user_id)
    
    def authenticate(self, email, password):
        user = self.repo.get_by_email(email)
        if user and user.check_password(password):
            return user.to_dict()
        return None
