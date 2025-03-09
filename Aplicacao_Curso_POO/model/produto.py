from .entidade import Entidade
from .categoria import Categoria
class Produto(Entidade):
    def __init__(self, produto_id: int, nome: str, preco: float, categoria: Categoria, fornecedor):
        self.__produto_id = produto_id
        self.__nome = nome
        self.__preco = self.__validar_preco(preco)
        self.__categoria = categoria
        self.__fornecedor = fornecedor
    
    def __validar_preco(self, preco):
        if preco <= 0:
            raise ValueError("O preço deve ser maior que zero.")
        return preco

    @property
    def produto_id(self):
        return self.__produto_id

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, novo_preco):
        self.__preco = self.__validar_preco(novo_preco)
    
    @property
    def categoria(self):
        return self.__categoria.nome

    @property
    def fornecedor(self):
        return f"{self.__fornecedor.nome} ({self.__fornecedor.contato})"

    def exibir_info(self):
        return f"{self.__produto_id} - {self.__nome} | R$ {self.__preco:.2f} | Categoria: {self.__categoria.nome} | Fornecedor: {self.fornecedor}"