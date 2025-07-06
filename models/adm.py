import sqlite3
from .user import User, UserRepository 
import json

class Administrador(User):
    def __init__(self, id, name, email, birthdate, password=None, permissoes=None):
        super().__init__(id, name, email, birthdate, password, tipo="administrador") 
        self.permissoes = permissoes if permissoes is not None else []

    def to_dict(self):
        user_dict = super().to_dict()
        user_dict["permissoes"] = self.permissoes
        return user_dict

    @staticmethod
    def from_dict(data):
        admin = Administrador(data["id"], data["name"], data["email"], data["birthdate"], data.get("password"))
        admin.permissoes = data.get("permissoes", [])
        return admin

    def gerenciar_usuarios(self):
        # Lógica para gerenciar usuários
        print(f"Administrador {self.name} gerenciando usuários.")

    def gerar_relatorios(self):
        # Lógica para gerar relatórios
        print(f"Administrador {self.name} gerando relatórios.")

class AdministradorRepository(UserRepository):
    def __init__(self, db_path='database.db'):
        super().__init__(db_path)

    def _row_to_administrador(self, row):
        admin = Administrador(
            id=row[0],
            name=row[1],
            email=row[2],
            birthdate=row[3],
            password=row[4],
            permissoes=json.loads(row[5]) if row[5] else [] # Carregar permissões como lista
        )
        return admin

    def add_administrador(self, admin): # add admin no banco
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO users (name, email, birthdate, password, tipo, permissoes) VALUES (?, ?, ?, ?, ?, ?)",
                (admin.name, admin.email, admin.birthdate, admin.password, admin.tipo, json.dumps(admin.permissoes))
            )
            conn.commit()
            return cursor.lastrowid 
    
    def update_administrador(self, admin): # att admin no banco
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE users SET name = ?, email = ?, birthdate = ?, password = ?, tipo = ?, permissoes = ? WHERE id = ?",
                (admin.name, admin.email, admin.birthdate, admin.password, admin.tipo, json.dumps(admin.permissoes), admin.id)
            )
            conn.commit()
            return cursor.rowcount > 0

    def get_all_administradores(self):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, email, birthdate, password, permissoes FROM users WHERE tipo = 'administrador'")
            return [self._row_to_administrador(row) for row in cursor.fetchall()]

    def get_administrador_by_id(self, admin_id):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, email, birthdate, password, permissoes FROM users WHERE id = ? AND tipo = 'administrador'", (admin_id,))
            row = cursor.fetchone()
            return self._row_to_administrador(row) if row else None


