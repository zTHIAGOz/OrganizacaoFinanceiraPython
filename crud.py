from utils import (entrada, entradaFloat, validacaoTipo, escolherData, formatarMoeda)
from models import (Objetos)
from persistencia import (inserirMovimentacao, listarMovimentacoes, atualizarMovimentacao, deletarMovimentacao)


def adicionar(lista):
    nome = entrada("Nome da movimentação: ")
    valor = entradaFloat("Valor da movimentação: ")
    tipo = validacaoTipo("Qual o tipo da movimentação (entrada/saida): ")
    data = escolherData()
    categoria = entrada("Digite a categoria: ")
    
    movimentacao = Objetos(nome, valor, tipo, data, categoria)
    inserirMovimentacao(movimentacao)
    
    
    lista.clear()
    lista.extend(listarMovimentacoes())
    print("Movimentação cadastrada com sucesso!")

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
            
    if not encontrar:
        print("Categoria não encontrada!")

def filtrarData(lista):
    encontrar = False
    filtroData = input("Qual data deseja acessar:")
    for u in lista:
        if filtroData == u.data:
            u.mostrarResultado()
            encontrar = True
    if not encontrar:
        print("Data não encontrada")

def editar(lista):
    listar(lista)
    try:
        idEscolhido = int(input("\nDigite o ID da movimentação que deseja editar: "))
    except ValueError:
        print("ID inválido! Digite apenas o número.")
        return

    for movimentacao in lista:
        if movimentacao.id == idEscolhido:
            movimentacao.nome = entrada("Qual o novo nome: ")
            movimentacao.valor = entradaFloat("Qual o novo valor: ")
            movimentacao.tipo = validacaoTipo("Qual o novo tipo (entrada/saida): ")
            movimentacao.data = entrada("Qual a nova data (dd/mm/aaaa): ")
            movimentacao.categoria = entrada("Qual a nova categoria: ")
            
            atualizarMovimentacao(movimentacao)
            print("Editada com sucesso!")
            return
            
    print("ID não encontrado!")

def remover(lista):
    listar(lista)
    try:
        idEscolhido = int(input("\nDigite o ID da movimentação que deseja remover: "))
    except ValueError:
        print("ID inválido! Digite apenas o número.")
        return

    for movimentacao in lista:
        if movimentacao.id == idEscolhido:
            deletarMovimentacao(idEscolhido)
            lista.remove(movimentacao)
            print("Movimentação removida com sucesso!")
            return
            
    print("ID não encontrado!")
