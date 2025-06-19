<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ESTOKE :) - {{title or 'Sistema de Estoque'}}</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --primary: #3498db;
            --secondary: #2980b9;
            --accent: #ffcc00;
            --dark: #1a1a2e;
            --light: #f5f5f5;
            --success: #2ecc71;
            --danger: #e74c3c;
            --form-bg-color: rgba(255, 255, 255, 0.15); 
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        body {
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), 
                        url('/static/img/estoque.png') no-repeat center center fixed;
            background-size: cover;
            color: var(--light);
        }

        /* cabeçalho */
        header {
            background: rgba(0, 0, 0, 0.7);
            backdrop-filter: blur(5px);
            padding: 1rem 2rem;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        .header-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            max-width: 1200px;
            margin: 0 auto;
        }
        
        .logo {
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .logo h1 {
            font-size: 1.8rem;
            background: linear-gradient(to right, var(--accent), #ff9966);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
        }
        
        nav {
            display: flex;
            gap: 15px;
            align-items: center;
        }
        
        nav a {
            color: var(--light);
            text-decoration: none;
            transition: all 0.3s ease;
        }
        
        nav a:hover {
            color: var(--accent);
        }
        
        /* principal  */
        .main-content {
            flex: 1;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 2rem;
        }
        
        .form-container {
            background: var(--form-bg-color);
            backdrop-filter: blur(12px);
            border-radius: 16px;
            padding: 2.5rem;
            width: 100%;
            max-width: 500px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
            border: 1px solid rgba(255, 255, 255, 0.1);
            transition: background-color 0.5s ease;
        }
        
        /* rodapé */
        footer {
            text-align: center;
            padding: 1.5rem;
            background: rgba(0, 0, 0, 0.7);
            backdrop-filter: blur(5px);
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            font-size: 0.9rem;
            color: rgba(255, 255, 255, 0.7);
        }

        .form-section {
            width: 100%;
        }
        
        .form-section h1 {
            text-align: center;
            margin-bottom: 1.5rem;
            color: var(--accent);
        }
        
        .form-group {
            margin-bottom: 1.5rem;
        }
        
        .form-group label {
            display: block;
            margin-bottom: 0.5rem;
            color: var(--light);
            font-weight: 500;
        }
        
        .form-group input {
            width: 100%;
            padding: 12px 15px;
            border-radius: 8px;
            border: 1px solid rgba(255, 255, 255, 0.2);
            background: rgba(0, 0, 0, 0.3);
            color: var(--light);
            font-size: 1rem;
            transition: all 0.3s ease;
        }
        
        .form-group input:focus {
            outline: none;
            border-color: var(--accent);
            box-shadow: 0 0 0 3px rgba(255, 204, 0, 0.2);
        }
        
        .form-group input::placeholder {
            color: rgba(255, 255, 255, 0.5);
        }
        
        .form-actions {
            display: flex;
            flex-direction: column;
            gap: 10px;
            margin-top: 2rem;
        }
        
        .btn-submit {
            background: linear-gradient(to right, var(--primary), var(--secondary));
            color: var(--light);
            border: none;
            padding: 12px;
            border-radius: 8px;
            font-size: 1rem;
            cursor: pointer;
            transition: all 0.3s ease;
            font-weight: 600;
        }
        
        .btn-submit:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
        }
        
        .btn-link {
            background: transparent;
            color: var(--accent);
            border: 1px solid var(--accent);
            padding: 12px;
            border-radius: 8px;
            text-align: center;
            text-decoration: none;
            font-size: 1rem;
            cursor: pointer;
            transition: all 0.3s ease;
            font-weight: 500;
        }
        
        .btn-link:hover {
            background: rgba(255, 204, 0, 0.1);
        }
        
        .color-selector {
            display: flex;
            justify-content: center;
            gap: 10px;
            margin-top: 25px;
            padding-top: 15px;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        .color-selector-title {
            text-align: center;
            margin-top: 20px;
            font-size: 0.9rem;
            color: rgba(255, 255, 255, 0.7);
        }
        
        .color-option {
            width: 30px;
            height: 30px;
            border-radius: 50%;
            cursor: pointer;
            border: 2px solid transparent;
            transition: transform 0.2s ease;
        }
        
        .color-option:hover {
            transform: scale(1.2);
        }
        
        .color-option.active {
            border-color: white;
            transform: scale(1.2);
        }
        
        .error {
            background: rgba(231, 76, 60, 0.3);
            border: 1px solid rgba(231, 76, 60, 0.5);
            padding: 12px;
            border-radius: 8px;
            margin-bottom: 1.5rem;
            color: rgba(255, 255, 255, 0.9);
            text-align: center;
        }
    </style>
</head>
<body>
    <header>
        <div class="header-container">
            <div class="logo">
                <h1>Sistema ESTOKE</h1>
            </div>
            % if session.get('user_id'):
            <nav>
                <span>Bem-vindo!</span>
                <a href="/logout">Sair</a>
            </nav>
            % end
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

    <script>
        // teste magico
        document.querySelectorAll('.color-option').forEach(option => {
            option.addEventListener('click', function() {
                document.querySelectorAll('.color-option').forEach(opt => {
                    opt.classList.remove('active');
                });
                
                this.classList.add('active');
                
                // parte que altera
                const formContainer = document.querySelector('.form-container');
                if (formContainer) {
                    formContainer.style.backgroundColor = this.style.backgroundColor;
                }
                
                // att variavel
                document.documentElement.style.setProperty('--form-bg-color', this.style.backgroundColor);
            });
        });

        // salvar cor
        window.addEventListener('DOMContentLoaded', () => {
            const savedColor = localStorage.getItem('formBgColor');
            if (savedColor) {
                document.documentElement.style.setProperty('--form-bg-color', savedColor);
                const formContainer = document.querySelector('.form-container');
                if (formContainer) {
                    formContainer.style.backgroundColor = savedColor;
                }
                
                document.querySelectorAll('.color-option').forEach(option => {
                    if (option.style.backgroundColor === savedColor) {
                        option.classList.add('active');
                    }
                });
            }
        });

        // att local apos selecionar
        document.querySelectorAll('.color-option').forEach(option => {
            option.addEventListener('click', function() {
                localStorage.setItem('formBgColor', this.style.backgroundColor);
            });
        });
    </script>
</body>
</html>