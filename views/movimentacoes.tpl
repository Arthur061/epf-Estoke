% rebase('layout.tpl', title='Registrar Movimentações')

<div class="content-container">
    <div class="content-header">
        <h1>Registrar Movimentação de Estoque</h1>
    </div>

    <div class="form-container" style="margin-bottom: 2rem;">
        <form action="/movimentacoes" method="post">
            <div class="form-group">
                <label for="produto_id">Produto</label>
                <select id="produto_id" name="produto_id" required>
                    <option value="" disabled selected>Selecione um produto...</option>
                    % for produto in produtos:
                        <option value="{{produto.id}}">{{produto.nome}} (Estoque: {{produto.qtd_estoque}})</option>
                    % end
                </select>
            </div>
            <div class="form-group">
                <label for="tipo">Tipo de Movimentação</label>
                <select id="tipo" name="tipo" required>
                    <option value="entrada">Entrada</option>
                    <option value="saida">Saída</option>
                </select>
            </div>
            <div class="form-group">
                <label for="quantidade">Quantidade</label>
                <input type="number" id="quantidade" name="quantidade" min="1" required>
            </div>
            <div class="form-actions">
                <button type="submit" class="btn-submit">Registrar</button>
            </div>
        </form>
    </div>

    <h2>Histórico de Movimentações</h2>
    <table class="admin-table">
        <thead>
            <tr>
                <th>Data</th>
                <th>Produto</th>
                <th>Tipo</th>
                <th>Quantidade</th>
            </tr>
        </thead>
        <tbody>
            % if not movimentacoes:
            <tr>
                <td colspan="4" style="text-align: center;">Nenhuma movimentação registrada.</td>
            </tr>
            % else:
                % for mov in movimentacoes:
                <tr>
                    <td>{{ mov.data.strftime('%d/%m/%Y %H:%M') }}</td>
                    <td>{{ produtos_dict.get(mov.produto_id, 'Produto não encontrado') }}</td>
                    <td>
                        % if mov.tipo == 'entrada':
                            <span style="color: #2ecc71;">Entrada</span>
                        % else:
                            <span style="color: #e74c3c;">Saída</span>
                        % end
                    </td>
                    <td>{{ mov.qtd }}</td>
                </tr>
                % end
            % end
        </tbody>
    </table>
</div>