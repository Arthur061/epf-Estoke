import sqlite3
from models.fornecedor import Fornecedor

class FornecedorService:
    def __init__(self, db_path='database.db'):
        self.db_path = db_path

    def _get_connection(self):
        """Cria e retorna uma conexão com o banco de dados"""
        return sqlite3.connect(self.db_path)

    def _row_to_fornecedor(self, row):
        """Converte uma linha do banco para objeto Fornecedor"""
        if not row:
            return None
        return Fornecedor(
            id=row[0],
            nome=row[1],
            contato=row[2],
            endereco=row[3],
            cnpj=row[4],
            user_id=row[5]
        )

    def get_fornecedores_by_user(self, user_id):
        """Retorna todos os fornecedores de um usuário específico."""
        with self._get_connection() as conn:

            cursor = conn.cursor()
            cursor.execute("SELECT id, nome, contato, endereco, cnpj, user_id FROM fornecedores WHERE user_id = ?", (user_id,))
            return [self._row_to_fornecedor(row) for row in cursor.fetchall()]

    def get_fornecedor_by_id(self, fornecedor_id):
        """Busca um fornecedor pelo ID"""
        with self._get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute("SELECT id, nome, contato, endereco, cnpj, user_id FROM fornecedores WHERE id = ?", (fornecedor_id,))
            row = cursor.fetchone()
            return self._row_to_fornecedor(row)

    def add_fornecedor(self, fornecedor):
        """Adiciona um novo fornecedor, incluindo os novos campos"""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO fornecedores (nome, contato, endereco, cnpj, user_id) VALUES (?, ?, ?, ?, ?)",
                (
                    fornecedor.nome,
                    fornecedor.contato,
                    fornecedor.endereco,
                    fornecedor.cnpj,
                    fornecedor.user_id
                )
            )
            conn.commit()
            return cursor.lastrowid

    def update_fornecedor(self, fornecedor):
        """Atualiza os dados de um fornecedor existente"""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """UPDATE fornecedores 
                   SET nome = ?, contato = ?, endereco = ?, cnpj = ? 
                   WHERE id = ? AND user_id = ?""",
                (
                    fornecedor.nome,
                    fornecedor.contato,
                    fornecedor.endereco,
                    fornecedor.cnpj,
                    fornecedor.id,
                    fornecedor.user_id
                )
            )
            conn.commit()
            return cursor.rowcount > 0

    def delete_fornecedor(self, fornecedor_id, user_id):
        """Remove um fornecedor pelo ID, garantindo que pertence ao usuário"""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM fornecedores WHERE id = ? AND user_id = ?", (fornecedor_id, user_id))
            conn.commit()
            return cursor.rowcount > 0
        
    def get_all_fornecedores_as_dict(self, user_id):
        """
        Busca todos os fornecedores de um usuário e os retorna como um dicionário
        no formato {id_do_fornecedor: nome_do_fornecedor}.
        Isso é útil para buscas rápidas de nome no template.
        """
        fornecedores_list = self.get_fornecedores_by_user(user_id)

        if not fornecedores_list:
            return {}

        return {fornecedor.id: fornecedor.nome for fornecedor in fornecedores_list}