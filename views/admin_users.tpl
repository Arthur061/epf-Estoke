% rebase('layout', title='Gerenciamento de Usuários')

<div class="content-container">
    <div class="content-header">
        <h1>Gerenciamento de Usuários</h1>
        <a href="#" id="btn-adicionar-usuario" class="btn btn-primary">
            <i class="fas fa-plus"></i> Adicionar Usuário
        </a>
    </div>
    
    <p>Aqui você pode visualizar e gerenciar todos os usuários do sistema.</p>

    % if not users:
    <div class="empty-state">
        <i class="fas fa-users-slash"></i>
        <p>Nenhum usuário cadastrado.</p>
    </div>
    % else:
    <table class="admin-table">
        <thead>
            <tr>
                <th>ID</th>
                <th>Nome</th>
                <th>Email</th>
                <th>Tipo</th>
                <th>Ações</th>
            </tr>
        </thead>
        <tbody>
            % for user in users:
            <tr>
                <td>{{user.id}}</td>
                <td>{{user.name}}</td>
                <td>{{user.email}}</td>
                <td>{{user.tipo or 'Comum'}}</td>
                <td>
                    <a href="/admin/users/edit/{{user.id}}" class="button button-primary">Editar</a>
                    
                    <form action="/admin/users/delete/{{user.id}}" method="post" style="display:inline;" onsubmit="return confirm('Tem certeza que deseja excluir o usuário {{user.name}}?');">
                        <button type="submit" class="button button-danger">Excluir</button>
                    </form>
                </td>
            </tr>
            % end
        </tbody>
    </table>
    % end
</div>

<script>
    const botaoAdicionar = document.getElementById('btn-adicionar-usuario');

    botaoAdicionar.addEventListener('click', function(event) {
        event.preventDefault();

        const confirmacao = confirm('Você será desconectado da conta atual para criar um novo usuário. Deseja continuar?');

        if (confirmacao) {
            window.location.href = '/logout_and_register'; 
        }
    });
</script>