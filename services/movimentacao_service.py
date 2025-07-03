from datetime import datetime
from models.movimentacao import Movimentacao, MovimentacaoRepository
import sqlite3

class MovimentacaoService:
    def __init__(self):
        self.repo = MovimentacaoRepository()
    
    def get_movimentacoes_by_user(self, user_id):
        """Retorna todas as movimentações de um usuário específico"""
        return self.repo.get_all_by_user(user_id)
    
    def get_by_id(self, movimentacao_id):
        """Busca movimentação por ID"""
        return self.repo.get_by_id(movimentacao_id)
    
    def get_by_produto(self, produto_id):
        """Busca movimentações por produto"""
        return self.repo.get_by_produto_id(produto_id)
    
    def save(self, produto_id, tipo, quantidade, user_id):
        movimentacao = Movimentacao(
            id=None,
            produto_id=produto_id,
            data=datetime.now(),
            tipo=tipo,
            qtd=quantidade,
            user_id=user_id 
        )
        return self.repo.add_movimentacao(movimentacao)
    
    def update(self, movimentacao_id, new_data):
        """
        Atualiza movimentação existente
        Retorna True se sucesso, False se falhou
        """
        movimentacao = self.get_by_id(movimentacao_id)
        if not movimentacao:
            return False
            
        # Atualiza apenas campos permitidos
        if 'tipo' in new_data:
            movimentacao.tipo = new_data['tipo']
        if 'qtd' in new_data:
            movimentacao.qtd = new_data['qtd']
        
        try:
            return self.repo.update_movimentacao(movimentacao)
        except sqlite3.Error:
            return False
    
    def delete(self, movimentacao_id):
        """Remove movimentação pelo ID"""
        try:
            return self.repo.delete_movimentacao(movimentacao_id)
        except sqlite3.Error:
            return False
    
    def registrar_entrada(self, produto_id, quantidade, user_id):
        return self.save(produto_id, 'entrada', quantidade, user_id)
    
    def registrar_saida(self, produto_id, quantidade, user_id):
        return self.save(produto_id, 'saida', quantidade, user_id)