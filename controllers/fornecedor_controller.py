from bottle import request, redirect
from .base_controller import BaseController 
from services.fornecedor_service import FornecedorService
from models.fornecedor import Fornecedor
from services.user_service import UserService

class FornecedorController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.fornecedor_service = FornecedorService()
        self.user_service = UserService()
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
        
        fornecedores = self.fornecedor_service.get_fornecedores_by_user(user_id)
        
        user_info = self.get_user_info(session)
        return self.render("fornecedores", fornecedores=fornecedores, **user_info)

    def novo_fornecedor(self):
        session = request.environ.get('beaker.session', {})
        user_id = session.get('user_id')
        if not user_id:
            return redirect('/login')

        if request.method == "POST":
            nome = request.forms.get("nome")
            cnpj = request.forms.get("cnpj")
            contato = request.forms.get("contato")
            endereco = request.forms.get("endereco")
            

            novo_fornecedor_obj = Fornecedor(
                id=None, 
                nome=nome, 
                user_id=user_id,
                cnpj=cnpj,
                contato=contato,
                endereco=endereco
            )

            if self.fornecedor_service.add_fornecedor(novo_fornecedor_obj):
                return redirect("/fornecedores")
            else:
                user_info = self.get_user_info(session)
                return self.render(
                    "fornecedor_form",
                    fornecedor=novo_fornecedor_obj, 
                    action="/fornecedores/novo",
                    error="Erro ao adicionar. O CNPJ pode já existir.",
                    **user_info
                )
        
        user_info = self.get_user_info(session)
        return self.render("fornecedor_form", fornecedor=None, action="/fornecedores/novo", **user_info)
    def editar_fornecedor(self, fornecedor_id):
        fornecedor = self.fornecedor_service.get_fornecedor_by_id(fornecedor_id)
        if not fornecedor:
            return "Fornecedor não encontrado!"
        
        session = request.environ.get('beaker.session', {})
        user_id = session.get('user_id')
        if not user_id or fornecedor.user_id != user_id:
            return "Acesso negado."

        if request.method == "POST":
            fornecedor.nome = request.forms.get("nome")
            fornecedor.cnpj = request.forms.get("cnpj")
            fornecedor.contato = request.forms.get("contato")
            fornecedor.endereco = request.forms.get("endereco")
            
            if self.fornecedor_service.update_fornecedor(fornecedor):
                return redirect("/fornecedores")
            else:
                return "Erro ao atualizar fornecedor."
        
        user_info = self.get_user_info(session)
        return self.render("fornecedor_form", fornecedor=fornecedor, action=f"/fornecedores/editar/{fornecedor_id}", **user_info)

    def excluir_fornecedor(self, fornecedor_id):
        fornecedor = self.fornecedor_service.get_fornecedor_by_id(fornecedor_id)
        session = request.environ.get('beaker.session', {})
        user_id = session.get('user_id')
        if not user_id or not fornecedor or fornecedor.user_id != user_id:
            return "Acesso negado."

        self.fornecedor_service.delete_fornecedor(fornecedor_id, user_id)
        return redirect("/fornecedores")
        
    # Função auxiliar para evitar repetição de código
    def get_user_info(self, session):
        user_id = session.get('user_id')
        if user_id:
            user = self.user_service.get_by_id(user_id)
            if user:
                return {
                    'user_name': user.name.split()[0],
                    'is_admin': user.tipo == 'administrador',
                    'session': session
                }
        return {'user_name': None, 'is_admin': False, 'session': session}