class Produto:
    def __init__(self, id, nome, descricao, preco, qtd_estoque, qtd_minima, fornecedor_id):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.qtd_estoque = qtd_estoque
        self.qtd_minima =  qtd_minima
        self.fornecedor_id = fornecedor_id

def to_dict(self):
    return{
        "id": self.id,
        "nome": self.nome,
        "descricao": self.descricao,
        "preco": self.preco,
        "qtd_estoque": self. qtd_estoque,
        "qtd_minima": self.qtd_minima,
        "fornecedor_id": self.fornecedor_id
    } 

    @staticmethod
    def from_dict(data):
        return Produto(data["id"], data["nome"], data["descricao"], data["preco"], data["qtd_estoque"], data["qtd_minima"], data["fornecedor_id"])

    def verificar_reposicao(self):
        return self.qtd_estoque < self.qtd_minima

    def registrar_movimentacao(self, tipo, quantidade):
        if tipo == "entrada":
            self.qtd_estoque += quantidade
        elif tipo == "saida":
            self.qtd_estoque -= quantidade
        else:
            raise ValueError("Tipo de movimentação inválido. Use 'entrada' ou 'saida'.")