import sqlite3
from datetime import datetime
import bcrypt

class User:
    def __init__(self, id, name, email, birthdate, password=None, tipo=None):
        self.id = id
        self.name = name
        self.email = email
        self.birthdate = birthdate
        self.password = password
        self.tipo = tipo

    def __repr__(self):
        return (f"User(id={self.id}, name='{self.name}', email='{self.email}', "
                f"birthdate='{self.birthdate}', tipo='{self.tipo}')") 

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'birthdate': self.birthdate,
            'tipo': self.tipo  
        }

    def set_password(self, password):
        self.password = self._hash_password(password)

    def _hash_password(self, password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password):
        if not self.password:
            return False
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

class UserRepository:
    def __init__(self, db_path='database.db'): 
        self.db_path = db_path

    def _get_connection(self):
        return sqlite3.connect(self.db_path)

    def _row_to_user(self, row):
        if not row:
            return None
        return User(
            id=row[0],
            name=row[1],
            email=row[2],
            birthdate=row[3],
            password=row[4],
            tipo=row[5] 
        )

    def get_by_email(self, email):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, email, birthdate, password, tipo FROM users WHERE email = ?", (email,))
            row = cursor.fetchone()
            return self._row_to_user(row)

    def get_by_id(self, user_id):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, email, birthdate, password, tipo FROM users WHERE id = ?", (user_id,))
            row = cursor.fetchone()
            return self._row_to_user(row)

    def get_all(self):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, email, birthdate, password, tipo FROM users")
            return [self._row_to_user(row) for row in cursor.fetchall()]

    def add_user(self, user):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO users (name, email, birthdate, password, tipo) VALUES (?, ?, ?, ?, ?)",
                (user.name, user.email, user.birthdate, user.password, user.tipo)
            )
            conn.commit()
            return cursor.lastrowid

    def update_user(self, user):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE users SET name = ?, email = ?, birthdate = ?, password = ?, tipo = ? WHERE id = ?",
                (user.name, user.email, user.birthdate, user.password, user.tipo, user.id)
            )
            conn.commit()
            return cursor.rowcount > 0

    def delete_user(self, user_id):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
            conn.commit()
            return cursor.rowcount > 0