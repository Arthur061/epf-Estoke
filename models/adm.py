import sqlite3
import bcrypt

class Administrador:
    def __init__(self, id, nome, email, senha, permissoes):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha # Senha já deve ser o hash
        self.permissoes = permissoes # Lista de strings, e.g., ["gerenciar_usuarios", "gerar_relatorios"]

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "permissoes": self.permissoes
        }

    @staticmethod
    def from_row(row):
        if row is None:
            return None
        # Permissões são armazenadas como string JSON no banco de dados
        import json
        permissoes = json.loads(row[4]) if row[4] else []
        return Administrador(row[0], row[1], row[2], row[3], permissoes)

    def set_senha(self, senha_texto_claro): # Gera hash da senha
        self.senha = bcrypt.hashpw(senha_texto_claro.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    def check_senha(self, senha_texto_claro): # Verifica se a senha corresponde ao hash
        if not self.senha:
            return False
        return bcrypt.checkpw(senha_texto_claro.encode("utf-8"), self.senha.encode("utf-8"))

class AdministradorRepository:
    def __init__(self, db_path='database.db'):
        self.db_path = db_path
        self.create_table()

    def _get_connection(self):
        return sqlite3.connect(self.db_path)

    def create_table(self):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS administradores (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    senha TEXT NOT NULL,
                    permissoes TEXT
                )
            """)

    def _row_to_administrador(self, row):
        return Administrador.from_row(row)

    def get_all(self):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nome, email, senha, permissoes FROM administradores")
            return [self._row_to_administrador(row) for row in cursor.fetchall()]

    def get_by_id(self, admin_id):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nome, email, senha, permissoes FROM administradores WHERE id = ?", (admin_id,))
            row = cursor.fetchone()
            return self._row_to_administrador(row)

    def add_administrador(self, administrador):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            import json
            permissoes_json = json.dumps(administrador.permissoes)
            cursor.execute(
                "INSERT INTO administradores (nome, email, senha, permissoes) VALUES (?, ?, ?, ?)",
                (administrador.nome, administrador.email, administrador.senha, permissoes_json)
            )
            conn.commit()
            return cursor.lastrowid

    def update_administrador(self, administrador):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            import json
            permissoes_json = json.dumps(administrador.permissoes)
            cursor.execute(
                "UPDATE administradores SET nome = ?, email = ?, senha = ?, permissoes = ? WHERE id = ?",
                (administrador.nome, administrador.email, administrador.senha, permissoes_json, administrador.id)
            )
            conn.commit()
            return cursor.rowcount > 0

    def delete_administrador(self, admin_id):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM administradores WHERE id = ?", (admin_id,))
            conn.commit()
            return cursor.rowcount > 0