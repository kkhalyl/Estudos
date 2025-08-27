class Produto:
    def __init__(self):
        self.nome = ""
        self.unidade = ""
        self.quantidade = 0
        self.descricao = ""

def adicionar():
    
def remover():

def listar():

def menu_opcoes():
    print("Bem vindo ao Gerenciador de Lista de Compras! O que você deseja fazer?")
    resposta=input("A. Adicionar Produto\nB. Remover Produto\nC. Pesquisar Produtos\nD. Sair do Programa")

    if resposta not in ['A', 'B', 'C', 'D']:
        print("Resposta inválida")

    if resposta == 'A':
        adicionar()

    elif resposta == 'B'
        remover()

    elif resposta == 'C'
        listar()

    elif resposta == 'D':
        print("Obrigado por utilizar nosso gerenciador!")

    else:
        print("Resposta inválida!")


