% rebase('layout', title='Gerenciamento de Fornecedores')

<div class="content-container">
    <div class="content-header">
        <h1>Gerenciamento de Fornecedores</h1>
        <a href="/fornecedores/novo" class="btn btn-primary">
            <i class="fas fa-plus"></i> Adicionar Fornecedor
        </a>
    </div>
    
    <p>Aqui você pode visualizar e gerenciar todos os fornecedores cadastrados.</p>

    % if not fornecedores:
    <div class="empty-state">
        <i class="fas fa-box-open"></i>
        <p>Nenhum fornecedor cadastrado.</p>
    </div>
    % else:
    <table class="admin-table">
        <thead>
            <tr>
                <th>ID</th>
                <th>Nome</th>
                <th>Contato</th>
                <th>CNPJ</th>
                <th>Ações</th>
            </tr>
        </thead>
        <tbody>
            %for fornecedor in fornecedores:
            <tr>
                <td>{{fornecedor.id}}</td>
                <td>{{fornecedor.nome}}</td>
                <td>{{fornecedor.contato}}</td>
                <td>{{fornecedor.cnpj}}</td>
                <td>
                    <a href="/fornecedores/editar/{{fornecedor.id}}" class="button button-primary">Editar</a>
                    <form action="/fornecedores/excluir/{{fornecedor.id}}" method="post" style="display:inline;">
                        <button type="submit" class="button button-danger">Excluir</button>
                    </form>
                </td>
            </tr>
            %end
        </tbody>
    </table>
    % end
</div>