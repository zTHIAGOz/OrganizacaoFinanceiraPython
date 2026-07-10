from utils import cabecalho
from utils import entrada
from utils import validacaoTipo
from utils import escolherData
from utils import formatarMoeda

class Objetos:

    def __init__(self, nome, valor, tipo, data, categoria):
        self.nome = nome
        self.valor = valor
        self.tipo = tipo
        self.data = data
        self.categoria = categoria

    def mostrarResultado(self):
        valorFormatado = formatarMoeda(self.valor)
        if self.tipo.lower() == "entrada":
            print(f"{self.nome} - +R${valorFormatado} - {self.data} - {self.categoria}")
        elif self.tipo.lower() == "saida":
            print(f"{self.nome} - -R${valorFormatado} - {self.data} - {self.categoria}")
        else:
            print(f"{self.nome} - R${valorFormatado} - {self.data} - {self.categoria}")

    def conversao(self):
        return {
        "nome" : self.nome,
        "valor" : self.valor,
        "tipo": self.tipo,
        "data" : self.data,
        "categoria" : self.categoria
    }

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

def adicionar():
    nome = entrada("Nome da movimentação: ")
    valor = float(entrada("Valor da movimentação: "))
    tipo = validacaoTipo("Qual o tipo da movimentação (entrada/saida): ")
    data = escolherData()
    categoria = entrada ("Digite a categoria: ")
    movimentacao = Objetos(nome, valor, tipo, data, categoria)
    lista.append(movimentacao)
    print("Movimentação cadastrada com sucesso!")
    salvarJson()

def listar():
    print("\nMovimentações cadastradas:\n")
    for movimentacao in lista:
        movimentacao.mostrarResultado()

def mostrarSaldo():
    saldoTotal = 0
    for movimentacao in lista:
        if movimentacao.tipo.lower() == "entrada":
            saldoTotal += movimentacao.valor
        elif movimentacao.tipo.lower() == "saida":
            saldoTotal -= movimentacao.valor
    saldoFormatado = formatarMoeda(saldoTotal)
    print(f"\nSaldo atual: R${saldoFormatado}")

def filtrarCategoria():
    encontrar = False
    categoria = input("Qual categoria deseja acessar:")
    for movimentacao in lista:
        if categoria.lower() == movimentacao.categoria.lower():
            movimentacao.mostrarResultado()
            encontrar = True
            
    if encontrar == False:
        print("Categoria não encontrada!")
            
            
            
import datetime
import json

def filtrarData():
    encontrar = False
    filtroData = input("Qual data deseja acessar:")
    for u in lista:
        if filtroData == u.data:
            u.mostrarResultado()
            encontrar = True
    if encontrar == False:
        print("Data não encontrada")

def editar():
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

def remover ():
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

def salvarJson():
    listaJson = []
    for movimentacao in lista:
        listaJson.append(movimentacao.conversao())
    with open (nomeArquivo(), "w") as arquivo : #abri dados.json em modo escrita e chamar ele de arquivo (o w é de write)
        json.dump( #escreva a listajson dentro do arquivo (codigo abaixo)
            listaJson,
            arquivo,
            indent=4
            )

def carregarJson():
    try:
        with open (nomeArquivo(), "r") as arquivo: #abrir dadosjson(é o arquivo) em modo leitura e chamar ele de arquivo (o r é de read)
            dados = json.load(arquivo) #carrega os dados em modo lista de dicionario 
            for item in dados: #percorre cada item do dicionario
                movimentacao = Objetos(
                item ["nome"],
                item ["valor"],
                item ["tipo"],
                item ["data"],
                item ["categoria"]
            )
                lista.append(movimentacao)
    except FileNotFoundError:
        pass

def gerarDadosRelatorio():

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

def mostrarRelatório():

    dados = gerarDadosRelatorio()

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

def nomeArquivo():
    data = datetime.datetime.now()
    dataFormatada = data.strftime("%Y-%m")
    return dataFormatada + ".json"

def consultaMensal():
    mes = input("Digite o mês de consulta: (ano/mes - '2026-05' por exemplo) ").strip()
    arquivoConsulta = mes + ".json"
    try:
        with open (arquivoConsulta, "r") as arquivo:
            dados = json.load(arquivo)
            for item in dados:
                valorFormatado = formatarMoeda(item["valor"])
                print (f"{item['nome']} - R${valorFormatado} - {item['data']} - {item['categoria']}")

    except FileNotFoundError:
            print("Nenhum registro encontrado!")

def exportarCSV():
        with open ("relatorio.csv", "w") as arquivo:
            arquivo.write("Nome, Valor, Tipo, Data, Categoria\n")
            for movimentacao in lista:
                arquivo.write(f"{movimentacao.nome},"
                              f"{movimentacao.valor},"
                              f"{movimentacao.tipo},"
                              f"{movimentacao.data},"
                              f"{movimentacao.categoria}\n")
    
lista = []
carregarJson()


while True:

    cabecalho()

    menu()
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        adicionar()
    
    elif opcao == "2":
        listar()
    
    elif opcao == "3":
        mostrarSaldo()
    
    elif opcao == "4":
        filtrarCategoria()

    elif opcao == "5":
        filtrarData()

    elif opcao == "6":
        editar()
        
    elif opcao == "7":
        remover()
        
    elif opcao == "8":
        mostrarRelatório()

    elif opcao == "9":
        consultaMensal()

    elif opcao == "10":
        exportarCSV()

    elif opcao == "11":
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida!")