%# Informa ao Bottle que este template deve ser "encaixado" dentro do layout principal
% rebase('layout.tpl', title='Meu Perfil')

<div class="content-container">
    <div class="content-header">
        <h1>Meu Perfil</h1>
    </div>

    % if defined('message') and message:
        <div class="success-message" style="background-color: #2ecc71; padding: 15px; border-radius: 8px; margin-bottom: 20px; text-align: center;">
            {{ message }}
        </div>
    % end

    <form action="/perfil" method="post">
        <div class="form-group">
            <label for="name">Nome Completo</label>
            <input type="text" id="name" name="name" value="{{ user.name }}" required>
        </div>

        <div class="form-group">
            <label for="email">Email</label>
            <input type="email" id="email" name="email" value="{{ user.email }}" required>
        </div>

        <div class="form-group">
            <label for="birthdate">Data de Aniversário</label>
            <input type="date" id="birthdate" name="birthdate" value="{{ user.birthdate.split(' ')[0] if user.birthdate else '' }}">
        </div>

        <hr style="border-color: rgba(255,255,255,0.1); margin: 25px 0;">

        <div class="form-group">
            <label for="password">Nova Senha</label>
            <input type="password" id="password" name="password" placeholder="Deixe em branco para não alterar">
        </div>

        <div class="form-actions">
            <button type="submit" class="btn btn-primary">Salvar Alterações</button>
        </div>
    </form>
</div>