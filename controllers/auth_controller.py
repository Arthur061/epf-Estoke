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
        self.app.route('/home', method='GET', callback=self.pagina_home)
        self.app.route('/login-sucesso', method='GET', callback=self.login_bem_sucedido)
        self.app.route('/logout_and_register', method='GET', callback=self.logout_and_register)
    
    def login(self):
        """Lida com o processo de login."""
        if request.method == 'GET':
            return self.render('login', error=None)
        
        email = request.forms.get('email')
        password = request.forms.get('password')
        
        user = self.user_service.authenticate(email, password)
        
        if user:
            
            print(">>> LOGIN BEM-SUCEDIDO. Redirecionando para /home...")
    
            # ---- INÍCIO DA DEPURAÇÃO ----
            print(f"DEBUG: Objeto 'user' recebido pelo controller: {user}") 
            # ---- FIM DA DEPURAÇÃO ----

            session = request.environ['beaker.session']
            session['user_id'] = user['id']
            session['user_name'] = user['name'] 
            session.save()

            # ---- INÍCIO DA DEPURAÇÃO ----
            print(f"DEBUG: Dados salvos na sessão: {session}")
            # ---- FIM DA DEPURAÇÃO ----
            
            return redirect('/home')
        else:
            print(">>> LOGIN FALHOU. Renderizando a página de login com erro...")

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
            
            if email.lower() == 'arthuralves6622@gmail.com':
                tipo = 'administrador'
            else:
                tipo = 'comum'

            success = self.user_service.save(name, email, birthdate, password, tipo=tipo)
            
            if success:
                return redirect('/login')
            else:
                return self.render('register', error="Email já cadastrado")
    
    def logout(self):
        session = request.environ.get('beaker.session', {})
        session.delete()
        return self.redirect('/login')
    
    def logout_and_register(self):
        """Desconecta o usuário e o redireciona para a página de registro."""
        session = request.environ.get('beaker.session', {})
        session.delete()
        return redirect('/register')
    
    def pagina_home(self):
        session = request.environ.get('beaker.session')
        user_id = session.get('user_id')

        if not user_id:
            return redirect('/login')

        user = self.user_service.get_by_id(user_id)
        user_name = user.name.split()[0] if user else "Usuário"

        user_name = "Usuário"

        if user and user.name and user.name.strip():
            user_name = user.name.strip().split()[0]

        
        return self.render('home_template', user_name=user_name)

    def login_bem_sucedido(self):
        print(">>> O login foi validado, redirecionando para /home...")
        return redirect('/home')

    
auth_routes = Bottle()
auth_controller = AuthController(auth_routes)
