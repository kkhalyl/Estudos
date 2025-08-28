import random

class Produto:
    def __init__(self):
        self.nome = ""
        self.unidade = ""
        self.quantidade = 0
        self.descricao = ""
        self.id = 000
    
    def mostrar_produto_simples(self):
        return f"\nID: {self.id}\nNome: {self.nome}\nQuantidade: {self.quantidade}"

    def mostrar_produto(self):
        return f"\nID: {self.id}\nNome: {self.nome}\nUnidade: {self.unidade}\nQuantidade: {self.quantidade}\nDescricao: {self.descricao}"

def mostra_produtos(lista):
    if lista == []:
        print("Não há objetos na lista.")
    else:
        for obj in lista:
            print(obj.mostrar_produto_simples())

def unidade(opcao):
    if opcao=='A':
        return "Quilograma"
    elif opcao=='B':
        return "Grama"
    elif opcao=='C':
        return "Litro"
    elif opcao=='D':
        return "Mililitro"
    elif opcao=='E':
        return "Unidade"
    elif opcao=='F':
        return "Metro"
    elif opcao=='G':
        return "Centímetro"

def adicionar_novo():
    id_rand=random.randint(1,10)
    produto=Produto()
    produto.nome=input("Qual o nome do seu produto?\n")
    produto.unidade=unidade(input("Qual a unidade de medida do seu produto?\nA. Quilograma\nB. Grama\nC. Litro\nD. Mililitro\nE. Unidade\nF. Metro\nG. Centímetro\n").upper())
    produto.quantidade=int(input("Quantos produtos você irá adicionar?\n"))
    produto.descricao=input("Dê uma descrição básica do seu produto\n")
    produto.id = len(produto.unidade)+id_rand+(100*id_rand)
    print("Produto adicionado!")
    return produto

def adicionar(lista, id):
    for obj in lista:
        if obj.id == id:
            print("Quantidade deste produto:", obj.quantidade)
            qtd=int(input("Quanto você quer adicionar à esse produto?\n"))
            obj.quantidade+=qtd
            print("Produto adicionado!")
            return lista
    print("Produto não encontrado!")

def remover(lista, id):
    for obj in lista:
        if obj.id == id:
            print("Quantidade deste produto:", obj.quantidade)
            qtd=int(input("Quanto você quer remover desse produto?\n"))
            obj.quantidade-=qtd
            if obj.quantidade == 0:
                lista.remove(obj)
            print("Produto removido!")
            return lista
    print("Produto não encontrado!")

def pesquisar_por_nome(lista, nome):
    n_resultados=0
    for obj in lista:
        nomeo=obj.nome.upper()
        if nomeo == nome or (nomeo[:3]==nome[:3]):
            n_resultados+=1
            print(obj.mostrar_produto())
    if n_resultados==0:
        print("Produto não encontrado!")

def menu_opcoes(lista):
    print("Bem vindo ao Gerenciador de Lista de Compras! O que você deseja fazer?")
    mostra_produtos(lista)
    resposta=input("A. Adicionar Produto\nB. Remover Produto\nC. Pesquisar Produtos\nD. Sair do Programa\n").upper()

    if resposta not in ['A', 'B', 'C', 'D']:
        print("Resposta inválida")

    if resposta == 'A':
        if(input("1. Adicionar novo produto\n2. Adicionar produto existente\n"))=='1':
            lista.append(adicionar_novo())
        else:
            if lista == []:
                print("Ainda não há objetos na lista.")
            else:
                id=int(input("Insira o ID do objeto a ser adicionado\n"))
                lista = adicionar(lista, id)

    elif resposta == 'B':
        if lista == []:
            print("Ainda não há objetos na lista.")
        else:
            id=int(input("Insira o ID do objeto a ser removido\n"))
            lista = remover(lista, id)

    elif resposta == 'C':
        nome = ""
        while nome!="SAIR":
            nome=input("Pesquisar:\n").upper()
            pesquisar_por_nome(lista, nome)
            print("\nDigite SAIR para fechar a pesquisa").upper()

    elif resposta == 'D':
        print("Obrigado por utilizar nosso gerenciador!")
        return -1

    else:
        print("Resposta inválida!")

    return lista

x=1
lista = []
while x!=-1:
    x=menu_opcoes(lista)

