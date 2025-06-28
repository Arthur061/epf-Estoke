% rebase('layout', title='Meus Produtos', user_name=user_name)

<style>
    /* Estilos específicos para a tabela de produtos */
    .product-table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 2rem;
        background: var(--form-bg-color);
        backdrop-filter: blur(10px);
        border-radius: 8px;
        overflow: hidden;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    .product-table th, .product-table td {
        padding: 15px;
        text-align: left;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }
    .product-table th {
        background-color: rgba(0, 0, 0, 0.3);
        color: var(--accent);
        font-weight: 600;
    }
    .product-table tr:last-child td {
        border-bottom: none;
    }
    .product-table tr:hover {
        background-color: rgba(255, 255, 255, 0.05);
    }
    .product-table a {
        color: var(--accent);
        text-decoration: none;
        font-weight: 500;
    }
    .product-table a:hover {
        text-decoration: underline;
    }
    .actions-cell form, .actions-cell a {
        display: inline-block;
        margin-right: 10px;
    }
    .btn {
        padding: 8px 12px;
        border-radius: 5px;
        text-decoration: none;
        color: white;
        border: none;
        cursor: pointer;
        font-size: 0.9rem;
        transition: all 0.3s ease;
    }
    .btn-add { background-color: var(--primary-color); }
    .btn-edit { background-color: #f39c12; } /* Laranja */
    .btn-delete { background-color: var(--danger-color); }
    .btn:hover { transform: translateY(-2px); box-shadow: 0 4px 10px rgba(0,0,0,0.3); }
</style>

<div class="welcome-container">
    <h1 class="welcome-title">Gerenciamento de Produtos</h1>
    <p class="welcome-subtitle">Adicione, visualize, edite e remova seus produtos.</p>
    <a href="/produtos/adicionar" class="btn btn-add">Adicionar Novo Produto</a>

    % if not produtos:
        <p style="margin-top: 2rem;">Você ainda não tem produtos cadastrados.</p>
    % else:
        <table class="product-table">
            <thead>
                <tr>
                    <th>Nome</th>
                    <th>Preço</th>
                    <th>Estoque</th>
                    <th>Ações</th>
                </tr>
            </thead>
            <tbody>
                % for produto in produtos:
                <tr>
                    <td><a href="/produtos/detalhes/{{produto.id}}">{{produto.nome}}</a></td>
                    <td>R$ {{ "%.2f" % produto.preco }}</td>
                    <td>{{produto.qtd_estoque}}</td>
                    <td class="actions-cell">
                        <a href="/produtos/editar/{{produto.id}}" class="btn btn-edit">Editar</a>
                        <form action="/produtos/excluir/{{produto.id}}" method="POST" onsubmit="return confirm('Tem certeza que deseja excluir este produto?');">
                            <button type="submit" class="btn btn-delete">Excluir</button>
                        </form>
                    </td>
                </tr>
                % end
            </tbody>
        </table>
    % end
</div>
