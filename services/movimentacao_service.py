import sqlite3
from datetime import datetime
from models.movimentacao import Movimentacao, movimentacao_repository

class MovimentacaoService:
    def __init__(self):
        self.repo = movimentacao_repository
    
    def get_all(self):
        """Retorna todas as movimentações"""
        return self.repo.get_all()
    
    def get_by_id(self, movimentacao_id):
        """Busca movimentação por ID"""
        return self.repo.get_by_id(movimentacao_id)
    
    def get_by_produto(self, produto_id):
        """Busca movimentações por produto"""
        return self.repo.get_by_produto_id(produto_id)
    
    def save(self, produto_id, tipo, quantidade):
        """
        Registra nova movimentação
        Retorna ID se sucesso, None se falhou
        """
        movimentacao = Movimentacao(
            id=None,
            produto_id=produto_id,
            data=datetime.now(),
            tipo=tipo,
            qtd=quantidade
        )
        
        try:
            return self.repo.add_movimentacao(movimentacao)
        except sqlite3.Error as e:
            print(f"Erro ao salvar movimentação: {e}")
            return None
    
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
    
    def registrar_entrada(self, produto_id, quantidade):
        """Método especializado para registrar entrada de estoque"""
        return self.save(produto_id, 'entrada', quantidade)
    
    def registrar_saida(self, produto_id, quantidade):
        """Método especializado para registrar saída de estoque"""
        return self.save(produto_id, 'saida', quantidade)