# Método estático que opera sem referência a uma instância específica
class Matematica:
    # Opera sem instância, sem o parâmetro self
    # se não for estatico, ele passa o parâmetro self
    @staticmethod
    def somar(x, y):
        return x + y


class Matematica2:
    # se for chamado por uma instância, ele dará typeError por que não é estático
    def somar(x, y):
        return x + y


# Uso do método estático

m = Matematica2()

print(f"Resultado da soma: {Matematica.somar(10, 15)}")
print(f"Resultado da soma: {m.somar(10, 15)}")  # Erro, o primeiro parametro é o self
