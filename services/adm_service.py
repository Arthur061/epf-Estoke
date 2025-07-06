from models.adm import Administrador, AdministradorRepository
from models.user import UserRepository
import sqlite3

class AdministradorService:
    def __init__(self):
        self.admin_repo = AdministradorRepository()
        self.user_repo = UserRepository()

    def get_all_administradores(self):
        return self.admin_repo.get_all_administradores()

    def get_administrador_by_id(self, admin_id):
        return self.admin_repo.get_administrador_by_id(admin_id)

    def add_administrador(self, name, email, birthdate, password, permissoes=None):
        admin = Administrador(None, name, email, birthdate, permissoes=permissoes)
        admin.set_password(password)
        try:
            new_admin_id = self.admin_repo.add_administrador(admin)
            return new_admin_id is not None
        except sqlite3.IntegrityError:
            return False

    def update_administrador(self, admin_id, name, email, birthdate, permissoes=None):
        admin = self.admin_repo.get_administrador_by_id(admin_id)
        if not admin:
            return False

        admin.name = name
        admin.email = email
        admin.birthdate = birthdate
        admin.permissoes = permissoes if permissoes is not None else admin.permissoes

        try:
            return self.admin_repo.update_administrador(admin)
        except sqlite3.IntegrityError:
            return False

    def delete_administrador(self, admin_id):
        return self.admin_repo.delete_user(admin_id) 

    def gerenciar_usuarios(self, admin_id):
        admin = self.get_administrador_by_id(admin_id)
        if admin:
            admin.gerenciar_usuarios()
            return True
        return False

    def gerar_relatorios(self, admin_id):
        admin = self.get_administrador_by_id(admin_id)
        if admin:
            admin.gerar_relatorios()
            return True
        return False

administrador_service = AdministradorService()

