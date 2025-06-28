import os

class Config:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    # Configurações do servidor
    HOST = 'localhost'
    PORT = 8080
    DEBUG = True
    RELOADER = True

    TEMPLATE_PATH = os.path.join(BASE_DIR, 'views')
    STATIC_PATH = os.path.join(BASE_DIR, 'static')
    DATA_PATH = os.path.join(BASE_DIR, 'data')

    SECRET_KEY = os.environ.get('SECRET_KEY', 'chave-secreta-padrao-para-desenvolvimento')

