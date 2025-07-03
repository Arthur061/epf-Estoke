% rebase('layout.tpl', title='Gerenciamento de Reposição')

<div class="content-container">
    <div class="content-header">
        <h1>Relatório de Reposição</h1>
        </div>
    
    <p>A lista abaixo exibe todos os produtos cujo estoque atual está igual ou abaixo da quantidade mínima definida.</p>

    % if not produtos:
    <div class="empty-state">
        <i class="fas fa-check-circle"></i>
        <p>Nenhum produto precisa de reposição. O estoque está em dia!</p>
    </div>
    % else:
    <table class="admin-table">
        <thead>
            <tr>
                <th>ID</th>
                <th>Produto</th>
                <th>Estoque Atual</th>  
                <th>Estoque Mínimo</th>
                <th>Fornecedor Sugerido</th>
            </tr>
        </thead>
        <tbody>
            %for produto in produtos:
            <tr>
                <td>{{produto.id}}</td>
                <td>{{produto.nome}}</td>
                <td><strong>{{produto.qtd_estoque}}</strong></td> <td>{{produto.qtd_minima}}</td>
                <td>{{fornecedores.get(produto.fornecedor_id, 'Não definido')}}</td>
            </tr>
            %end
        </tbody>
    </table>
    % end
</div>