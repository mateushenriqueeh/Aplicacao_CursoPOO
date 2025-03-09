class HistoricoAlteracoes:
    def __init__(self):
        self.__alteracoes = []
    def registrar_alteracao(self, produto, campo, valor_antigo, valor_novo):
        self.__alteracoes.append(f"{produto.nome}: {campo} alterado de {valor_antigo} para {valor_novo}")
    def listar_alteracoes(self):
        return self.__alteracoes