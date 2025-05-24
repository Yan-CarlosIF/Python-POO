# Questão 9 – Banco com Propriedades e Validação
# Crie uma classe ContaBancaria com uma propriedade saldo. Ao usar o setter do saldo, garanta que ele nunca possa ser negativo.

# Extra: Crie um método sacar(valor) que usa o setter para modificar o saldo, respeitando a regra de não permitir valores negativos.


class ContaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo):
        if saldo >= 0:
            self.__saldo = saldo

    def sacar(self, saque):
        self.saldo -= saque


contaYan = ContaBancaria(1000)

print(contaYan.saldo)

contaYan.saldo = -1

print(contaYan.saldo)

contaYan.sacar(500)

print(contaYan.saldo)

contaYan.sacar(501)

print(contaYan.saldo)
