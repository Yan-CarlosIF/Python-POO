# @classmethod — Método de Classe
# Um método de classe recebe a classe como primeiro argumento (cls), em vez da instância (self).

# Muito útil para fábricas (factory methods) ou para acessar/alterar atributos da classe inteira.

class Pessoa:
    contador = 0

    def __init__(self, nome):
        self.nome = nome
        Pessoa.contador += 1

    @classmethod # Acessar os atributos da classe
    def total_pessoas(cls):
        return cls.contador

p1 = Pessoa("Ana")
p2 = Pessoa("João")

print(Pessoa.total_pessoas())  # 2
