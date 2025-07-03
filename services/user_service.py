from models.user import User, UserRepository
import sqlite3
import bcrypt

class UserService:
    def __init__(self):
        self.repo = UserRepository()
    
    def get_all(self):
        return self.repo.get_all()
    
    def get_by_id(self, user_id):
        return self.repo.get_by_id(user_id)
    
    def save(self, name, email, birthdate, password, tipo='comum'):
        existing_user = self.repo.get_by_email(email)
        if existing_user:
            return False

        user = User(None, name, email, birthdate, tipo=tipo) 
        user.set_password(password)
        
        new_user_id = self.repo.add_user(user)
        
        return new_user_id is not None
    
    def update_user(self, user_id, name, email, birthdate, tipo): 
        user = self.repo.get_by_id(user_id)
        if not user:
            return False
        
        user.name = name
        user.email = email
        user.birthdate = birthdate
        user.tipo = tipo

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
    
    def update_profile(self, user_id, data):
        """
        Atualiza os dados do perfil de um usuário a partir de um dicionário.
        """
        user = self.repo.get_by_id(user_id)
        if not user:
            return False

        if 'name' in data:
            user.name = data['name']
        if 'email' in data:
            user.email = data['email']
        if 'birthdate' in data and data['birthdate']:
            user.birthdate = data['birthdate']

        if 'password' in data and data['password']:
            user.set_password(data['password'])

        try:
            return self.repo.update_user(user)
        except sqlite3.Error:
            return False