%rebase('layout', title='Login')

<div class="form-container">
    % if error is not None:
        <div class="error">{{error}}</div>
    % end

    <form action="/login" method="post">
        <h1><i class="fas fa-sign-in-alt"></i> Fazer login</h1>

        <div class="form-group">
            <label for="email">E-mail</label>
            <input type="email" id="email" name="email" placeholder="seu.email@exemplo.com" required>
        </div>
        
        <div class="form-group">
            <label for="password">Senha</label>
            <input type="password" id="password" name="password" placeholder="Digite sua senha" required>
        </div>
        
        <div class="form-actions">
            <button type="submit" class="btn-submit">Entrar</button>

            <a href="/register" class="btn-link">Criar conta</a>
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