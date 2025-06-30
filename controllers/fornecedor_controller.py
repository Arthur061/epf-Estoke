from bottle import request, redirect
from .base_controller import BaseController 
from services.fornecedor_service import FornecedorService

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
        # É uma boa prática usar POST para ações de exclusão
        self.app.route("/fornecedores/excluir/<fornecedor_id:int>", method="POST", callback=self.excluir_fornecedor) 

    def listar_fornecedores(self):
        fornecedores = self.fornecedor_service.get_all_fornecedores()
        # O método 'render' deve existir no seu BaseController
        return self.render("fornecedores", fornecedores=fornecedores)

    def novo_fornecedor(self):
        if request.method == "POST":
            nome = request.forms.get("nome")
            contato = request.forms.get("contato")
            endereco = request.forms.get("endereco")
            cnpj = request.forms.get("cnpj")

            if self.fornecedor_service.save(nome, contato, endereco, cnpj):
                redirect("/fornecedores")
            else:
                return "Erro ao adicionar fornecedor. Verifique se o CNPJ já existe."
        
        return self.render("fornecedor_form", fornecedor=None, action="/fornecedores/novo")

    def editar_fornecedor(self, fornecedor_id):
        fornecedor = self.fornecedor_service.get_fornecedor_by_id(fornecedor_id)
        if not fornecedor:
            return "Fornecedor não encontrado!"

        if request.method == "POST":
            nome = request.forms.get("nome")
            contato = request.forms.get("contato")
            endereco = request.forms.get("endereco")
            cnpj = request.forms.get("cnpj")

            if self.fornecedor_service.update_fornecedor(fornecedor_id, nome, contato, endereco, cnpj):
                redirect("/fornecedores")
            else:
                return "Erro ao atualizar fornecedor."
        
        return self.render("fornecedor_form", fornecedor=fornecedor, action=f"/fornecedores/editar/{fornecedor_id}")

    def excluir_fornecedor(self, fornecedor_id):
        self.fornecedor_service.delete_fornecedor(fornecedor_id)
        redirect("/fornecedores")