import sqlite3
from models.adm import Administrador, administrador_repository

class AdministradorService:
    def __init__(self):
        self.repo = administrador_repository
    
    def get_all(self):
        """Retorna todos os administradores"""
        return self.repo.get_all_administradores()
    
    def get_by_id(self, admin_id):
        """Busca administrador por ID"""
        return self.repo.get_administrador_by_id(admin_id)
    
    def save(self, nome, email, permissoes, password):
        """
        Cria um novo administrador
        Retorna True se sucesso, False se falhou (email duplicado)
        """
        admin = Administrador(None, nome, email, permissoes)
        admin.set_password(password)
        
        try:
            new_admin_id = self.repo.add_administrador(admin)
            return new_admin_id is not None
        except sqlite3.IntegrityError:
            return False
    
    def update(self, admin_id, nome, email, permissoes):
        """
        Atualiza dados do administrador
        Retorna True se sucesso, False se falhou (email duplicado ou admin não existe)
        """
        admin = self.get_by_id(admin_id)
        if not admin:
            return False
        
        admin.nome = nome
        admin.email = email
        admin.permissoes = permissoes
        
        try:
            return self.repo.update_administrador(admin)
        except sqlite3.IntegrityError:
            return False
    
    def delete(self, admin_id):
        """Remove administrador pelo ID"""
        return self.repo.delete_administrador(admin_id)
    
    def authenticate(self, email, password):
        """
        Autentica administrador
        Retorna dados do admin se sucesso, None se falhou
        """
        admin = self.repo.get_administrador_by_email(email)
        if admin and admin.check_password(password):
            return admin.to_dict()
        return None
    
    def change_password(self, admin_id, new_password):
        """
        Altera senha do administrador
        Retorna True se sucesso, False se admin não existe
        """
        admin = self.get_by_id(admin_id)
        if not admin:
            return False
            
        admin.set_password(new_password)
        return self.repo.update_administrador(admin)


