import sqlite3
from datetime import datetime
from .produto import Produto, ProdutoRepository 

class Movimentacao:
    def __init__(self, id, produto_id, data, tipo, qtd, user_id):
        self.id = id
        self.produto_id = produto_id
        self.data = data
        self.tipo = tipo
        self.qtd = qtd
        self.user_id = user_id

    def to_dict(self):
        return {
            "id": self.id,
            "produto_id": self.produto_id,
            "data": self.data.isoformat() if isinstance(self.data, datetime) else self.data,
            "tipo": self.tipo,
            "qtd": self.qtd
        }

    def registrar(self):
        print(f"Movimentação registrada: Produto ID {self.produto_id}, Tipo: {self.tipo}, Quantidade: {self.qtd}")

class MovimentacaoRepository:
    def __init__(self, db_path='database.db'):
        self.db_path = db_path

    def _get_connection(self):
        return sqlite3.connect(self.db_path)

    def _row_to_movimentacao(self, row):
        if not row:
            return None
        return Movimentacao(
            id=row[0], 
            produto_id=row[1], 
            data=datetime.fromisoformat(row[2]), 
            tipo=row[3], 
            qtd=row[4], 
            user_id=row[5]
        )

    def add_movimentacao(self, movimentacao):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO movimentacoes (produto_id, data, tipo, qtd, user_id) VALUES (?, ?, ?, ?, ?)",
                (movimentacao.produto_id, movimentacao.data.isoformat(), movimentacao.tipo, movimentacao.qtd, movimentacao.user_id)
            )
            conn.commit()
            return cursor.lastrowid

    def get_all_by_user(self, user_id):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM movimentacoes WHERE user_id = ? ORDER BY data DESC", (user_id,))
            return [self._row_to_movimentacao(row) for row in cursor.fetchall()]

    def get_by_id(self, movimentacao_id):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM movimentacoes WHERE id = ?", (movimentacao_id,))
            row = cursor.fetchone()
            return self._row_to_movimentacao(row)

    def delete_movimentacao(self, movimentacao_id):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM movimentacoes WHERE id = ?", (movimentacao_id,))
            conn.commit()
            return cursor.rowcount > 0
