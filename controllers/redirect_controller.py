from bottle import Bottle, redirect, request
from controllers.base_controller import BaseController, login_required

class RedirectController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.setup_routes()

    def setup_routes(self):
        self.app.route("/users", method="GET", callback=self.redirect_to_home)

    @login_required
    def redirect_to_home(self):
        session = request.environ.get("beaker.session", {})
        if session.get("user_id"):
            return redirect("/home")
        return redirect("/login")

redirect_routes = Bottle()
redirect_controller = RedirectController(redirect_routes)