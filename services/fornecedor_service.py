import sqlite3
from models.fornecedor import Fornecedor

class FornecedorService:
    def __init__(self, db_path='database.db'):
        self.db_path = db_path
        self._initialize_database()

    def _get_connection(self):
        """Cria e retorna uma conexão com o banco de dados"""
        return sqlite3.connect(self.db_path)

    def _initialize_database(self):
        """Cria a tabela de fornecedores se não existir"""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS fornecedores (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    contato TEXT,
                    endereco TEXT,
                    cnpj TEXT UNIQUE,
                    produtos TEXT
                )
            """)
            conn.commit()

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
            produtos=row[5].split('|') if row[5] else []
        )

    def get_all_fornecedores(self):
        """Retorna todos os fornecedores cadastrados"""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM fornecedores")
            return [self._row_to_fornecedor(row) for row in cursor.fetchall()]

    def get_fornecedor_by_id(self, fornecedor_id):
        """Busca um fornecedor pelo ID"""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM fornecedores WHERE id = ?", (fornecedor_id,))
            return self._row_to_fornecedor(cursor.fetchone())

    def add_fornecedor(self, fornecedor):
        """Adiciona um novo fornecedor"""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO fornecedores (nome, contato, endereco, cnpj, produtos) VALUES (?, ?, ?, ?, ?)",
                (
                    fornecedor.nome,
                    fornecedor.contato,
                    fornecedor.endereco,
                    fornecedor.cnpj,
                    '|'.join(fornecedor.produtos) if fornecedor.produtos else None
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
                SET nome = ?, contato = ?, endereco = ?, cnpj = ?, produtos = ? 
                WHERE id = ?""",
                (
                    fornecedor.nome,
                    fornecedor.contato,
                    fornecedor.endereco,
                    fornecedor.cnpj,
                    '|'.join(fornecedor.produtos) if fornecedor.produtos else None,
                    fornecedor.id
                )
            )
            conn.commit()
            return cursor.rowcount > 0

    def delete_fornecedor(self, fornecedor_id):
        """Remove um fornecedor pelo ID"""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM fornecedores WHERE id = ?", (fornecedor_id,))
            conn.commit()
            return cursor.rowcount > 0

    def get_next_id(self):
        """Retorna o próximo ID disponível (para compatibilidade com sistema antigo)"""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT MAX(id) FROM fornecedores")
            max_id = cursor.fetchone()[0]
            return max_id + 1 if max_id else 1