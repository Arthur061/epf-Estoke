% rebase('layout', title=produto.nome, user_name=user_name)

<style>
    .details-container {
        background: var(--form-bg-color);
        backdrop-filter: blur(12px);
        border-radius: 16px;
        padding: 2.5rem;
        width: 100%;
        max-width: 700px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    .details-container h2 {
        text-align: center;
        margin-bottom: 2rem;
        color: var(--accent);
    }
    .details-list {
        list-style: none;
        padding: 0;
        margin: 0;
    }
    .details-list li {
        display: flex;
        justify-content: space-between;
        padding: 1rem 0;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        font-size: 1.1rem;
    }
    .details-list li:last-child {
        border-bottom: none;
    }
    .details-list li strong {
        color: #ccc;
    }
    .details-actions {
        margin-top: 2rem;
        display: flex;
        justify-content: center;
        gap: 1rem;
    }
     .btn {
        padding: 12px 20px;
        border-radius: 8px;
        text-decoration: none;
        color: white;
        border: none;
        cursor: pointer;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    .btn-back { background-color: #6c757d; }
    .btn-edit { background-color: var(--primary-color); }
    .btn:hover { transform: translateY(-2px); box-shadow: 0 4px 10px rgba(0,0,0,0.3); }
</style>

<div class="details-container">
    <h2>Detalhes do Produto</h2>
    <ul class="details-list">
        <li><strong>Nome:</strong> <span>{{produto.nome}}</span></li>
        <li><strong>Descrição:</strong> <span>{{produto.descricao or 'Não informado'}}</span></li>
        <li><strong>Preço:</strong> <span>R$ {{ "%.2f" % produto.preco }}</span></li>
        <li><strong>Quantidade em Estoque:</strong> <span>{{produto.qtd_estoque}}</span></li>
        <li><strong>Estoque Mínimo:</strong> <span>{{produto.qtd_minima}}</span></li>
        <li><strong>ID do Fornecedor:</strong> <span>{{produto.fornecedor_id or 'Não informado'}}</span></li>
    </ul>
    <div class="details-actions">
        <a href="/produtos" class="btn btn-back">Voltar</a>
        <a href="/produtos/editar/{{produto.id}}" class="btn btn-edit">Editar Produto</a>
    </div>
</div>
