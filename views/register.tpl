%rebase('layout', title='Registro')

<div class="form-container">
    % if 'error' in locals() or 'error' in globals():
        % if error is not None:
            <div class="error">{{error}}</div>
        % end
    % end

    <form action="/register" method="post" id="registerForm">
        <h1><i class="fas fa-user-plus"></i> Criar Conta</h1>
            
        <div class="form-group">
            <label for="username">Nome de Usuário</label>
            <input type="text" id="username" name="name" placeholder="Digite seu nome de usuário" required>
        </div>
            
        <div class="form-group">
            <label for="email">E-mail</label>
            <input type="email" id="email" name="email" placeholder="seu.email@exemplo.com" required>
        </div>
            
        <div class="form-group password-group">
            <label for="password">Senha</label>
            <div style="position: relative;">
                <input type="password" id="password" name="password" placeholder="Crie uma senha segura" required>
                <span class="toggle-password" onclick="togglePassword('password')" style="position:absolute; right:10px; top:50%; transform:translateY(-50%); cursor:pointer;">
                    👁
                </span>
            </div>
        </div>

        <div class="form-group password-group">
            <label for="confirm-password">Confirme a Senha</label>
            <div style="position: relative;">
                <input type="password" id="confirm-password" name="confirm_password" placeholder="Digite a senha novamente" required>
                <span class="toggle-password" onclick="togglePassword('confirm-password')" style="position:absolute; right:10px; top:50%; transform:translateY(-50%); cursor:pointer;">
                    👁
                </span>
            </div>
        </div>
            
        <div class="form-group">
            <label for="birthdate">Data de Nascimento</label>
            <input type="date" id="birthdate" name="birthdate" required>
        </div>
            
        <div class="form-actions">
            <button type="submit" class="btn-submit">Registrar</button>
            <a href="/login" class="btn-link">Já tem conta? Faça login</a>
        </div>
        
        <div class="color-selector-title">Personalizar cor do formulário:</div>
        <div class="color-selector">
            <div class="color-option active" style="background-color: rgba(255, 255, 255, 0.15);" title="Padrão"></div>
            <div class="color-option" style="background-color: rgba(52, 152, 219, 0.3);" title="Azul Claro"></div>
            <div class="color-option" style="background-color: rgba(46, 204, 113, 0.3);" title="Verde Claro"></div>
            <div class="color-option" style="background-color: rgba(155, 89, 182, 0.3);" title="Lavanda"></div>
            <div class="color-option" style="background-color: rgba(231, 76, 60, 0.3);" title="Vermelho Suave"></div>
        </div>
    </form>
</div>

<script>
    document.getElementById('registerForm').addEventListener('submit', function(e) {
        const password = document.getElementById('password').value;
        const confirmPassword = document.getElementById('confirm_password').value;
        
        if (password !== confirmPassword) {
            alert('As senhas não coincidem!');
            e.preventDefault();
        }
    });
    function togglePassword(fieldId) {
        const input = document.getElementById(fieldId);
        if (input.type === "password") {
            input.type = "text";
        } else {
            input.type = "password";
        }
    }
</script>