# Questão 7 – Sistema de Veículos com Abstração
# Crie uma classe abstrata Veiculo com um método abstrato mover(). Depois, crie as subclasses
# Carro, Bicicleta e Aviao. Cada classe deve implementar o método mover() com uma mensagem personalizada.

# Extra: Adicione um método tipo_combustivel() obrigatório nas subclasses.

from abc import ABC, abstractmethod


class Veiculo(ABC):
    @abstractmethod
    def mover(self):
        pass

    def tipo_combustivel(self):
        pass


class Carro(Veiculo):
    def __init__(self, tipo):
        self.__tipo_combustivel = tipo

    def mover(self):
        print("O carro se move rápido pela terra")

    @property
    def tipo_combustivel(self):
        return self.__tipo_combustivel


class Aviao(Veiculo):
    def __init__(self, tipo):
        self.__tipo_combustivel = tipo

    def mover(self):
        print("O Aviao se move rápido pelo céu")

    @property
    def tipo_combustivel(self):
        return self.__tipo_combustivel


class Bicicleta(Veiculo):
    def __init__(self, tipo):
        self.__tipo_combustivel = tipo

    def mover(self):
        print("O Bicicleta se move lento pela terra")

    @property
    def tipo_combustivel(self):
        return self.__tipo_combustivel


veiculos = [Carro("Etanol"), Aviao("Gasolina"), Bicicleta("Força de vontade")]

for v in veiculos:
    print(f"\nClasse: {v.__class__.__name__}")
    v.mover()
    print(v.tipo_combustivel)
