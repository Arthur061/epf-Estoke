<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ESTOKE  - {{title or 'Sistema de Estoque'}}</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <header>
        <div class="header-container">
            <div class="main-nav-menu">
                <button class="nav-toggle-btn" id="navToggleBtn">
                    <i class="fas fa-bars"></i> </button>
                <div class="nav-dropdown-content" id="navDropdown">
                    <h2>Navegação</h2>
                    <ul>
                        <li><a href="/produtos">Gerenciar Produtos</a></li>
                        <li><a href="/fornecedores">Gerenciar Fornecedores</a></li>
                        <li><a href="/produtos/reposicao">Produtos para Reposição</a></li>
                        <li><a href="/movimentacoes">Registrar Movimentações</a></li>
                        <li><a href="/administradores">Gerenciar Administradores</a></li>
                        <li><a href="/users">Gerenciar Usuários</a></li>
                    </ul>
                </div>
            </div>

            <div class="logo">
                <a href="/home" style="text-decoration: none; color: inherit;">
                    <h1>Sistema ESTOKE</h1>
                </a>
            </div>

            <nav>
                % if session and session.get('user_id'):
                    <a href="/perfil" class="profile-link">
                        <i class="fas fa-user-circle"></i> Olá, {{ user_name or 'Usuário' }}!
                    </a>
                    <a href="/logout">Sair</a>
                % else:
                    <a href="/login">Entrar</a>
                    <a href="/register">Registrar</a>
                % end
            </nav>
        </div>
    </header>

    <main class="main-content">
        <div class="container">
            {{!base}}
        </div>
    </main>

    <footer>
        <p>&copy; 2025, ESTOKE. Todos os direitos reservados.</p>
    </footer>

    <script src="/static/js/main.js"></script>
</body>
</html>