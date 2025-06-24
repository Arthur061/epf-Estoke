from bottle import Bottle, request
from controllers.base_controller import BaseController, login_required

class HomeController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.setup_routes()

    def setup_routes(self):
        self.app.route("/home", method="GET", callback=self.home)

    @login_required
    def home(self):
        return self.render("home")

# Instanciação do Bottle e do controlador
home_routes = Bottle()
home_controller = HomeController(home_routes)
