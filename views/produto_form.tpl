% rebase('layout', title=title, user_name=user_name)

<div class="form-container">
    <div class="form-section">
        <h1>{{title}}</h1>

        <form action="{{action_url}}" method="POST">
            <div class="form-group">
                <label for="nome">Nome do Produto:</label>
                <input type="text" id="nome" name="nome" value="{{produto.nome if produto else ''}}" required placeholder="Ex: Monitor Gamer">
            </div>
            <div class="form-group">
                <label for="descricao">Descrição:</label>
                <input type="text" id="descricao" name="descricao" value="{{produto.descricao if produto else ''}}" placeholder="Ex: 27 polegadas, 144Hz">
            </div>
            <div class="form-group">
                <label for="preco">Preço (R$):</label>
                <input type="number" step="0.01" id="preco" name="preco" value="{{produto.preco if produto else ''}}" required placeholder="Ex: 1599.90">
            </div>
            <div class="form-group">
                <label for="qtd_estoque">Quantidade em Estoque:</label>
                <input type="number" id="qtd_estoque" name="qtd_estoque" value="{{produto.qtd_estoque if produto else ''}}" required placeholder="Ex: 50">
            </div>
             <div class="form-group">
                <label for="qtd_minima">Estoque Mínimo:</label>
                <input type="number" id="qtd_minima" name="qtd_minima" value="{{produto.qtd_minima if produto else ''}}" required placeholder="Ex: 10">
            </div>
            <div class="form-group">
                <label for="fornecedor_id">ID do Fornecedor (opcional):</label>
                <input type="number" id="fornecedor_id" name="fornecedor_id" value="{{produto.fornecedor_id if produto else ''}}" placeholder="Ex: 1">
            </div>
            
            <div class="form-actions">
                <button type="submit" class="btn-submit">Salvar Produto</button>
                <a href="/produtos" class="btn-link">Cancelar</a>
            </div>
        </form>
    </div>
</div>
