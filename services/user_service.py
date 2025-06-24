from models.user import user_repository, User
import sqlite3

class UserService:
    def __init__(self):
        self.repo = user_repository
    
    def get_all(self):
        return self.repo.get_all()
    
    def get_by_id(self, user_id):
        return self.repo.get_by_id(user_id)
    
    # Salva um novo usuário, com verificação no email
    def save(self, name, email, birthdate, password):
        existing_user = self.repo.get_by_email(email)
        if existing_user:
            return False

        user = User(None, name, email, birthdate)
        user.set_password(password)
        
        new_user_id = self.repo.add_user(user)
        
        return new_user_id is not None
    
    def update_user(self, user_id, name, email, birthdate):
        user = self.repo.get_by_id(user_id)
        if not user:
            return False
        
        user.name = name
        user.email = email
        user.birthdate = birthdate

        try:
            return self.repo.update_user(user)
        except sqlite3.Error:
            return False
    
    def delete_user(self, user_id):
        return self.repo.delete_user(user_id)
    
    def authenticate(self, email, password):
        user = self.repo.get_by_email(email)
        if user and user.check_password(password):
            return user.to_dict()
        return None