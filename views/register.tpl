%rebase('layout', title='Registro')

<section class="form-section">
    <h1>Criar Conta</h1>
    
    % if 'error' in locals() or 'error' in globals():
        % if error is not None:
            <div class="error">{{error}}</div>
        % end
    % end

    <form action="/register" method="post" id="registerForm">
        <div class="form-group">
            <label for="name">Nome:</label>
            <input type="text" id="name" name="name" required>
        </div>
        
        <div class="form-group">
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
        </div>
        
        <div class="form-group">
            <label for="birthdate">Data de Nascimento:</label>
            <input type="date" id="birthdate" name="birthdate" required>
        </div>
        
        <div class="form-group">
            <label for="password">Senha:</label>
            <input type="password" id="password" name="password" required>
        </div>
        
        <div class="form-group">
            <label for="confirm_password">Confirmar Senha:</label>
            <input type="password" id="confirm_password" name="confirm_password" required>
        </div>
        
        <div class="form-actions">
            <button type="submit" class="btn-submit">Registrar</button>
            <a href="/login" class="btn-link">Já tem conta? Faça login</a>
        </div>
    </form>
</section>

<script>
    document.getElementById('registerForm').addEventListener('submit', function(e) {
        const password = document.getElementById('password').value;
        const confirmPassword = document.getElementById('confirm_password').value;
        
        if (password !== confirmPassword) {
            alert('As senhas não coincidem!');
            e.preventDefault();
        }
    });
</script>