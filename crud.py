from utils import (entrada,validacaoTipo, escolherData, formatarMoeda)
from models import (Objetos)
from persistencia import (salvarJson)


def adicionar(lista):
    nome = entrada("Nome da movimentação: ")
    valor = float(entrada("Valor da movimentação: "))
    tipo = validacaoTipo("Qual o tipo da movimentação (entrada/saida): ")
    data = escolherData()
    categoria = entrada ("Digite a categoria: ")
    movimentacao = Objetos(nome, valor, tipo, data, categoria)
    lista.append(movimentacao)
    print("Movimentação cadastrada com sucesso!")
    salvarJson()

def listar(lista):
    print("\nMovimentações cadastradas:\n")
    for movimentacao in lista:
        movimentacao.mostrarResultado()

def mostrarSaldo(lista):
    saldoTotal = 0
    for movimentacao in lista:
        if movimentacao.tipo.lower() == "entrada":
            saldoTotal += movimentacao.valor
        elif movimentacao.tipo.lower() == "saida":
            saldoTotal -= movimentacao.valor
    saldoFormatado = formatarMoeda(saldoTotal)
    print(f"\nSaldo atual: R${saldoFormatado}")

def filtrarCategoria(lista):
    encontrar = False
    categoria = input("Qual categoria deseja acessar:")
    for movimentacao in lista:
        if categoria.lower() == movimentacao.categoria.lower():
            movimentacao.mostrarResultado()
            encontrar = True
            
    if encontrar == False:
        print("Categoria não encontrada!")

def filtrarData(lista):
    encontrar = False
    filtroData = input("Qual data deseja acessar:")
    for u in lista:
        if filtroData == u.data:
            u.mostrarResultado()
            encontrar = True
    if encontrar == False:
        print("Data não encontrada")

def editar(lista):
    encontrar = False
    edicao = input("Qual movimentação deseja editar: ")
    for movimentacao in lista:
        if edicao.lower() == movimentacao.nome.lower():
            novoNome = entrada("Qual o novo nome: ")
            novoValor = float(entrada("Qual o novo valor: "))
            novoTipo = validacaoTipo("Qual  o novo tipo: ")
            novaData = entrada("Qual a nova data: ")
            novaCategoria = entrada("Qual a nova categoria: ")
            movimentacao.nome = novoNome
            movimentacao.valor = novoValor
            movimentacao.tipo = novoTipo
            movimentacao.data = novaData
            movimentacao.categoria = novaCategoria
            encontrar = True
            print("Editada com sucesso!")
            salvarJson()
    if encontrar == False:
        print("Movimentação não encontrada!")

def remover (lista):
    encontrar = False
    removendo = input("Qual movimentação deseja remover: ")
    for movimentacao in lista: 
        if removendo.lower() == movimentacao.nome.lower():
            lista.remove(movimentacao)
            print("Movimentação removida com sucesso!")
            salvarJson()
            encontrar = True
            break
    if encontrar == False:
        print("Movimentação não encontrada")