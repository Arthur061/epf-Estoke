% rebase('layout', title='Gerenciamento de Fornecedores')

<div class="form-container">
    <div class="form-section">
        <h1>{{'Editar Fornecedor' if fornecedor else 'Cadastrar Novo Fornecedor'}}</h1>
        
        <form action="" method="post" id="fornecedorForm">
            <div class="form-group">
                <label for="nome">Nome:</label>
                <input type="text" id="nome" name="nome" required value="{{fornecedor.nome if fornecedor else ''}}" placeholder="Nome ou razão social">
            </div>
            
            <div class="form-group">
                <label for="cnpj">CNPJ:</label>
                <input type="text" id="cnpj" name="cnpj" value="{{fornecedor.cnpj if fornecedor else ''}}" placeholder="00.000.000/0001-00">
            </div>

            <div class="form-group">
                <label for="contato">Contato (Email ou Telefone):</label>
                <input type="text" id="contato" name="contato" value="{{fornecedor.contato if fornecedor else ''}}" placeholder="contato@empresa.com ou (11) 99999-9999">
            </div>
            
            <div class="form-group">
                <label for="endereco">Endereço:</label>
                <input type="text" id="endereco" name="endereco" value="{{fornecedor.endereco if fornecedor else ''}}" placeholder="Rua, número, bairro, cidade - UF">
            </div>
            
            <div class="form-actions">
                <button type="submit" class="btn-submit">Salvar</button>
                <a href="/admin/fornecedores" class="btn-link">Cancelar</a>
            </div>
        </form>
    </div>
</div>