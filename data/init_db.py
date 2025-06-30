import sqlite3

def init_db(db_path='database.db'):
    """
    Inicializa o banco de dados, criando todas as tabelas necessárias
    com as colunas corretas se elas ainda não existirem.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Tabela de Usuários com as colunas
    print("Verificando/Criando tabela 'users'...")
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        birthdate TEXT NOT NULL,
        password TEXT NOT NULL,
        tipo TEXT,
        permissoes TEXT
    )
    ''')
    print("-> Tabela 'users' verificada/criada com sucesso.")

    # Tabela de Fornecedores
    print("Verificando/Criando tabela 'fornecedores'...")
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS fornecedores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        user_id INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
    ''')
    print("-> Tabela 'fornecedores' verificada/criada com sucesso.")

    # Tabela de Produtos
    print("Verificando/Criando tabela 'produtos'...")
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        descricao TEXT,
        preco REAL NOT NULL,
        qtd_estoque INTEGER NOT NULL,
        qtd_minima INTEGER NOT NULL,
        fornecedor_id INTEGER,
        user_id INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (fornecedor_id) REFERENCES fornecedores(id)
    )
    ''')
    print("-> Tabela 'produtos' verificada/criada com sucesso.")

    conn.commit()
    conn.close()
    print("\nBanco de dados inicializado com sucesso!")

if __name__ == '__main__':
    print("Iniciando a criação do banco de dados...")
    init_db()

