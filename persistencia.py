import datetime
import json
from utils import formatarMoeda
from models import Objetos


def salvarJson(lista):
    listaJson = []
    for movimentacao in lista:
        listaJson.append(movimentacao.conversao())
    with open (nomeArquivo(), "w") as arquivo : #abri dados.json em modo escrita e chamar ele de arquivo (o w é de write)
        json.dump( #escreva a listajson dentro do arquivo (codigo abaixo)
            listaJson,
            arquivo,
            indent=4
            )

def carregarJson(lista):
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

def exportarCSV(lista):
        with open ("relatorio.csv", "w") as arquivo:
            arquivo.write("Nome, Valor, Tipo, Data, Categoria\n")
            for movimentacao in lista:
                arquivo.write(f"{movimentacao.nome},"
                              f"{movimentacao.valor},"
                              f"{movimentacao.tipo},"
                              f"{movimentacao.data},"
                              f"{movimentacao.categoria}\n")
    