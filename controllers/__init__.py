from bottle import Bottle
from .auth_controller import auth_routes
from .user_controller import user_routes

def init_controllers(app: Bottle):
    app.merge(auth_routes)
    app.merge(user_routes)
