<section class="form-section">
    <h1>{{'Editar Usuário' if user else 'Cadastrar Usuário'}}</h1>
    
    <form action="{{action}}" method="post" class="form-container" id="userForm">
        <div class="form-group">
            <label for="name">Nome:</label>
            <input type="text" id="name" name="name" required 
                   value="{{user.name if user else ''}}">
        </div>
        
        <div class="form-group">
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required 
                   value="{{user.email if user else ''}}">
        </div>
        
        % if not user:
        <div class="form-group">
            <label for="password">Senha:</label>
            <input type="password" id="password" name="password" required>
        </div>
        <div class="form-group">
            <label for="confirm_password">Confirmar Senha:</label>
            <input type="password" id="confirm_password" name="confirm_password" required>
        </div>
        % end
        
        <div class="form-group">
            <label for="birthdate">Data de Nascimento:</label>
            <input type="date" id="birthdate" name="birthdate" required 
                   value="{{user.birthdate if user else ''}}">
        </div>
        
        <div class="form-actions">
            <button type="submit" class="btn-submit">Salvar</button>
            <a href="/users" class="btn-cancel">Voltar</a>
        </div>
    </form>
</section>

<script>
    document.getElementById('userForm').addEventListener('submit', function(e) {
        const password = document.getElementById('password')?.value;
        const confirmPassword = document.getElementById('confirm_password')?.value;
        
        if (password && password !== confirmPassword) {
            alert('As senhas não coincidem!');
            e.preventDefault();
        }
    });
</script>