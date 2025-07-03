from bottle import request, redirect
from .base_controller import BaseController 
from services.fornecedor_service import FornecedorService
from models.fornecedor import Fornecedor

class FornecedorController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.fornecedor_service = FornecedorService()
        self.setup_routes()

    def setup_routes(self):
        """Registra as rotas do fornecedor na instância do app Bottle."""
        self.app.route("/fornecedores", method="GET", callback=self.listar_fornecedores)
        self.app.route("/fornecedores/novo", method=["GET", "POST"], callback=self.novo_fornecedor)
        self.app.route("/fornecedores/editar/<fornecedor_id:int>", method=["GET", "POST"], callback=self.editar_fornecedor)
        self.app.route("/fornecedores/excluir/<fornecedor_id:int>", method="POST", callback=self.excluir_fornecedor) 

    def listar_fornecedores(self):
        session = request.environ.get('beaker.session', {})
        user_id = session.get('user_id')
        if not user_id:
            return redirect('/login')
        
        # Busca apenas os fornecedores do usuário logado
        fornecedores = self.fornecedor_service.get_fornecedores_by_user(user_id)
        return self.render("fornecedores", fornecedores=fornecedores)

    def novo_fornecedor(self):
        session = request.environ.get('beaker.session', {})
        user_id = session.get('user_id')
        if not user_id:
            return redirect('/login')

        if request.method == "POST":
            nome = request.forms.get("nome")
            
            novo_fornecedor_obj = Fornecedor(id=None, nome=nome, user_id=user_id)

            if self.fornecedor_service.add_fornecedor(novo_fornecedor_obj):
                return redirect("/fornecedores")
            else:
                return self.render("fornecedor_form",
                                   fornecedor=None,
                                   action="/fornecedores/novo",
                                   error="Erro ao adicionar fornecedor.")
        
        return self.render("fornecedor_form", fornecedor=None, action="/fornecedores/novo")

    def editar_fornecedor(self, fornecedor_id):
        fornecedor = self.fornecedor_service.get_fornecedor_by_id(fornecedor_id)
        if not fornecedor:
            return "Fornecedor não encontrado!"
        
        # Checagem de segurança para garantir que o usuário só edite seus próprios fornecedores
        session = request.environ.get('beaker.session', {})
        user_id = session.get('user_id')
        if not user_id or fornecedor.user_id != user_id:
            return "Acesso negado."

        if request.method == "POST":
            fornecedor.nome = request.forms.get("nome")
            
            if self.fornecedor_service.update_fornecedor(fornecedor):
                return redirect("/fornecedores")
            else:
                return "Erro ao atualizar fornecedor."
        
        return self.render("fornecedor_form", fornecedor=fornecedor, action=f"/fornecedores/editar/{fornecedor_id}")

    def excluir_fornecedor(self, fornecedor_id):
        # Checagem de segurança
        fornecedor = self.fornecedor_service.get_fornecedor_by_id(fornecedor_id)
        session = request.environ.get('beaker.session', {})
        user_id = session.get('user_id')
        if not user_id or not fornecedor or fornecedor.user_id != user_id:
            return "Acesso negado."

        self.fornecedor_service.delete_fornecedor(fornecedor_id)
        return redirect("/fornecedores")
