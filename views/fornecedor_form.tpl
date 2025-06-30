
%rebase layout

<h2>%if fornecedor: Editar Fornecedor #{{fornecedor.id}}%else: Novo Fornecedor%end</h2>
<form action="" method="post">
    <label for="nome">Nome:</label>
    <input type="text" id="nome" name="nome" value="{{fornecedor.nome if fornecedor else ''}}" required><br>

    <label for="contato">Contato:</label>
    <input type="text" id="contato" name="contato" value="{{fornecedor.contato if fornecedor else ''}}"><br>

    <label for="endereco">Endereço:</label>
    <input type="text" id="endereco" name="endereco" value="{{fornecedor.endereco if fornecedor else ''}}"><br>

    <label for="cnpj">CNPJ:</label>
    <input type="text" id="cnpj" name="cnpj" value="{{fornecedor.cnpj if fornecedor else ''}}"><br>

    <input type="submit" value="Salvar">
</form>


