<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistema Bottle - {{title or 'Sistema'}}</title>
    <link rel="stylesheet" href="/static/css/style.css" />
</head>
<body>

    <div class="container">
            <h1>Sistema ESTOKE</h1>
            % if session.get('user_id'):
            <nav>
                <span>Bem-vindo!</span>
                <a href="/logout">Sair</a>
            </nav>
            % end
        </div>
    </header>

    <div class="container">
        {{!base}}
    </div>

    <footer>
        <p>&copy; 2025, ESTOKE. Todos os direitos reservados.</p>
    </footer>

    <!-- Scripts JS no final do body -->
    <script src="/static/js/main.js"></script>
</body>
</html>
