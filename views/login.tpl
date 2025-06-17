%rebase('layout', title='Login')

<section class="form-section">
    <h1>Login</h1>
    
     % if error is not None:
        <div class="error">{{error}}</div>
    % end

    <form action="/login" method="post">
        <div class="form-group">
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
        </div>
        
        <div class="form-group">
            <label for="password">Senha:</label>
            <input type="password" id="password" name="password" required>
        </div>
        
        <div class="form-actions">
            <button type="submit" class="btn-submit">Entrar</button>
            <a href="/register" class="btn-link">Criar conta</a>
        </div>
    </form>
</section>