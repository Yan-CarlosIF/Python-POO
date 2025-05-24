# Exercicio 5: Decorator que verifica autenticação
# Objetivo: Criar um decorator que impede a execução de uma função caso o usuário não esteja autenticado.


def auth_login(function):
    def wrapper(self):
        user_name = input("Insira seu nome de usuario: ")
        user_password = input("Insira sua senha: ")
        return function(self, user_name, user_password)

    return wrapper


class Usuario:
    def __init__(self, name, password):
        self.user_name = name
        self.__password = password
        self.__token = None

    @auth_login
    def login(self, user_name, user_password):
        if self.user_name == user_name and self.__password == user_password:
            self.__token = user_name + user_password
            print("Login feito com sucesso")
        else:
            print("Credenciais inválidas")

    def logado(self):
        if self.__token:
            print("Autenticado!")
        else:
            print("Sem autorização")


yan = Usuario("yanzinn", "chama123")

yan.login()

yan.logado()
