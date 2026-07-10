from utils import (formatarMoeda)
from models import (Objetos)


def gerarDadosRelatorio(lista):

    entradaTotal = 0
    saidaTotal = 0
    maiorEntrada = None
    maiorSaida = None
    gastosCategoria = {}
    entradasCategoria = {}

    for movimentacao in lista:
        if movimentacao.tipo.lower() == "entrada":
            entradaTotal += movimentacao.valor

            if maiorEntrada is None:
                maiorEntrada = movimentacao
            elif movimentacao.valor > maiorEntrada.valor:
                maiorEntrada = movimentacao

            if movimentacao.categoria not in entradasCategoria:
                entradasCategoria[movimentacao.categoria] = movimentacao.valor
            else:
                entradasCategoria[movimentacao.categoria] += movimentacao.valor

        elif movimentacao.tipo.lower() == "saida":

            saidaTotal += movimentacao.valor

            if maiorSaida is None:
                maiorSaida = movimentacao
            elif movimentacao.valor > maiorSaida.valor:
                maiorSaida = movimentacao

            if movimentacao.categoria not in gastosCategoria:
                gastosCategoria[movimentacao.categoria] = movimentacao.valor
            else: 
                gastosCategoria [movimentacao.categoria] += movimentacao.valor

    saldoFinal = entradaTotal - saidaTotal

    maiorCategoriaGasto = None
    
    for categoria in gastosCategoria:
            if maiorCategoriaGasto is None:
                maiorCategoriaGasto = categoria
            elif gastosCategoria[categoria] > gastosCategoria[maiorCategoriaGasto]:
                maiorCategoriaGasto = categoria 
    
    maiorCategoriaEntrada = None
    
    for categoria in entradasCategoria:
            if maiorCategoriaEntrada is None:
                maiorCategoriaEntrada = categoria
            elif entradasCategoria [categoria] > entradasCategoria[maiorCategoriaEntrada]:
                maiorCategoriaEntrada = categoria
                
    return {
            "entradaTotal": entradaTotal,
            "saidaTotal": saidaTotal, 
            "maiorEntrada": maiorEntrada, 
            "maiorSaida": maiorSaida, 
            "gastosCategoria": gastosCategoria,
            "entradasCategoria": entradasCategoria, 
            "maiorCategoriaGasto": maiorCategoriaGasto,
            "maiorCategoriaEntrada": maiorCategoriaEntrada,
            "saldoFinal" : saldoFinal
        }

def mostrarRelatório(lista):

    dados = gerarDadosRelatorio(lista)

    entradaTotal =  dados["entradaTotal"]
    saidaTotal = dados["saidaTotal"]
    saldoFinal = dados["saldoFinal"]
    maiorEntrada = dados["maiorEntrada"]
    maiorSaida = dados["maiorSaida"]
    maiorCategoriaGasto = dados["maiorCategoriaGasto"]
    maiorCategoriaEntrada = dados["maiorCategoriaEntrada"]
    gastosCategoria = dados["gastosCategoria"]
    entradasCategoria = dados["entradasCategoria"]

    entradaFormatada = formatarMoeda(entradaTotal)
    saidaFormatada = formatarMoeda(saidaTotal)
    saldoFormatado = formatarMoeda(saldoFinal)

    if maiorEntrada is not None:
           maiorEntradaFormatada = formatarMoeda(maiorEntrada.valor)
           maiorEntradaValidacao = (
               f"{maiorEntrada.nome} - R${maiorEntradaFormatada}"
           )
    else:
        maiorEntradaValidacao = "Nenhuma entrada cadastrada"


    if maiorSaida is not None:
        maiorSaidaFormatada = formatarMoeda(maiorSaida.valor)
        maiorSaidaValidacao = (
            f"{maiorSaida.nome} - R${maiorSaidaFormatada}"
        )
    else: 
        maiorSaidaValidacao = "Nenhuma saída cadastrada"


    if maiorCategoriaGasto is not None:
            maiorCategoriaGastoFormatada = formatarMoeda(gastosCategoria[maiorCategoriaGasto])
            maiorCategoriaGastoValidacao = (f"{maiorCategoriaGasto} - R${maiorCategoriaGastoFormatada}")
    else:
            maiorCategoriaGastoValidacao = ("Nenhuma saída cadastrada")

    
    if maiorCategoriaEntrada is not None:
            maiorCategoriaEntradaFormatada = formatarMoeda(entradasCategoria[maiorCategoriaEntrada])
            maiorCategoriaEntradaValidacao = (f"{maiorCategoriaEntrada} - R${maiorCategoriaEntradaFormatada}")
    else:
            maiorCategoriaEntradaValidacao = ("Nenhuma entrada cadastrada")

   
    
    print("="*15)
    print("RELATÓRIO FINANCEIRO")
    print("="*15)

    print()

    print(f"Entradas: R${entradaFormatada}")
    print(f"Saídas: R${saidaFormatada}")
    print(f"Saldo: R${saldoFormatado}")

    print()

    print(f"Maior entrada: {maiorEntradaValidacao}")
    print(f"Maior saída: {maiorSaidaValidacao}")
    print(f"Maior categoria de gastos: {maiorCategoriaGastoValidacao}")
    print(f"Maior categoria de entradas: {maiorCategoriaEntradaValidacao}")

    print()

    print("=" *15)
    print("Gastos por Categoria")
    print("="*15)

    for categoria in gastosCategoria:
            valorFormatadoSaidas = formatarMoeda(gastosCategoria[categoria])
            print(f"{categoria}: R${valorFormatadoSaidas}")
            print()

    print("=" *15)
    print("Entradas por Categoria")
    print("="*15)

    for categoria in entradasCategoria:
        valorFormatadoEntradas = formatarMoeda(entradasCategoria[categoria])
        print(f"{categoria}: R${valorFormatadoEntradas}")
        print()

