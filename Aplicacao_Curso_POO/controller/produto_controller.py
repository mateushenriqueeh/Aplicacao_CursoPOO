from model.produto import Produto
from model.categoria import Categoria
from model.fornecedor import Fornecedor
from model.historico import HistoricoAlteracoes

class ProdutoController:
    def __init__(self):
        self.produtos = []
        self.historico = HistoricoAlteracoes()
        self.id_counter = 1  # Variável para gerar IDs sequenciais
        
        # Produtos iniciais - Peças para Máquinas Agrícolas
        categoria_pecas_trator = Categoria("Peças para Tratores")
        fornecedor1 = Fornecedor("AgroFornecedora Tratores", "123456789")
        produto1 = Produto(self.id_counter, "Pneu Trator 18.4R30", 1200.50, categoria_pecas_trator, fornecedor1)
        self.produtos.append(produto1)
        self.historico.registrar_alteracao(produto1, "Cadastro", "N/A", "Criado")
        self.id_counter += 1  # Incrementa o contador para o próximo ID

        categoria_pecas_colheitadeira = Categoria("Peças para Colheitadeiras")
        fornecedor2 = Fornecedor("AgroFornecedora Colheitadeiras", "987654321")
        produto2 = Produto(self.id_counter, "Faca Colheitadeira John Deere", 450.00, categoria_pecas_colheitadeira, fornecedor2)
        self.produtos.append(produto2)
        self.historico.registrar_alteracao(produto2, "Cadastro", "N/A", "Criado")
        self.id_counter += 1  # Incrementa o contador para o próximo ID

        categoria_pecas_trator = Categoria("Peças para Tratores")
        fornecedor3 = Fornecedor("AgroFornecedora Tratores", "111222333")
        produto3 = Produto(self.id_counter, "Bomba Hidráulica Trator Massey", 650.00, categoria_pecas_trator, fornecedor3)
        self.produtos.append(produto3)
        self.historico.registrar_alteracao(produto3, "Cadastro", "N/A", "Criado")
        self.id_counter += 1  # Incrementa o contador para o próximo ID
        
        categoria_pecas_colheitadeira = Categoria("Peças para Colheitadeiras")
        fornecedor4 = Fornecedor("AgroFornecedora Colheitadeiras", "444555666")
        produto4 = Produto(self.id_counter, "Correia Colheitadeira Case IH", 200.00, categoria_pecas_colheitadeira, fornecedor4)
        self.produtos.append(produto4)
        self.historico.registrar_alteracao(produto4, "Cadastro", "N/A", "Criado")
        self.id_counter += 1  # Incrementa o contador para o próximo ID
        
        categoria_pecas_implementos = Categoria("Peças para Implementos Agrícolas")
        fornecedor5 = Fornecedor("AgroFornecedora Implementos", "777888999")
        produto5 = Produto(self.id_counter, "Pino de Reboque Implemento", 75.00, categoria_pecas_implementos, fornecedor5)
        self.produtos.append(produto5)
        self.historico.registrar_alteracao(produto5, "Cadastro", "N/A", "Criado")
        self.id_counter += 1  # Incrementa o contador para o próximo ID
        
        categoria_pecas_implementos = Categoria("Peças para Implementos Agrícolas")
        fornecedor6 = Fornecedor("AgroFornecedora Implementos", "101112131")
        produto6 = Produto(self.id_counter, "Engate Rápido Implemento", 100.00, categoria_pecas_implementos, fornecedor6)
        self.produtos.append(produto6)
        self.historico.registrar_alteracao(produto6, "Cadastro", "N/A", "Criado")
        self.id_counter += 1  # Incrementa o contador para o próximo ID

    def cadastrar_produto(self, nome, preco, categoria_nome, fornecedor_nome, fornecedor_contato):
        categoria = Categoria(categoria_nome)
        fornecedor = Fornecedor(fornecedor_nome, fornecedor_contato)
        produto = Produto(self.id_counter, nome, preco, categoria, fornecedor)
        self.produtos.append(produto)
        self.historico.registrar_alteracao(produto, "Cadastro", "N/A", "Criado")
        self.id_counter += 1  # Incrementa o contador para o próximo ID

    def listar_produtos(self):
        return [produto.exibir_info() for produto in self.produtos]

    def listar_historico(self):
        return self.historico.listar_alteracoes()

    def alterar_produto(self, produto_id, campo, novo_valor):
        for produto in self.produtos:
            if produto.produto_id == produto_id:
                if campo == "nome":
                    antigo_valor = produto.nome
                    produto.nome = novo_valor
                elif campo == "preco":
                    antigo_valor = produto.preco
                    produto.preco = float(novo_valor)
                else:
                    return "Campo inválido"
                self.historico.registrar_alteracao(produto, campo, antigo_valor, novo_valor)
                return "Produto alterado com sucesso."
        return "Produto não encontrado."

    def excluir_produto(self, produto_id):
        for produto in self.produtos:
            if produto.produto_id == produto_id:
                self.produtos.remove(produto)
                self.historico.registrar_alteracao(produto, "Exclusão", produto.nome, "Removido")
                return "Produto excluído com sucesso."
        return "Produto não encontrado."

    def consultar_produto_por_nome(self, nome):
        produtos_encontrados = [produto for produto in self.produtos if nome.lower() in produto.nome.lower()]
        if produtos_encontrados:
            return [produto.exibir_info() for produto in produtos_encontrados]
        else:
            return "Nenhum produto encontrado com esse nome."
