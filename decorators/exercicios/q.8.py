#  Questão 8 – Autenticação com Decorator em Classe
# Crie um sistema de autenticação com uma classe Usuario.
# Faça um @decorator chamado verifica_login que bloqueia métodos protegidos caso o usuário não esteja autenticado.
# O método login() deve mudar o estado interno de autenticação.

# Extra: O logout() deve impedir novos acessos até novo login.


def verify_login(function):
    def wrapper(self, *args, **kwargs):
        if self._User__token:
            return function(self, *args, **kwargs)

        print("User not Authenticated")

    return wrapper


class User:
    def __init__(self, name, password, email):
        self.name = name
        self.__password = password
        self.email = email
        self.__token = None

    def login(self):
        email = input("Insira o seu email: ")
        password = input("Insira sua senha: ")

        if self.email == email and self.__password == password:
            self.__token = email + password
            print("Login sucess")
            return

        print("Invalid Crendentials")

    @verify_login
    def exibir_dados(self):
        print("\n== USER DATA ==")
        print(f"👤 Nome: {self.name}")
        print(f"📧 Email: {self.email}")
        print(f"🔐 Authenticated: {bool(self.__token)}")

    def logout(self):
        if not self.__token:
            print("User not logged in")
        else:
            self.__token = None
            print("Logged out successfully")


yan = User("Yan Carlos", "chama123", "yan312005@gmail.com")

yan.login()

yan.exibir_dados()

yan.logout()
