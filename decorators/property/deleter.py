#  @<propriedade>.deleter — Apagar uma propriedade (deleter)
# Permite criar uma função que é chamada quando você usa del obj.propriedade.

class Produto:
    def __init__(self, preco):
        self.__preco = preco

    @property
    def preco(self):
        return self.__preco

    @preco.deleter
    def preco(self):
        del self.__preco

p = Produto(100)
del p.preco  # chama o deleter
print(p.preco)