import datetime

def cabecalho():
    print("="*22)
    print(" CONTROLE FINANCEIRO ")
    print("="*22)

def entrada(texto):
    valor = input(texto).strip()
    while not valor:
        print ("Digite uma opção válida! ")
        valor = input(texto).strip()
    return valor

def validacaoTipo(texto):
    valorTipo = input(texto).strip().lower()

    while valorTipo not in ("entrada", "saida"):
        print("Opção não é válida!")
        valorTipo = input(texto).strip().lower()

    return valorTipo

def entradaFloat(): 
    while True: 
        valorTexto: input (texto).strip().replace(",",".")
        try:
            valor = float(valorTexto)
            if valor <= 0:
                print("Digite um valor maior que zero!")
                continue
            return valor
        except ValueError: 
            print("Valor inválido! Digite apenas números(ex: 50.90 ou 54.65)")
            
    

def escolherData():
    data = datetime.datetime.now()
    dataFormatada = data.strftime("%d/%m/%Y")
    return dataFormatada

def formatarMoeda(valor):
    return f"{valor:.2f}".replace(".", ",")
