<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistema de Estoque</title>
    <link rel="stylesheet" href="/static/css/style.css">
    <link rel="stylesheet" href="/static/css/helper.css">
</head>
<body>
    <header>
        <h1>Sistema de Estoque com Reposição Inteligente</h1>
        <nav>
            <ul>
                <li><a href="/home">Home</a></li>
                <li><a href="/produtos">Produtos</a></li>
                <li><a href="/fornecedores">Fornecedores</a></li>
                <li><a href="/produtos/reposicao">Reposição</a></li>
                <li><a href="/movimentacoes">Movimentações</a></li>
                <li><a href="/administradores">Administradores</a></li>
                <li><a href="/users">Usuários</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <h2>Login</h2>
        <form action="/login" method="post">
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required><br>

            <label for="password">Senha:</label>
            <input type="password" id="password" name="password" required><br>

            <input type="submit" value="Entrar">
        </form>
        %if error:
        <p style="color: red;">{{error}}</p>
        %end
        <p>Não tem uma conta? <a href="/register">Registre-se aqui</a>.</p>
    </main>
    <footer>
        <p>&copy; 2024 Sistema de Estoque Inteligente</p>
    </footer>
</body>
</html>
