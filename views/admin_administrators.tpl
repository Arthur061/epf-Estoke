% rebase('layout', title='Gerenciamento de Administradores')

<div class="content-container">
    <div class="content-header">
        <h1>Gerenciamento de Administradores</h1>
        <a href="/admin/users" class="btn btn-primary">
            <i class="fas fa-user-shield"></i> Adicionar Administrador
        </a>
    </div>

    <p>Aqui você pode visualizar e gerenciar os administradores do sistema.</p>

    % if not administrators:
    <div class="empty-state">
        <i class="fas fa-user-shield"></i>
        <p>Nenhum administrador cadastrado.</p>
    </div>
    % else:
    <table class="admin-table">
        <thead>
            <tr>
                <th>ID</th>
                <th>Nome</th>
                <th>Email</th>
                <th>Permissões</th>
                <th>Ações</th>
            </tr>
        </thead>
        <tbody>
            % for admin in administrators:
            <tr>
                <td>{{admin.id}}</td>
                <td>{{admin.name}}</td>
                <td>{{admin.email}}</td>
                <td>{{', '.join(admin.permissoes)}}</td>
                <td>
                    <a href="/admin/administrators/edit/{{admin.id}}" class="button button-primary">Editar</a>
                    <form action="/admin/administrators/delete/{{admin.id}}" method="post" style="display:inline;">
                        <button type="submit" class="button button-danger">Excluir</button>
                    </form>
                </td>
            </tr>
            % end
        </tbody>
    </table>
    % end
</div>