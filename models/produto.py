import sqlite3
from .fornecedor import Fornecedor # Importar Fornecedor para referência

class Produto:
    def __init__(self, id, nome, descricao, preco, qtd_estoque, qtd_minima, fornecedor_id):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.qtd_estoque = qtd_estoque
        self.qtd_minima = qtd_minima
        self.fornecedor_id = fornecedor_id # Mantido como ID para persistência no banco

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "descricao": self.descricao,
            "preco": self.preco,
            "qtd_estoque": self.qtd_estoque,
            "qtd_minima": self.qtd_minima,
            "fornecedor_id": self.fornecedor_id
        }

    def verificar_reposicao(self):
        return self.qtd_estoque < self.qtd_minima

    def registrar_movimentacao(self, tipo, quantidade):
        if tipo == "entrada":
            self.qtd_estoque += quantidade
        elif tipo == "saida":
            self.qtd_estoque -= quantidade
        else:
            raise ValueError("Tipo de movimentação inválido. Use \'entrada\' ou \'saida\'.")

class ProdutoRepository:
    def __init__(self, db_path='database.db'):
        self.db_path = db_path
        self._create_table()

    def _get_connection(self):
        return sqlite3.connect(self.db_path)

    def _create_table(self):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS produtos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    descricao TEXT,
                    preco REAL,
                    qtd_estoque INTEGER,
                    qtd_minima INTEGER,
                    fornecedor_id INTEGER,
                    FOREIGN KEY (fornecedor_id) REFERENCES fornecedores(id)
                )
            """)
            conn.commit()

    def _row_to_produto(self, row):
        return Produto(
            id=row[0],
            nome=row[1],
            descricao=row[2],
            preco=row[3],
            qtd_estoque=row[4],
            qtd_minima=row[5],
            fornecedor_id=row[6]
        )

    def get_all(self):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nome, descricao, preco, qtd_estoque, qtd_minima, fornecedor_id FROM produtos")
            return [self._row_to_produto(row) for row in cursor.fetchall()]

    def get_by_id(self, produto_id):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nome, descricao, preco, qtd_estoque, qtd_minima, fornecedor_id FROM produtos WHERE id = ?", (produto_id,))
            row = cursor.fetchone()
            return self._row_to_produto(row) if row else None

    def add_produto(self, produto):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO produtos (nome, descricao, preco, qtd_estoque, qtd_minima, fornecedor_id) VALUES (?, ?, ?, ?, ?, ?)",
                (produto.nome, produto.descricao, produto.preco, produto.qtd_estoque, produto.qtd_minima, produto.fornecedor_id)
            )
            conn.commit()
            return cursor.lastrowid

    def update_produto(self, produto):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE produtos SET nome = ?, descricao = ?, preco = ?, qtd_estoque = ?, qtd_minima = ?, fornecedor_id = ? WHERE id = ?",
                (produto.nome, produto.descricao, produto.preco, produto.qtd_estoque, produto.qtd_minima, produto.fornecedor_id, produto.id)
            )
            conn.commit()
            return cursor.rowcount > 0

    def delete_produto(self, produto_id):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM produtos WHERE id = ?", (produto_id,))
            conn.commit()
            return cursor.rowcount > 0

produto_repository = ProdutoRepository()


