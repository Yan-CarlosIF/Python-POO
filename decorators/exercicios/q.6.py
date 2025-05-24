# Exercício 6: Sistema de Pagamentos com Classe Abstrata
# Objetivo: Criar uma estrutura base para diferentes tipos de pagamento, obrigando subclasses a implementarem um método de pagamento.

# 💡 Enunciado:
# Crie uma classe abstrata chamada Pagamento que tenha um método abstrato chamado processar_pagamento().

# Depois, crie duas classes concretas:

# PagamentoCartao

# PagamentoPix

# Cada classe deve implementar processar_pagamento() de forma específica.

# No final, instancie e use as classes para demonstrar o funcionamento.

from abc import ABC, abstractmethod


class Pagamento(ABC):
    @abstractmethod
    def processar_pagamento(self, valor):
        pass


class PagamentoCartao(Pagamento):
    def processar_pagamento(self, valor, parcelas=1):
        if parcelas < 1 or parcelas > 12:
            print("Numeros de parcelas inválido")
            return

        print(f"R${valor:.2f} Pago no cartão de crédito em {parcelas}x")


class PagamentoPix(Pagamento):
    def processar_pagamento(self, valor, chave):
        print(f"Transferencia de R${valor:.2f} para a chave {chave}")


cartao = PagamentoCartao()
cartao.processar_pagamento(120, 3)

pix = PagamentoPix()
pix.processar_pagamento(50, "chavepix@email.com")
