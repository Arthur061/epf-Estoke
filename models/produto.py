import sqlite3

class Produto:
    """
    Representa o modelo de um produto. Inclui o user_id para associar
    o produto a um usuário específico.
    """
    def __init__(self, id, user_id, nome, descricao, preco, qtd_estoque, qtd_minima, fornecedor_id):
        self.id = id
        self.user_id = user_id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.qtd_estoque = qtd_estoque
        self.qtd_minima = qtd_minima
        self.fornecedor_id = fornecedor_id

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "nome": self.nome,
            "descricao": self.descricao,
            "preco": self.preco,
            "qtd_estoque": self.qtd_estoque,
            "qtd_minima": self.qtd_minima,
            "fornecedor_id": self.fornecedor_id
        }

class ProdutoRepository:
    """
    Responsável pela comunicação direta com o banco de dados para
    operações relacionadas a produtos.
    """
    def __init__(self, db_path='database.db'):
        self.db_path = db_path

    def _get_connection(self):
        return sqlite3.connect(self.db_path)

    def _row_to_produto(self, row):
        if row:
            return Produto(id=row[0], user_id=row[1], nome=row[2], descricao=row[3],
                           preco=row[4], qtd_estoque=row[5], qtd_minima=row[6], fornecedor_id=row[7])
        return None

    def get_by_user_id(self, user_id):
        """ Retorna todos os produtos de um usuário específico. """
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, user_id, nome, descricao, preco, qtd_estoque, qtd_minima, fornecedor_id FROM produtos WHERE user_id = ?", (user_id,))
            return [self._row_to_produto(row) for row in cursor.fetchall()]

    def get_by_id_and_user(self, produto_id, user_id):
        """ Retorna um produto específico se ele pertencer ao usuário. """
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, user_id, nome, descricao, preco, qtd_estoque, qtd_minima, fornecedor_id FROM produtos WHERE id = ? AND user_id = ?", (produto_id, user_id))
            row = cursor.fetchone()
            return self._row_to_produto(row)

    def add(self, produto):
        """ Adiciona um novo produto ao banco de dados. """
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO produtos (user_id, nome, descricao, preco, qtd_estoque, qtd_minima, fornecedor_id) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (produto.user_id, produto.nome, produto.descricao, produto.preco, produto.qtd_estoque, produto.qtd_minima, produto.fornecedor_id)
            )
            conn.commit()
            return cursor.lastrowid

    def update(self, produto):
        """ Atualiza um produto existente, verificando o user_id por segurança. """
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE produtos SET nome = ?, descricao = ?, preco = ?, qtd_estoque = ?, qtd_minima = ?, fornecedor_id = ? WHERE id = ? AND user_id = ?",
                (produto.nome, produto.descricao, produto.preco, produto.qtd_estoque, produto.qtd_minima, produto.fornecedor_id, produto.id, produto.user_id)
            )
            conn.commit()
            return cursor.rowcount > 0

    def delete(self, produto_id, user_id):
        """ Deleta um produto, verificando o user_id por segurança. """
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM produtos WHERE id = ? AND user_id = ?", (produto_id, user_id))
            conn.commit()
            return cursor.rowcount > 0
