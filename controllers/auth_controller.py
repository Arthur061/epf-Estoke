from bottle import Bottle, request, redirect
from controllers.base_controller import BaseController
from services.user_service import UserService
import bcrypt

class AuthController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.user_service = UserService()
        self.setup_routes()
    
    def setup_routes(self):
        self.app.route('/login', method=['GET', 'POST'], callback=self.login)
        self.app.route('/register', method=['GET', 'POST'], callback=self.register)
        self.app.route('/logout', method='GET', callback=self.logout)
    
    def login(self):
        if request.method == 'GET':
            return self.render('login', error=None)
        else:
            email = request.forms.get('email')
            password = request.forms.get('password')
            user = self.user_service.authenticate(email, password)
            
            if user:
                session = request.environ['beaker.session']
                session['user_id'] = user['id']
                session.save()
                self.redirect('/users')
            else:
                return self.render('login', error="Credenciais inválidas")
    
    def register(self):
        if request.method == 'GET':
            return self.render('register')
        else:
            name = request.forms.get('name')
            email = request.forms.get('email')
            birthdate = request.forms.get('birthdate')
            password = request.forms.get('password')
            confirm_password = request.forms.get('confirm_password')
            
            if password != confirm_password:
                return self.render('register', error="As senhas não coincidem")
            
            success = self.user_service.save(name, email, birthdate, password)
            
            if success:
                redirect('/login')
            else:
                return self.render('register', error="Email já cadastrado")
    
    def logout(self):
        session = request.environ.get('beaker.session', {})
        session.delete()
        self.redirect('/login')

# Cria as rotas para autenticação
auth_routes = Bottle()
auth_controller = AuthController(auth_routes)