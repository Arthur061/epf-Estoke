from bottle import request, static_file, redirect as bottle_redirect
from bottle import template as render_template
from functools import wraps
from bottle import template, request
from services.user_service import UserService

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not request.environ.get('beaker.session', {}).get('user_id'):
            return bottle_redirect('/login')
        return func(*args, **kwargs)
    return wrapper

class BaseController:
    def __init__(self, app):
        self.app = app
        self._setup_base_routes()

    def _setup_base_routes(self):
        """Configura rotas básicas comuns a todos os controllers"""
        self.app.route('/', method='GET', callback=self.home_redirect)
        self.app.route('/helper', method=['GET'], callback=self.helper)

        # Rota para arquivos estáticos (CSS, JS, imagens)
        self.app.route('/static/<filename:path>', callback=self.serve_static)

    def home_redirect(self):
        bottle_redirect('/login')

    def helper(self):
        return self.render('helper-final')


    def serve_static(self, filename):
        """Serve arquivos estáticos da pasta static/"""
        return static_file(filename, root='./static')


    def render(self, template_name, **kwargs):
        session = request.environ.get('beaker.session')
        
        kwargs['session'] = session

        user_id = session.get('user_id')

        if user_id:
            user_service = UserService()
            user = user_service.get_by_id(user_id)
            
            user_name = "Usuário"
            if user and user.name and user.name.strip():
                user_name = user.name.strip().split()[0]
            
            kwargs['user_name'] = user_name

        return template(template_name, **kwargs)


    def redirect(self, path):
        """Método auxiliar para redirecionamento"""
        from bottle import redirect as bottle_redirect
        return bottle_redirect(path)
