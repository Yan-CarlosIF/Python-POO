# 3. @property — Acessar métodos como se fossem atributos
# Permite criar métodos que se comportam como atributos. Muito útil para encapsulamento com leitura controlada (getter).

class Produto:
    def __init__(self, preco):
        self._preco = preco

    @property
    def preco_com_desconto(self):
        return self._preco * 0.9

p = Produto(100)
print(p.preco_com_desconto)  # 90.0 (obs: não precisa chamar o método com (), irá se comportar como se fosse um atributo)