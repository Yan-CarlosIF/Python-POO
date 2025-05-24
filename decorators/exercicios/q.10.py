# Questão 10 – Cadastro de Produtos com Classe Abstrata e Método Factory
# Crie uma classe abstrata Produto com um método exibir_info().

# Crie duas subclasses: ProdutoAlimenticio e ProdutoEletronico. Cada uma deve implementar exibir_info() de forma personalizada.

# Crie um método de classe chamado criar_produto() que receba um dicionário e crie o tipo correto de produto dinamicamente (fábrica).

from abc import ABC, abstractmethod


class Produto(ABC):
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    @classmethod
    def criar_produto(cls, dados: dict):
        tipo = dados.get("tipo")

        if tipo == "alimenticio":
            return ProdutoAlimenticio(dados.get("nome"), dados.get("preco"))
        elif tipo == "eletronico":
            return ProdutoEletronico(dados.get("nome"), dados.get("preco"))
        else:
            raise ValueError("Tipo de produto desconhecido.")

    @abstractmethod
    def exibir_info(self):
        pass


class ProdutoAlimenticio(Produto):
    def __init__(self, nome, preco):
        super().__init__(nome, preco)

    def exibir_info(self):
        print(f"Produto alimenticio {self.nome} com preco {self.preco}")


class ProdutoEletronico(Produto):
    def __init__(self, nome, preco):
        super().__init__(nome, preco)

    def exibir_info(self):
        print(f"Produto eletronico {self.nome} com preco {self.preco}")


prod1 = Produto.criar_produto({"nome": "Hamburger", "preco": 25, "tipo": "alimenticio"})
prod2 = Produto.criar_produto({"nome": "Teclado", "preco": 250, "tipo": "eletronico"})

prod1.exibir_info()
prod2.exibir_info()
