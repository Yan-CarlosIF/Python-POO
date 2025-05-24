# Exercício 1: Criando um decorator simples
# Objetivo: Criar um decorator que exibe uma mensagem antes e depois da execução de uma função.


# *args e **kwargs são convenções usadas em Python para lidar com argumentos variáveis em funções

def log(func):
    def wrapper(*args, **kwargs):
        print("Before the function")
        # * é como se fosse o rest/spread do JS, desempacota os args em uma tupla,
        # ** desempacota em um dicionário
        func(*args, *kwargs) 
        print("After the function")

    return wrapper


@log
def sum_two_numbers(x, y):
    print(x + y)


sum_two_numbers(1, 2)
