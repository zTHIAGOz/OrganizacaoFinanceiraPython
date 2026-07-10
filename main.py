from utils import (cabecalho)
from persistencia import(carregarJson, consultaMensal, exportarCSV)
from models import (Objetos)
from relatorios import (mostrarRelatório)
from crud import (adicionar, listar, mostrarSaldo, filtrarCategoria, filtrarData, editar, remover)

def menu():
    print(
        "\n1 - Adicionar movimentação"
        "\n2 - Listar movimentações"
        "\n3 - Mostrar saldo"
        "\n4 - Filtrar por categoria"
        "\n5 - Filtrar por data"
        "\n6 - Editar movimentação"
        "\n7 - Remover movimentação"
        "\n8 - Relatório financeiro"
        "\n9 - Consultar histórico mensal"
        "\n10 - Exportar arquivo CSV"
        "\n11 - Sair\n"

        
    )
            
lista = []
carregarJson(lista)


while True:

    cabecalho()

    menu()
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        adicionar(lista)
    
    elif opcao == "2":
        listar(lista)
    
    elif opcao == "3":
        mostrarSaldo(lista)
    
    elif opcao == "4":
        filtrarCategoria(lista)

    elif opcao == "5":
        filtrarData(lista)

    elif opcao == "6":
        editar(lista)
        
    elif opcao == "7":
        remover(lista)
        
    elif opcao == "8":
        mostrarRelatório(lista)

    elif opcao == "9":
        consultaMensal(lista)

    elif opcao == "10":
        exportarCSV(lista)

    elif opcao == "11":
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida!")