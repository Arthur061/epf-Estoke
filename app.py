import os
from bottle import Bottle, run, static_file, redirect, TEMPLATE_PATH
from beaker.middleware import SessionMiddleware
from config import Config

from controllers.auth_controller import AuthController
from controllers.produto_controller import ProdutoController 

class App:
    def __init__(self):
        """
        Construtor da classe principal da aplicação.
        """
        self.bottle = Bottle()
        self.config = Config()
        
        TEMPLATE_PATH.insert(0, self.config.TEMPLATE_PATH)

        session_dir = os.path.join(self.config.DATA_PATH, 'sessions')
        if not os.path.exists(session_dir):
            os.makedirs(session_dir)

        session_opts = {
            'session.type': 'file',
            'session.data_dir': session_dir,
            'session.cookie_expires': 3600,
            'session.auto': True,
            'session.secret': self.config.SECRET_KEY
        }
        self.app = SessionMiddleware(self.bottle, session_opts)

    def setup_routes(self):
        """
        Cria as instâncias dos controllers, que por sua vez registram suas próprias rotas.
        """
        print("🚀 Inicializando rotas da aplicação...")
        
        # --- CORRETO: Cria as instâncias aqui ---
        # Ao criar o objeto, o __init__ do controller é chamado, e ele mesmo
        # configura suas rotas usando a instância do 'self.bottle' que passamos.
        auth_controller = AuthController(self.bottle)
        produto_controller = ProdutoController(self.bottle)
        
        # --- Rotas Globais ---
        @self.bottle.route('/')
        def index():
            # A página inicial deve ser a lista de produtos (ou a de login se não estiver logado)
            redirect('/produtos')

        @self.bottle.route('/static/<filename:path>')
        def server_static(filename):
            """Serve arquivos estáticos (CSS, JS, imagens)"""
            return static_file(filename, root=self.config.STATIC_PATH)
        
        print("✅ Rotas inicializadas com sucesso!")

    def run(self):
        """
        Inicia o processo de configuração de rotas e executa o servidor web.
        """
        self.setup_routes()
        
        print(f"🌍 Servidor iniciado em http://{self.config.HOST}:{self.config.PORT}")
        print("   (Pressione CTRL+C para parar o servidor)")
        
        run(
            app=self.app,
            host=self.config.HOST,
            port=self.config.PORT,
            debug=self.config.DEBUG,
            reloader=self.config.RELOADER
        )

# teste main
if __name__ == '__main__':
    app_instance = App()
    app_instance.run()
