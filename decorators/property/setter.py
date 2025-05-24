# @<propriedade>.setter — Definir valor da propriedade (setter)
# Permite criar uma função que define (altera) o valor de uma propriedade.

class Produto:
    def __init__(self, preco):
        self._preco = preco

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, novo_preco):
        if novo_preco > 0:
            self._preco = novo_preco

p = Produto(100)
p.preco = 150  # usa o setter
print(p.preco)  # 150