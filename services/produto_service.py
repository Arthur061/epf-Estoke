from models.produto import ProdutoRepository, Produto

class ProdutoService:
    """
    Camada de serviço que contém a lógica de negócio para produtos.
    Ela atua como intermediária entre o Controller e o Repository.
    """
    def __init__(self):
        self.repository = ProdutoRepository()

    def get_produtos_by_user_id(self, user_id):
        """ Obtém todos os produtos de um usuário. """
        return self.repository.get_by_user_id(user_id)

    def get_produto_by_id_and_user(self, produto_id, user_id):
        """ Obtém um produto específico, garantindo que pertence ao usuário. """
        return self.repository.get_by_id_and_user(produto_id, user_id)

    def add_produto(self, produto):
        """ Adiciona um novo produto. """
        return self.repository.add(produto)

    def update_produto(self, produto):
        """ Atualiza um produto existente. """
        produto_existente = self.repository.get_by_id_and_user(produto.id, produto.user_id)
        if not produto_existente:
            raise ValueError("Produto não encontrado ou não pertence ao usuário.")
        return self.repository.update(produto)

    def delete_produto(self, produto_id, user_id):
        """ Deleta um produto. """
        return self.repository.delete(produto_id, user_id)

    def get_produtos_para_reposicao(self, user_id):
        """ Obtém produtos com estoque baixo para um usuário específico. """
        return self.repository.get_para_reposicao_by_user_id(user_id)