class Objetos:
    
    def __init__(self, nome, valor, tipo, data, categoria):
        self.nome = nome
        self.valor = valor
        self.tipo = tipo
        self.data = data
        self.categoria = categoria
    
    def mostrar_resultado(self):    
        valorFormatado = f"{self.valor:.2f}".replace(".",",")
        if self.tipo.lower() == "entrada":
            print(f"{self.nome} - +R${valorFormatado} - {self.data} - {self.categoria}")
        elif self.tipo.lower() == "saida":
            print(f"{self.nome} - -R${valorFormatado} - {self.data} - {self.categoria}")
        else:
            print(f"{self.nome} - R${valorFormatado} - {self.data} - {self.categoria}")

    def conversao(self):
        return{
            "nome" : self.nome,
            "valor" : self.valor,
            "tipo" : self.tipo,
            "data" : self.data,
            "categoria" : self.categoria
        }

def cabecalho():
    print("="*22)
    print(" CONTROLE FINANCEIRO ")
    print("="*22)
    
def menu():
    print(
        "\n1 - Adicionar movimentação"
        "\n2 - Listar movimentações"
        "\n3 - Mostrar saldo"
        "\n4 - Filtrar por categoria"
        "\n5 - Filtrar por data"
        "\n6 - Editar movimentação"
        "\n7 - Remover movimentação"
        "\n8 - Sair\n"
    )

def validacaoTipo(texto):
    valorTipo = input("Qual o tipo da movimentação: ") 
    while valorTipo not in ("entrada", "saida"):
            print("Opção não é válida!") 
            valorTipo = input("Digite entrada/saida para a movimentação: " )
    return valorTipo

def adicionar():
    nome = entrada("Nome da movimentação: ")
    valor = float(entrada("Valor da movimentação: "))
    tipo = validacaoTipo("Tipo (entrada/saida): ")
    data = escolherData()
    categoria = entrada("Digite a categoria: ")
    u = Objetos(nome, valor, tipo, data, categoria)
    lista.append(u)
    print("Movimentação cadastrada com sucesso!")
    salvarJson()

def listar():
    print("\n Movimentações cadastradas: \n")
    for u in lista:
        u.mostrarResultados()
        
def mostrar_saldo():
    saldo_total = 0
    for u in lista:
        if u.tipo.lower() == "entrada":
            saldo_total += u.valor
        elif u.tipo.lower() == "saida":
            saldo_total -= u.valor
    print(f"\nSaldo atual: R${saldo_total}")

def entrada(texto):
    valor = input(texto)
    while not valor:
        print ("Digite uma opção válida! ")
        valor = input(texto)
    return valor

def filtrarCategoria():
    encontrar = False
    categoria = input("Qual categoria deseja acessar:")
    for u in lista:
        if categoria.lower() == u.categoria.lower():
            u.mostrarResultado()
            encontrar = True
            
    if encontrar == False:
        print("Categoria não encontrada!")

import datetime
import json

def escolherData():
    data = datetime.datetime.now()
    dataFormatada = data.strftime("%d/%m/%Y")
    return dataFormatada
            
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
    for u in lista:
        if edicao.lower() == u.nome.lower():
            novoNome = input("Qual o novo nome: ")
            novoValor = float(input("Qual o novo valor: "))
            novoTipo = input("Qual  o novo tipo: ")
            novaData = input("Qual a nova data: ")
            novaCategoria = input("Qual a nova categoria: ")
            u.nome = novoNome
            u.valor = novoValor
            u.tipo = novoTipo
            u.data = novaData
            u.categoria = novaCategoria
            encontrar = True
            print("Editada com sucesso!")
            salvarJson()
    if encontrar == False:
        print("Movimentação não encontrada!")

def remover ():
    encontrar = False
    removendo = input("Qual movimentação deseja remover: ")
    for u in lista: 
        if removendo.lower() == u.nome.lower():
            lista.remove(u)
            print("Movimentação removida com sucesso!")
            salvarJson()
            encontrar = True
            break
    if encontrar == False:
        print("Movimentação não encontrada")

def salvarJson():
    listaJson = []
    for u in lista:
        listaJson.append(u.conversao())
    with open ("dados.json","w") as arquivo:
        json.dump(
            listaJson,
            arquivo,
            inednt = 4)

def carrefarJson():
    try:
        with open ("dados.json", "r") as arquivo:
            dados = json.dados:
            for item in dados:
                u = Objetos(
                    item ["nome"],
                    item ["valor"],
                    item ["tipo"],
                    item ["data"],
                    item ["categoria"]
                )
                lista.append(u)
    except FileNotFoundError:
        pass
        
 def mostrarRelatório():
    entradaTotal = 0
    saidaTotal = 0
    maiorEntrada = None
    maiorSaida = None
    gastosCategoria = {}
    EntradasCategoria = {}
     
    for u in lista:
        if u.tipo.lower() == "entrada":
            entradaTotal += u.valor
            if maiorEntrada == None:
                maiorEntrada = u    
            elif u.valor > maiorEntrada.valor:
                maiorEntrada = u
            if u.categoria not in entradasCategoria:
                entradasCategoria[u.categoria] = u.valor
            else: entradasCategoria[u.categoria] += u.valor
        elif u.tipo.lower() == "saida":
            saidaTotal += u.valor
            if maiorSaida is None:
                maiorSaida = u
            elif u.valor > maiorSaida.valor:
                maiorSaida = u
            if u.categoria not in gastosCategoria:
                gastosCategoria[u.categoria] = u.valor
            else:gastosCategoria[u.categoria] += u.valor
                
    saldoFinal = entradaTotal  - saidaTotal
    entradaFormatada = f"{entradaTotal:.2f}".replace(".", ",")
    saidaFormatada = f"{saidaTotal:.2f}".replace(".", ",")
    saldoFormatado = f"{saldoFinal:.2f}".replace(".", ",")
    if maiorEntrada is not None:
        maiorEntradaFormatada = f"{maiorEntrada.valor:.2f}".replace(".",",")
        maiorEntradaValidacao = f"{maiorEntrada.nome} - R${maiorEntradaFormatada}"
    else: maiorEntradaValidacao = "nenhuma entrada cadastrada"
    if maiorSaida is not None:
        maiorSaidaFormatada = f"{maiorSaida.valor:.2f}".replace(".", ",")
        maiorSaidaValidacao = f"{maiorSaida.nome} - R${maiorSaidaFormatada}"
    else: maiorSaidaValidacao = "nenhuma saída cadastrada"

    print("=" * 15)
    print(" RELATÓRIO ")
    print("=" * 15)
    print (f"Entradas: R${entradaFormatada} \n"
           f"Saídas:  R${saidaFormatada} \n" 
           f"Saldo final: R${saldoFormatado}\n"
           f"Maior entrada:{maiorEntradaValidacao}\n"
           f"Maior saída: {maiorSaidaValidacao}\n")
    print("=" *20)
    print("Gastos por Categoria")
    print("="*20)
    for categoria in gastosCategoria:
        valorFormatadoSaidas = f"{gastosCategoria[categoria]:.2f}".replace(".",",")
        print(f"{categoria}: R${valorFormatadoSaidas}")
    print("=" *20)
    print("Ganhos por Categoria")
    print("="*20)
    for categoria in entradasCategoria:
        valorFormatadoEntradas = f"{entradasCategoria[categoria]:.2f}".replace(".",",")
        print(f"{categoria}: R${valorFormatadoEntradas}")
                
lista = []
carregarJSon()


while True:

    cabecalho()

    menu()
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
      adicionar()
        
    elif opcao == "2":
        listar()
        
    elif opcao == "3":
        mostrar_saldo()
    
    elif opcao == "4":
        filtrarCategoria()

    elif opcao == "5":
        filtrarData()

    elif opcao == "6":
        editar()
       

    elif opcao == "7":
        remover()

    elif opcao == "8":
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida!")
