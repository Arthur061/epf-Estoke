
%rebase layout

<h2>Produtos para Reposição</h2>
%if produtos:
<table border="1">
    <thead>
        <tr>
            <th>ID</th>
            <th>Nome</th>
            <th>Estoque Atual</th>
            <th>Quantidade Mínima</th>
            <th>Fornecedor</th>
        </tr>
    </thead>
    <tbody>
        %for produto in produtos:
        <tr>
            <td>{{produto.id}}</td>
            <td>{{produto.nome}}</td>
            <td>{{produto.qtd_estoque}}</td>
            <td>{{produto.qtd_minima}}</td>
            <td>{{fornecedores.get(produto.fornecedor_id, 'N/A')}}</td>
        </tr>
        %end
    </tbody>
</table>
%else:
<p>Nenhum produto precisa de reposição no momento.</p>
%end


