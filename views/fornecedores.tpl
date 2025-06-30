
%rebase layout

<h2>Lista de Fornecedores</h2>
<a href="/fornecedores/novo" class="button">Adicionar Novo Fornecedor</a>
<table border="1">
    <thead>
        <tr>
            <th>ID</th>
            <th>Nome</th>
            <th>Contato</th>
            <th>Endereço</th>
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
            <td>{{fornecedor.endereco}}</td>
            <td>{{fornecedor.cnpj}}</td>
            <td>
                <a href="/fornecedores/editar/{{fornecedor.id}}">Editar</a>
                <a href="/fornecedores/excluir/{{fornecedor.id}}">Excluir</a>
            </td>
        </tr>
        %end
    </tbody>
</table>


