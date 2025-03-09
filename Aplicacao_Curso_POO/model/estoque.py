from .produto import Produto
class Estoque:
    def __init__(self):
        self.__produtos = {}
    def adicionar_produto(self, produto, quantidade):
        if produto in self.__produtos:
            self.__produtos[produto] += quantidade
        else:
            self.__produtos[produto] = quantidade
    def remover_produto(self, produto, quantidade):
        if produto in self.__produtos and self.__produtos[produto] >= quantidade:
            self.__produtos[produto] -= quantidade
        else:
            raise ErroEstoqueNegativo(produto.nome)
    def listar_estoque(self):
        return [f"{produto.exibir_info()} | Quantidade: {qtd}" for produto, qtd in self.__produtos.items()]
class ErroEstoqueNegativo(Exception):
    def __init__(self, produto_nome):
        super().__init__(f"Estoque insuficiente para o produto: {produto_nome}")
