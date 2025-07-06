from bottle import Bottle, request
from .base_controller import BaseController
from services.user_service import UserService
from controllers.base_controller import login_required

class UserController(BaseController):
    def __init__(self, app):
        super().__init__(app)

        self.setup_routes()
        self.user_service = UserService()

    # Rotas User
    def setup_routes(self):
        self.app.route('/users', method='GET', callback=self.list_users)
        self.app.route('/users/add', method=['GET', 'POST'], callback=self.add_user)
        self.app.route('/users/edit/<user_id:int>', method=['GET', 'POST'], callback=self.edit_user)
        self.app.route('/users/delete/<user_id:int>', method='POST', callback=self.delete_user)

    @login_required
    def list_users(self):
        users = self.user_service.get_all()
        return self.render('users', users=users)

    @login_required
    def add_user(self):
        if request.method == 'GET':
            return self.render('user_form', user=None, action="/users/add", errors={})
        else:
            name = request.forms.get('name')
            email = request.forms.get('email')
            birthdate = request.forms.get('birthdate')
            password = request.forms.get('password') 
            
            errors = {}
            if not name:
                errors['name'] = "Nome é obrigatório"
            if not email or '@' not in email:
                errors['email'] = "Email inválido"
            
            if errors:
                return self.render('user_form', 
                                user={'name': name, 'email': email, 'birthdate': birthdate},
                                action="/users/add",
                                errors=errors)
            
            # Salva no banco
            success = self.user_service.save(name, email, birthdate, password)
            
            if not success:
                errors['email'] = "Email já cadastrado"
                return self.render('user_form', 
                                user={'name': name, 'email': email, 'birthdate': birthdate},
                                action="/users/add",
                                errors=errors)
            
            self.redirect('/users')

    def edit_user(self, user_id):
        user = self.user_service.get_by_id(user_id)
        if request.method == 'GET':
            user = self.user_service.get_by_id(user_id)
            if not user:
                return "Usuário não encontrado"
            return self.render('user_form', 
                            user=user, 
                            action=f"/users/edit/{user_id}",
                            errors={})

        else:
            name = request.forms.get('name')
            email = request.forms.get('email')
            birthdate = request.forms.get('birthdate')
            
            errors = {}
            if not name:
                errors['name'] = "Nome é obrigatório"
            if not email or '@' not in email:
                errors['email'] = "Email inválido"
            
            if errors:
                user_data = {'id': user_id, 'name': name, 'email': email, 'birthdate': birthdate}
                return self.render('user_form', 
                                user=user_data, 
                                action=f"/users/edit/{user_id}",
                                errors=errors)
            
            success = self.user_service.edit_user(user_id, name, email, birthdate)
            
            if not success:
                errors['email'] = "Email já cadastrado (por outro usuário)"
                user_data = {'id': user_id, 'name': name, 'email': email, 'birthdate': birthdate}
                return self.render('user_form', 
                                user=user_data, 
                                action=f"/users/edit/{user_id}",
                                errors=errors)
            
            self.redirect('/users')


    def delete_user(self, user_id):
        self.user_service.delete_user(user_id)
        self.redirect('/users')


user_routes = Bottle()
user_controller = UserController(user_routes)
