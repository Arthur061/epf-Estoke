from bottle import Bottle
from beaker.middleware import SessionMiddleware
from config import Config

class App:
    def __init__(self):
        self.bottle = Bottle()
        self.config = Config()
        self.bottle.TEMPLATE_PATH = [self.config.TEMPLATE_PATH]

    # conf da sessão 1h
        self.session_opts = {
            'session.type': 'file',  
            'session.data_dir': './data/sessions',
            'session.cookie_expires': 3600,  
            'session.auto': True,
            'session.secret': self.config.SECRET_KEY
        }

        self.app = SessionMiddleware(self.bottle, self.session_opts)

    def setup_routes(self):
        from controllers import init_controllers

        print('🚀 Inicializa rotas!')
        init_controllers(self.bottle)


    def run(self):
        self.setup_routes()
        from bottle import run
        run(app=self.app, 
            host=self.config.HOST,
            port=self.config.PORT,
            debug=self.config.DEBUG,
            reloader=self.config.RELOADER)


def create_app():
    return App()
