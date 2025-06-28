import sqlite3
from datetime import datetime
from .produto import Produto, ProdutoRepository # Importar Produto e ProdutoRepository

class Movimentacao:
    def __init__(self, id, produto_id, data, tipo, qtd):
        self.id = id
        self.produto_id = produto_id  # Armazena apenas o ID do produto
        self.data = data
        self.tipo = tipo
        self.qtd = qtd

    def to_dict(self):
        return {
            "id": self.id,
            "produto_id": self.produto_id,
            "data": self.data.isoformat() if isinstance(self.data, datetime) else self.data,
            "tipo": self.tipo,
            "qtd": self.qtd
        }

    def registrar(self):
        # Lógica para registrar a movimentação
        print(f"Movimentação registrada: Produto ID {self.produto_id}, Tipo: {self.tipo}, Quantidade: {self.qtd}")

class MovimentacaoRepository:
    def __init__(self, db_path='database.db'):
        self.db_path = db_path
        self._create_table()

    def _get_connection(self):
        return sqlite3.connect(self.db_path)

    def _create_table(self):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS movimentacoes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    produto_id INTEGER NOT NULL,
                    data TEXT NOT NULL,
                    tipo TEXT NOT NULL,
                    qtd INTEGER NOT NULL,
                    FOREIGN KEY (produto_id) REFERENCES produtos(id)
                )
            """
            )
            conn.commit()

    def _row_to_movimentacao(self, row):
        return Movimentacao(
            id=row[0],
            produto_id=row[1],
            data=datetime.fromisoformat(row[2]),
            tipo=row[3],
            qtd=row[4]
        )

    def add_movimentacao(self, movimentacao):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO movimentacoes (produto_id, data, tipo, qtd) VALUES (?, ?, ?, ?)",
                (movimentacao.produto_id, movimentacao.data.isoformat(), movimentacao.tipo, movimentacao.qtd)
            )
            conn.commit()
            return cursor.lastrowid

    def get_all(self):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, produto_id, data, tipo, qtd FROM movimentacoes")
            return [self._row_to_movimentacao(row) for row in cursor.fetchall()]

    def get_by_id(self, movimentacao_id):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, produto_id, data, tipo, qtd FROM movimentacoes WHERE id = ?", (movimentacao_id,))
            row = cursor.fetchone()
            return self._row_to_movimentacao(row) if row else None

    def update_movimentacao(self, movimentacao):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE movimentacoes SET produto_id = ?, data = ?, tipo = ?, qtd = ? WHERE id = ?",
                (movimentacao.produto_id, movimentacao.data.isoformat(), movimentacao.tipo, movimentacao.qtd, movimentacao.id)
            )
            conn.commit()
            return cursor.rowcount > 0

    def delete_movimentacao(self, movimentacao_id):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM movimentacoes WHERE id = ?", (movimentacao_id,))
            conn.commit()
            return cursor.rowcount > 0
