from bottle import request, redirect
from .base_controller import BaseController 
from services.movimentacao_service import MovimentacaoService
from services.produto_service import ProdutoService
from services.user_service import UserService 

class MovimentacaoController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.movimentacao_service = MovimentacaoService()
        self.produto_service = ProdutoService()
        self.user_service = UserService()  
        self.setup_routes()

    def setup_routes(self):
        """Registra as rotas de movimentação."""
        self.app.route("/movimentacoes", method="GET", callback=self.listar_movimentacoes)
        self.app.route("/movimentacoes", method="POST", callback=self.registrar_movimentacao)

    def listar_movimentacoes(self):
        """Exibe o histórico de movimentações e o formulário de registro."""
        session = request.environ.get('beaker.session', {})
        user_id = session.get('user_id')
        if not user_id:
            return redirect('/login')

        try:
            movimentacoes = self.movimentacao_service.get_movimentacoes_by_user(user_id)
            
            produtos = self.produto_service.get_produtos_by_user_id(user_id)
            
            user_info = self.get_user_info(session)
            
            produtos_dict = {p.id: p.nome for p in produtos}

            return self.render("movimentacoes", 
                            movimentacoes=movimentacoes, 
                            produtos=produtos, 
                            produtos_dict=produtos_dict,
                            **user_info)
        except Exception as e:
            print(f"ERRO AO LISTAR MOVIMENTAÇÕES: {e}")
            return "Erro ao carregar a página de movimentações."

    # Em controllers/movimentacao_controller.py

    def registrar_movimentacao(self):
        """Processa o registro de uma nova movimentação."""
        session = request.environ.get('beaker.session', {})
        user_id = session.get('user_id')
        if not user_id:
            return redirect('/login')

        produto_id = int(request.forms.get('produto_id'))
        tipo = request.forms.get('tipo')
        quantidade = int(request.forms.get('quantidade'))
        
        try:
            if tipo == 'entrada':
                self.movimentacao_service.registrar_entrada(produto_id, quantidade, user_id)
            elif tipo == 'saida':
                self.movimentacao_service.registrar_saida(produto_id, quantidade, user_id)
            else:
                return "Tipo de movimentação inválido."

            produto = self.produto_service.get_produto_by_id_and_user(produto_id, user_id)
            if produto:
                if tipo == 'entrada':
                    produto.qtd_estoque += quantidade
                elif tipo == 'saida':
                    produto.qtd_estoque -= quantidade
                
                self.produto_service.update_produto(produto)

        except Exception as e:
            print(f"ERRO AO REGISTRAR MOVIMENTAÇÃO: {e}")
        
        return redirect('/movimentacoes')

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