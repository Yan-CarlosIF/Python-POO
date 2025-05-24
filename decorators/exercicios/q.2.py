# Exercício 2: Método estático
# Objetivo: Criar uma classe com um método estático que calcula a área de um retângulo.


class Geometria:
    @staticmethod
    def area_retangulo(base, altura):
        return base * altura


print(Geometria.area_retangulo(5, 3))
