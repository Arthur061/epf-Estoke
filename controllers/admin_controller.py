from bottle import Bottle, request, redirect
from .base_controller import BaseController
from services.adm_service import AdministradorService
from services.user_service import UserService

class AdminController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.admin_service = AdministradorService()
        self.user_service = UserService()
        self.setup_routes()

    def setup_routes(self):
        self.app.route("/admin/users", method="GET", callback=self.list_all_users)
        self.app.route("/admin/users/edit/<user_id:int>", method=["GET", "POST"], callback=self.edit_user_by_admin)
        self.app.route("/admin/users/delete/<user_id:int>", method="POST", callback=self.delete_user_by_admin)
        self.app.route("/admin/administradores", method="GET", callback=self.list_administrators)
        self.app.route("/admin/administradores/add", method=["GET", "POST"], callback=self.add_administrator)
        self.app.route("/admin/administradores/edit/<admin_id:int>", method=["GET", "POST"], callback=self.edit_administrator)
        self.app.route("/admin/administradores/delete/<admin_id:int>", method="POST", callback=self.delete_administrator)

    def check_admin_permission(self):
        session = request.environ.get("beaker.session")
        user_id = session.get("user_id")
        if not user_id:
            return False 
        
        admin = self.admin_service.get_administrador_by_id(user_id)
        return admin is not None

    def list_all_users(self):
        if not self.check_admin_permission():
            return "Acesso negado. Apenas administradores podem gerenciar usuários."
        users = self.user_service.get_all()
        return self.render("admin_users", users=users) 

    def edit_user_by_admin(self, user_id):
        if not self.check_admin_permission():
            return "Acesso negado. Apenas administradores podem editar usuários."
        user = self.user_service.get_by_id(user_id)
        if not user:
            return "Usuário não encontrado"

        if request.method == "GET":
            return self.render("admin_user_form", user=user, action=f"/admin/users/edit/{user_id}") 
        else:
            name = request.forms.get("name")
            email = request.forms.get("email")
            birthdate = request.forms.get("birthdate")
            tipo = request.forms.get("tipo")
            if self.user_service.update_user(user_id, name, email, birthdate, tipo):
                self.redirect("/admin/users")
            else:
                return "Erro ao atualizar usuário."

    def delete_user_by_admin(self, user_id):
        if not self.check_admin_permission():
            return "Acesso negado. Apenas administradores podem excluir usuários."
        self.user_service.delete_user(user_id)
        self.redirect("/admin/users")

    def list_administrators(self):
        if not self.check_admin_permission():
            return "Acesso negado. Apenas administradores podem gerenciar administradores."
        administrators = self.admin_service.get_all_administradores()
        return self.render("admin_administrators", administrators=administrators) 

    def add_administrator(self):
        if not self.check_admin_permission():
            return "Acesso negado. Apenas administradores podem adicionar administradores."
        if request.method == "GET":
            return self.render("admin_administrator_form", admin=None, action="/admin/administrators/add") 
        else:
            name = request.forms.get("name")
            email = request.forms.get("email")
            birthdate = request.forms.get("birthdate")
            password = request.forms.get("password")
            permissoes = request.forms.get("permissoes") 
            
            if self.admin_service.add_administrador(name, email, birthdate, password, permissoes):
                self.redirect("/admin/administrators")
            else:
                return "Erro ao adicionar administrador. Verifique se o email já existe."

    def edit_administrator(self, admin_id):
        if not self.check_admin_permission():
            return "Acesso negado. Apenas administradores podem editar administradores."
        admin = self.admin_service.get_administrador_by_id(admin_id)
        if not admin:
            return "Administrador não encontrado"

        if request.method == "GET":
            return self.render("admin_administrator_form", admin=admin, action=f"/admin/administrators/edit/{admin_id}")
        else:
            name = request.forms.get("name")
            email = request.forms.get("email")
            birthdate = request.forms.get("birthdate")
            permissoes = request.forms.get("permissoes")

            if self.admin_service.update_administrador(admin_id, name, email, birthdate, permissoes):
                self.redirect("/admin/administrators")
            else:
                return "Erro ao atualizar administrador."

    def delete_administrator(self, admin_id):
        if not self.check_admin_permission():
            return "Acesso negado. Apenas administradores podem excluir administradores."
        self.admin_service.delete_administrador(admin_id)
        self.redirect("/admin/administrators")



