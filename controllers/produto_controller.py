from bottle import template, request, redirect

from services.fornecedor_service import FornecedorService 
from services.produto_service import ProdutoService 
from models.produto import Produto

class ProdutoController:
    def __init__(self, bottle_app):
        self.app = bottle_app
        self.produto_service = ProdutoService()
        self.fornecedor_service = FornecedorService()

        # --- REGISTRO DAS ROTAS ---
        self.app.route('/produtos', method='GET')(self.listar_produtos)
        self.app.route('/produtos/detalhes/<produto_id:int>', method='GET')(self.detalhes_produto)
        self.app.route('/produtos/adicionar', method='GET')(self.form_adicionar_produto)
        self.app.route('/produtos/adicionar', method='POST')(self.adicionar_produto)
        self.app.route('/produtos/editar/<produto_id:int>', method='GET')(self.form_editar_produto)
        self.app.route('/produtos/editar/<produto_id:int>', method='POST')(self.editar_produto)
        self.app.route('/produtos/excluir/<produto_id:int>', method='POST')(self.excluir_produto_post)
        self.app.route('/produtos/reposicao', method='GET')(self.listar_produtos_para_reposicao)

    def _get_session_data(self):
        """
        Função auxiliar que busca a sessão de forma segura.
        É a peça fundamental para corrigir o erro.
        """
        session = request.environ.get('beaker.session')
        if not session:
            return None, None, None 

        user_id = session.get('user_id', None)
        full_user_name = session.get('user_name', 'Usuário')
        first_name = full_user_name.split()[0] if full_user_name else 'Usuário'
        return session, user_id, first_name

    def listar_produtos(self):
        session, user_id, user_name = self._get_session_data()

        # ---- INÍCIO DA DEPURAÇÃO ----
        print(f"DEBUG: Sessão lida no /produtos: {session}")
        # ---- FIM DA DEPURAÇÃO ----
        
        if not user_id:
            return redirect('/login')

        try:
            produtos = self.produto_service.get_produtos_by_user_id(user_id)
            return template('produtos', produtos=produtos, user_name=user_name, user_id=user_id, session=session)
        except Exception as e:
            print(f"ERRO FATAL AO BUSCAR PRODUTOS: {e}")
            return "Ocorreu um erro crítico ao carregar seus produtos. Verifique o terminal."

    def detalhes_produto(self, produto_id):
        session, user_id, user_name = self._get_session_data()
        if not user_id: return redirect('/login')
        
        produto = self.produto_service.get_produto_by_id_and_user(produto_id, user_id)
        if produto:
            return template('produto_detalhes', produto=produto, user_name=user_name, user_id=user_id, session=session)
        return redirect('/produtos?error=not_found')

    def form_adicionar_produto(self):
        session, user_id, user_name = self._get_session_data()
        if not user_id: return redirect('/login')

        return template('produto_form', title='Adicionar Novo Produto', produto=None, action_url='/produtos/adicionar', user_name=user_name, user_id=user_id, session=session)

    def adicionar_produto(self):
        _session, user_id, _ = self._get_session_data()
        if not user_id: return redirect('/login')

        novo_produto = Produto(id=None, user_id=user_id, nome=request.forms.get('nome'), descricao=request.forms.get('descricao'), preco=float(request.forms.get('preco')), qtd_estoque=int(request.forms.get('qtd_estoque')), qtd_minima=int(request.forms.get('qtd_minima')), fornecedor_id=int(request.forms.get('fornecedor_id') or 0))
        self.produto_service.add_produto(novo_produto)
        redirect('/produtos?success=added')

    def form_editar_produto(self, produto_id):
        session, user_id, user_name = self._get_session_data()
        if not user_id: return redirect('/login')

        produto = self.produto_service.get_produto_by_id_and_user(produto_id, user_id)
        if produto:
            action_url = f'/produtos/editar/{produto_id}'
            return template('produto_form', title='Editar Produto', produto=produto, action_url=action_url, user_name=user_name, user_id=user_id, session=session)
        return redirect('/produtos?error=not_found')

    def editar_produto(self, produto_id):
        _session, user_id, _ = self._get_session_data()
        if not user_id: return redirect('/login')

        produto_atualizado = Produto(id=produto_id, user_id=user_id, nome=request.forms.get('nome'), descricao=request.forms.get('descricao'), preco=float(request.forms.get('preco')), qtd_estoque=int(request.forms.get('qtd_estoque')), qtd_minima=int(request.forms.get('qtd_minima')), fornecedor_id=int(request.forms.get('fornecedor_id') or 0))
        self.produto_service.update_produto(produto_atualizado)
        redirect('/produtos?success=updated')

    def excluir_produto_post(self, produto_id):
        _session, user_id, _ = self._get_session_data()
        if not user_id: return redirect('/login')
        
        deleted = self.produto_service.delete_produto(produto_id, user_id)
        redirect('/produtos?success=deleted' if deleted else '/produtos?error=delete_failed')
    
    # MÉTODO NOVO PARA A ROTA DE REPOSIÇÃO
    def listar_produtos_para_reposicao(self):
        session, user_id, user_name = self._get_session_data()
        if not user_id:
            return redirect('/login')

        try:
            produtos_para_reposicao = self.produto_service.get_produtos_para_reposicao(user_id)

            fornecedores_dict = self.fornecedor_service.get_all_fornecedores_as_dict(user_id)

            return template(
                'produto_reposicao', 
                produtos=produtos_para_reposicao,
                fornecedores=fornecedores_dict,
                user_name=user_name,
                user_id=user_id,
                session=session
            )
        except Exception as e:
            print(f"ERRO AO GERAR RELATÓRIO DE REPOSIÇÃO: {e}")
            return "Erro ao gerar relatório. Verifique os logs do servidor."
