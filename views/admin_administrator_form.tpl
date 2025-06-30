%rebase('layout', title='Gerenciamento admins Forms')

<section class="form-section">
    <h1>{{"Editar Administrador" if admin else "Adicionar Administrador"}}</h1>
    
    % if 'error' in locals() or 'error' in globals():
        % if error is not None:
            <div class="error">{{error}}</div>
        % end
    % end

    <form action="{{action}}" method="post" id="adminForm">
        <div class="form-group">
            <label for="name">Nome:</label>
            <input type="text" id="name" name="name" required 
                   value="{{admin.name if admin else ''}}">
        </div>
        
        <div class="form-group">
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required 
                   value="{{admin.email if admin else ''}}">
        </div>
        
        <div class="form-group">
            <label for="birthdate">Data de Nascimento:</label>
            <input type="date" id="birthdate" name="birthdate" required 
                   value="{{admin.birthdate if admin else ''}}">
        </div>
        
        % if not admin:
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
            <label for="permissoes">Permissões (separadas por vírgula):</label>
            <input type="text" id="permissoes" name="permissoes" 
                   value="{{', '.join(admin.permissoes) if admin else ''}}">
        </div>
        
        <div class="form-actions">
            <button type="submit" class="btn-submit">Salvar</button>
            <a href="/admin/administrators" class="btn-link">Voltar</a>
        </div>
    </form>
</section>

<script>
    document.getElementById('adminForm').addEventListener('submit', function(e) {
        const password = document.getElementById('password')?.value;
        const confirmPassword = document.getElementById('confirm_password')?.value;
        
        if (password && password !== confirmPassword) {
            alert('As senhas não coincidem!');
            e.preventDefault();
        }
    });
</script>

