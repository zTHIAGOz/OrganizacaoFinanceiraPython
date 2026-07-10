from utils import (formatarMoeda)

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