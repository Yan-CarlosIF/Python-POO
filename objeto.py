class Pessoa:
    # Inicializador que recebe o valor do objeto vindo de fora da classe
    def __init__(self, nome, sobrenome):
        # Objeto ↓     Atributo ↓
        self.nome = nome
        self.sobrenome = sobrenome

    def unir_nomes(self):
        # O parâmetro 'self' que permite o acesso dos atributos em outra função apenas dentro da classe.
        self.nome_completo = self.nome + self.sobrenome  # cria um novo atributo
        print(f"O nome completo é: {self.nome_completo}.")


# Criar uma instância da classe Pessoa
nome = "Guilherme"
sobrenome = " Carvalho"
pessoa = Pessoa(nome, sobrenome)

# Chamar o método unir_nomes() para a instância criada
pessoa.unir_nomes()
