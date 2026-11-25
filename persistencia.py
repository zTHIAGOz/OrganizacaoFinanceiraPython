"""
import datetime
import json
from utils import formatarMoeda
from models import Objetos


def salvarJson(lista):
    listaJson = []
    for movimentacao in lista:
        listaJson.append(movimentacao.conversao())
    with open (nomeArquivo(), "w", encoding="utf-8") as arquivo : #abri dados.json em modo escrita e chamar ele de arquivo (o w é de write)
        json.dump( #escreva a listajson dentro do arquivo (codigo abaixo)
            listaJson,
            arquivo,
            indent=4
            )

def carregarJson(lista):
    try:
        with open (nomeArquivo(), "r", encoding="utf-8") as arquivo: #abrir dadosjson(é o arquivo) em modo leitura e chamar ele de arquivo (o r é de read)
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
        with open (arquivoConsulta, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            for item in dados:
                valorFormatado = formatarMoeda(item["valor"])
                print (f"{item['nome']} - R${valorFormatado} - {item['data']} - {item['categoria']}")

    except FileNotFoundError:
            print("Nenhum registro encontrado!")

def exportarCSV(lista):
        with open ("relatorio.csv", "w", encoding="utf-8") as arquivo:
            arquivo.write("Nome, Valor, Tipo, Data, Categoria\n")
            for movimentacao in lista:
                arquivo.write(f"{movimentacao.nome},"
                              f"{movimentacao.valor},"
                              f"{movimentacao.tipo},"
                              f"{movimentacao.data},"
                              f"{movimentacao.categoria}\n")
    
"""
import sqlite3
from models import Objetos
from utils import formatarMoeda

def criarTabela():
    conexao = sqlite3.connect("financeiro.db")
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS movimentacoes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome  TEXT NOT NULL,
            valor REAL NOT NULL,
            tipo TEXT NOT NULL,
            data TEXT NOT NULL,
            categoria TEXT NOT NULL)
    """)

    conexao.commit()
    conexao.close()

def inserirMovimentacao (movimentacao):
    conexao = sqlite3.connect("financeiro.db")
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO movimentacoes(nome, valor, tipo, data, categoria)
        VALUES(?,?,?,?,?)
        """, (
            movimentacao.nome,
            movimentacao.valor,
            movimentacao.tipo,
            movimentacao.data,
            movimentacao.categoria
        ))
    conexao.commit()
    conexao.close()


def listarMovimentacoes():
    conexao = sqlite3.connect("financeiro.db")
    cursor =  conexao.cursor()

    cursor.execute("""
    SELECT id, nome, valor, tipo, data, categoria
    FROM movimentacoes
    """)

    Linhas = cursor.fetchall()
    conexao.close()

    Lista = []
    for linha in Linhas:
        movimentacao = Objetos(
            nome = linha [1],
            valor = linha [2],
            tipo = linha [3],
            data = linha [4],
            categoria = linha [5],
            id = linha[0]
        )
        Lista.append(movimentacao)
    return Lista

def atualizarMovimentacao(movimentacao):
    conexao = sqlite3.connect("financeiro.db")
    cursor  = conexao.cursor()

    cursor.execute("""
    UPDATE movimentacoes
    SET nome = ?, valor = ?, tipo = ?, data = ?, categoria = ?
    WHERE id = ?
     """, (
         movimentacao.nome,
         movimentacao.valor,
         movimentacao.tipo,
         movimentacao.data,
         movimentacao.categoria,
         movimentacao.id,
     ) )
    conexao.commit()
    conexao.close()

def deletarMovimentacao(idMovimentacao):
    conexao = sqlite3.connect("finenceiro.db")
    cursor = conexao.cursor()

    cursor.execute("""
    DELETE FROM movimentacoes
    WHERE id = ?
    """, (idMovimentacao,))

    conexao.commit()
    conexao.close()

def consultaMensal(): 
    mesAno = input("Digite o mês e ano de consulta (ex: '11/2026':)").strip()
    conexao = sqlite3.connect("financeiro.db")
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, nome, valor, tipo, data, categoria
        FROM movimentacoes
        WHERE data LIKE ?
        """, (f"%/{mesAno}",))

    linhas = cursor.fetchall()
    conexao.close()

    if not linhas:
        print ("Nenhum registro encontrado para esse mês!")
        return

    for linha in linhas:
        valorFormatado = formatarMoeda(linha[2])
        print(f"[ID: {linha[0]}] {linha[1]} - R${valorFormatado} - {linha[4]} - {linha[5]}")

def exportarCSV(lista):
        with open("relatorio.csv", "w", encoding="utf-8") as arquivo:
            arquivo.write("ID, Nome, Valor, Tipo, Data, Categoria\n")
            for movimentacao in lista:
                arquivo.write(
                    f"{movimentacao.id},"
                    f"{movimentacao.nome},"
                    f"{movimentacao.valor},"
                    f"{movimentacao.tipo},"
                    f"{movimentacao.data},"
                    f"{movimentacao.categoria},\n"
                )
        print("Arquivo relatorio.csv exportado com sucesso!")
            