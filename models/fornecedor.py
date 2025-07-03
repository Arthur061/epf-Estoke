import sqlite3

class Fornecedor:
    def __init__(self, id, nome, user_id, contato=None, endereco=None, cnpj=None):
        self.id = id
        self.nome = nome
        self.user_id = user_id
        self.contato = contato
        self.endereco = endereco
        self.cnpj = cnpj

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "user_id": self.user_id, 
            "contato": self.contato,
            "endereco": self.endereco,
            "cnpj": self.cnpj
        }

class FornecedorRepository:
    def __init__(self, db_path='database.db'):
        self.db_path = db_path
        self._create_table()

    def _get_connection(self):
        return sqlite3.connect(self.db_path)

    def _create_table(self):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS fornecedores (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    contato TEXT,
                    endereco TEXT,
                    cnpj TEXT UNIQUE,
                    user_id INTEGER NOT NULL, -- <-- MUDANÇA: Coluna para ligar ao usuário
                    FOREIGN KEY (user_id) REFERENCES users(id) -- Boa prática
                )
            """)
            conn.commit()

    def _row_to_fornecedor(self, row):
        return Fornecedor(
            id=row[0],
            nome=row[1],
            contato=row[2],
            endereco=row[3],
            cnpj=row[4],
            user_id=row[5] 
        )

    def get_all_by_user(self, user_id):
        with self._get_connection() as conn:
            conn.row_factory = lambda cursor, row: row 
            cursor = conn.cursor()
            cursor.execute("SELECT id, nome, contato, endereco, cnpj, user_id FROM fornecedores WHERE user_id = ?", (user_id,))
            return [self._row_to_fornecedor(row) for row in cursor.fetchall()]

    def get_by_id(self, fornecedor_id):
        with self._get_connection() as conn:
            conn.row_factory = lambda cursor, row: row
            cursor = conn.cursor()
            cursor.execute("SELECT id, nome, contato, endereco, cnpj, user_id FROM fornecedores WHERE id = ?", (fornecedor_id,))
            row = cursor.fetchone()
            return self._row_to_fornecedor(row) if row else None

    def add_fornecedor(self, fornecedor):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO fornecedores (nome, contato, endereco, cnpj, user_id) VALUES (?, ?, ?, ?, ?)",
                (fornecedor.nome, fornecedor.contato, fornecedor.endereco, fornecedor.cnpj, fornecedor.user_id) 
            )
            conn.commit()
            return cursor.lastrowid

    def update_fornecedor(self, fornecedor):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE fornecedores SET nome = ?, contato = ?, endereco = ?, cnpj = ? WHERE id = ? AND user_id = ?", 
                (fornecedor.nome, fornecedor.contato, fornecedor.endereco, fornecedor.cnpj, fornecedor.id, fornecedor.user_id)
            )
            conn.commit()
            return cursor.rowcount > 0

    def delete_fornecedor(self, fornecedor_id, user_id):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM fornecedores WHERE id = ? AND user_id = ?", (fornecedor_id, user_id))
            conn.commit()
            return cursor.rowcount > 0