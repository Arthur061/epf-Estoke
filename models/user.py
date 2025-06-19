import sqlite3
from datetime import datetime
import bcrypt

class User:
    def __init__(self, id, name, email, birthdate, password=None):
        self.id = id
        self.name = name
        self.email = email
        self.birthdate = birthdate
        self.password = password  # guarda o hash da senha

    def __repr__(self):
        return (f"User(id={self.id}, name='{self.name}', email='{self.email}', "
                f"birthdate='{self.birthdate}')")

    def to_dict(self): # convertendo obj para dict
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'birthdate': self.birthdate
        }
    
    def set_password(self, password): # gera hash da senha
        self.password = self._hash_password(password)

    def _hash_password(self, password): # gera hash bcrypt da senha
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    def check_password(self, password): # verifica se a senha = ao hash
        if not self.password:
            return False
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

class UserRepository:
    def __init__(self, db_path='database.db'):
        self.db_path = db_path
    
    def _get_connection(self):
        return sqlite3.connect(self.db_path)
    
    def _row_to_user(self, row):
        return User(
            id=row[0],
            name=row[1],
            email=row[2],
            birthdate=row[3],
            password=row[4] if len(row) > 4 else None
        )
    
    def get_all(self): # retorna todos users (se for precisar na parte admin)
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, email, birthdate, password FROM users")
            return [self._row_to_user(row) for row in cursor.fetchall()]
    
    def add_user(self, user): # add user no banco
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO users (name, email, birthdate, password) VALUES (?, ?, ?, ?)",
                (user.name, user.email, user.birthdate, user.password)
            )
            conn.commit()
            return cursor.lastrowid 
    
    def update_user(self, user): # att user no banco
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE users SET name = ?, email = ?, birthdate = ?, password = ? WHERE id = ?",
                (user.name, user.email, user.birthdate, user.password, user.id)
            )
            conn.commit()
            return cursor.rowcount > 0
    
    def delete_user(self, user_id): # Remove user do banco
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
            conn.commit()
            return cursor.rowcount > 0
        
user_repository = UserRepository()
