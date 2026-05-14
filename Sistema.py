class Objetos:

    def __init__(self, nome, valor, tipo, data, categoria):

        self.nome = nome
        self.valor = valor
        self.tipo = tipo
        self.data = data
        self.categoria = categoria

    def mostrar_resultado(self):    

        
        if self.tipo.lower() == "entrada":

            print(f"{self.nome} - +R${self.valor} - {self.data} - {self.categoria}")

        elif self.tipo.lower() == "saida":

            print(f"{self.nome} - -R${self.valor} - {self.data} - {self.categoria}")

        else:

            print(f"{self.nome} - R${self.valor} - {self.data} - {self.categoria}")



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
    if encontrar == False:
        print("Movimentação não encontrada!")

def remover ():
    encontrar = False
    removendo = input("Qual movimentação deseja remover: ")
    for u in lista: 
        if removendo.lower() == u.nome.lower():
            lista.remove(u)
            print("Movimentação removida com sucesso!")
            encontrar = True
            break
    if encontrar == False:
        print("Movimentação não encontrada")



lista = []



while True:

    menu()

    opcao = input("Escolha uma opção: ")

    
    if opcao == "1":

        nome = entrada("Nome da movimentação: ")
        
        valor = float(entrada("Valor da movimentação: "))
        
        tipo = validacaoTipo("Tipo (entrada/saida): ")

        data = entrada("Qual a data da movimentação: ")

        categoria = entrada ("Digite a categoria: ")
        
        u = Objetos(nome, valor, tipo, data, categoria)

        lista.append(u)

        print("Movimentação cadastrada com sucesso!")

    
    elif opcao == "2":

        print("\nMovimentações cadastradas:\n")

        for u in lista:

            u.mostrar_resultado()

    
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
