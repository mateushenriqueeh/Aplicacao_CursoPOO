import tkinter as tk
from tkinter import messagebox
from controller.produto_controller import ProdutoController

class ProdutoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicação de Produtos")
        self.produto_controller = ProdutoController()

        # Inicializando variáveis para armazenar widgets
        self.label = None
        self.campo_nome = None
        self.campo_preco = None
        self.campo_categoria = None
        self.campo_fornecedor_nome = None
        self.campo_fornecedor_contato = None
        self.campo_nome_consulta = None
        self.botoes = []

        self.create_widgets()
    
    def create_widgets(self):
        # Estilo para os botões
        button_style = {"width": 20, "height": 2, "font": ("Arial", 12)}

        # Menu de opções
        self.label = tk.Label(self.root, text="Escolha uma opção:", font=("Arial", 14))
        self.label.grid(row=0, column=0, columnspan=2, pady=20)

        self.btn_cadastrar = tk.Button(self.root, text="Cadastrar Produto", command=self.cadastrar_produto, **button_style)
        self.btn_cadastrar.grid(row=1, column=0, pady=10)

        self.btn_listar = tk.Button(self.root, text="Listar Produtos", command=self.listar_produtos, **button_style)
        self.btn_listar.grid(row=2, column=0, pady=10)

        self.btn_alterar = tk.Button(self.root, text="Alterar Produto", command=self.alterar_produto, **button_style)
        self.btn_alterar.grid(row=3, column=0, pady=10)

        self.btn_excluir = tk.Button(self.root, text="Excluir Produto", command=self.excluir_produto, **button_style)
        self.btn_excluir.grid(row=4, column=0, pady=10)

        self.btn_historico = tk.Button(self.root, text="Ver Histórico", command=self.ver_historico, **button_style)
        self.btn_historico.grid(row=5, column=0, pady=10)

        self.btn_consultar = tk.Button(self.root, text="Consultar Produto", command=self.consultar_produto, **button_style)
        self.btn_consultar.grid(row=6, column=0, pady=10)

        self.btn_sair = tk.Button(self.root, text="Sair", command=self.sair, **button_style)
        self.btn_sair.grid(row=7, column=0, pady=10)

        # Redefinindo área de entrada dos dados
        self.container_dados = tk.Frame(self.root)
        self.container_dados.grid(row=0, column=1, rowspan=8, padx=20)

    def limpar_area_dados(self):
        for widget in self.container_dados.winfo_children():
            widget.destroy()

    def cadastrar_produto(self):
        self.limpar_area_dados()
        tk.Label(self.container_dados, text="Cadastrar Produto", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)
        
        # Campos para cadastrar o produto (sem o ID)
        tk.Label(self.container_dados, text="Nome:").grid(row=1, column=0, sticky='e', pady=5)
        self.campo_nome = tk.Entry(self.container_dados)
        self.campo_nome.grid(row=1, column=1)

        tk.Label(self.container_dados, text="Preço:").grid(row=2, column=0, sticky='e', pady=5)
        self.campo_preco = tk.Entry(self.container_dados)
        self.campo_preco.grid(row=2, column=1)

        tk.Label(self.container_dados, text="Categoria:").grid(row=3, column=0, sticky='e', pady=5)
        self.campo_categoria = tk.Entry(self.container_dados)
        self.campo_categoria.grid(row=3, column=1)

        tk.Label(self.container_dados, text="Fornecedor Nome:").grid(row=4, column=0, sticky='e', pady=5)
        self.campo_fornecedor_nome = tk.Entry(self.container_dados)
        self.campo_fornecedor_nome.grid(row=4, column=1)

        tk.Label(self.container_dados, text="Fornecedor Contato:").grid(row=5, column=0, sticky='e', pady=5)
        self.campo_fornecedor_contato = tk.Entry(self.container_dados)
        self.campo_fornecedor_contato.grid(row=5, column=1)

        # Botão para salvar
        tk.Button(self.container_dados, text="Salvar", command=self.salvar_produto, **{"width": 20, "height": 2, "font": ("Arial", 12)}).grid(row=6, column=0, columnspan=2, pady=20)

    def salvar_produto(self):
        try:
            nome = self.campo_nome.get()
            preco = float(self.campo_preco.get())
            categoria = self.campo_categoria.get()
            fornecedor_nome = self.campo_fornecedor_nome.get()
            fornecedor_contato = self.campo_fornecedor_contato.get()
            self.produto_controller.cadastrar_produto(nome, preco, categoria, fornecedor_nome, fornecedor_contato)
            messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
            self.limpar_area_dados()
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos.")

    def listar_produtos(self):
        self.limpar_area_dados()
        tk.Label(self.container_dados, text="Produtos Cadastrados", font=("Arial", 16)).grid(row=0, column=0, pady=10)

        produtos = self.produto_controller.listar_produtos()
        for i, produto in enumerate(produtos):
            tk.Label(self.container_dados, text=str(produto)).grid(row=i+1, column=0, pady=5)

    def alterar_produto(self):
        self.limpar_area_dados()
        tk.Label(self.container_dados, text="Alterar Produto", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(self.container_dados, text="ID do Produto:").grid(row=1, column=0, sticky='e', pady=5)
        self.campo_id = tk.Entry(self.container_dados)
        self.campo_id.grid(row=1, column=1)

        tk.Label(self.container_dados, text="Campo a alterar (nome/preço):").grid(row=2, column=0, sticky='e', pady=5)
        self.campo_nome = tk.Entry(self.container_dados)
        self.campo_nome.grid(row=2, column=1)

        tk.Label(self.container_dados, text="Novo Valor:").grid(row=3, column=0, sticky='e', pady=5)
        self.campo_preco = tk.Entry(self.container_dados)
        self.campo_preco.grid(row=3, column=1)

        tk.Button(self.container_dados, text="Alterar", command=self.salvar_alteracao, **{"width": 20, "height": 2, "font": ("Arial", 12)}).grid(row=4, column=0, columnspan=2, pady=20)

    def salvar_alteracao(self):
        try:
            id = int(self.campo_id.get())
            campo = self.campo_nome.get()
            novo_valor = self.campo_preco.get()
            self.produto_controller.alterar_produto(id, campo, novo_valor)
            messagebox.showinfo("Sucesso", "Produto alterado com sucesso!")
            self.limpar_area_dados()
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos.")

    def excluir_produto(self):
        self.limpar_area_dados()
        tk.Label(self.container_dados, text="Excluir Produto", font=("Arial", 16)).grid(row=0, column=0, pady=10)

        tk.Label(self.container_dados, text="ID do Produto:").grid(row=1, column=0, sticky='e', pady=5)
        self.campo_id = tk.Entry(self.container_dados)
        self.campo_id.grid(row=1, column=1)

        tk.Button(self.container_dados, text="Excluir", command=self.salvar_exclusao, **{"width": 20, "height": 2, "font": ("Arial", 12)}).grid(row=2, column=0, columnspan=2, pady=20)

    def salvar_exclusao(self):
        try:
            id = int(self.campo_id.get())
            self.produto_controller.excluir_produto(id)
            messagebox.showinfo("Sucesso", "Produto excluído com sucesso!")
            self.limpar_area_dados()
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um ID válido.")

    def ver_historico(self):
        self.limpar_area_dados()
        tk.Label(self.container_dados, text="Histórico de Alterações", font=("Arial", 16)).grid(row=0, column=0, pady=10)

        historico = self.produto_controller.listar_historico()
        for i, registro in enumerate(historico):
            tk.Label(self.container_dados, text=str(registro)).grid(row=i+1, column=0, pady=5)

    def consultar_produto(self):
        self.limpar_area_dados()
        tk.Label(self.container_dados, text="Consultar Produto", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(self.container_dados, text="Nome do Produto:").grid(row=1, column=0, sticky='e', pady=5)
        self.campo_nome_consulta = tk.Entry(self.container_dados)
        self.campo_nome_consulta.grid(row=1, column=1)

        tk.Button(self.container_dados, text="Consultar", command=self.realizar_consulta, **{"width": 20, "height": 2, "font": ("Arial", 12)}).grid(row=2, column=0, columnspan=2, pady=20)

    
    def realizar_consulta(self):
        nome = self.campo_nome_consulta.get()
        produtos = self.produto_controller.consultar_produto_por_nome(nome)
        
        # Limpar resultados anteriores, se houver
        for widget in self.container_dados.winfo_children():
            if isinstance(widget, tk.Label) and widget != self.campo_nome_consulta:  # Exclui o campo de entrada
                widget.grid_forget()
        
        if produtos:
            # Exibir os produtos, um por linha
            for i, produto in enumerate(produtos, start=3):  # Começando da linha 3
                tk.Label(self.container_dados, text=str(produto)).grid(row=i, column=0, columnspan=2, pady=5)
        else:
            messagebox.showinfo("Resultado", "Produto não encontrado.")

    def sair(self):
        self.root.quit()


def main():
    root = tk.Tk()
    app = ProdutoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
