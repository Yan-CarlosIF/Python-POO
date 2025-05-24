# Exercício 4: Propriedade com @property e @setter
# Objetivo: Criar uma propriedade chamada email que pode ser lida e atualizada, mas formatada automaticamente.


class Usuario:
    def __init__(self, nome_email):
        self.email = nome_email

    @staticmethod
    def __format_email(email):
        return email.split("@")[0] if "@" in email else email

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, novo_email):
        self.__email = f"{self.__format_email(novo_email)}@empresa.com"


# Testando

yan = Usuario("yan312005@gmail.com")

print(yan.email)

yan.email = "yan@gmail.com"

print(yan.email)
