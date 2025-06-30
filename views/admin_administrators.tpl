%rebase('layout', title='Gerenciamento admins')

<div class="container">
    <h1>Gerenciamento de Administradores</h1>
    <p>Aqui você pode visualizar e gerenciar os administradores do sistema.</p>

    <a href="/admin/administrators/add" class="button button-success">Adicionar Novo Administrador</a>

    <table class="table">
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
</div>


