from model.estoque import Estoque
class EstoqueController:
    def __init__(self):
        self.estoque = Estoque()
    def adicionar_produto(self, produto, quantidade):
        self.estoque.adicionar_produto(produto, quantidade)
    def listar_estoque(self):
        return self.estoque.listar_estoque()