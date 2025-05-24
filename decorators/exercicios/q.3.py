# Exercício 3: Método de classe
# Objetivo: Criar um contador de instâncias com @classmethod.


class ClasseDoida:
    cont = 0

    def __init__(self):
        ClasseDoida.cont += 1

    @classmethod
    def quantidade_instancias(cls):  # cls = ClasseDoida = classe que chamou o método
        return cls.cont


class1 = ClasseDoida()
class2 = ClasseDoida()
class3 = ClasseDoida()

print(ClasseDoida.cont)
