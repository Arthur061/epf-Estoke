%rebase('layout', title='Gerenciamento de Usuários')

<!-- 
  Usamos a classe 'welcome-container' que já existe no seu CSS.
  Ela é mais larga que a do formulário de login e ideal para tabelas.
-->
<div class="welcome-container">
    <h1>Gerenciamento de Usuários</h1>
    <p>Aqui você pode visualizar e gerenciar todos os usuários do sistema.</p>

    <table class="table admin-table">
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
                    <form action="/admin/users/delete/{{user.id}}" method="post" style="display:inline;">
                        <button type="submit" class="button button-danger">Excluir</button>
                    </form>
                </td>
            </tr>
            % end
        </tbody>
    </table>
</div>
