class Pessoa:
    def __init__(self, v_construtor):  # Atributo ↓
        self.nome = "Steve"
        self.sobrenome = "Jobs"
        self.lista_nomes = ["João", "Maria"]
        self.dicionario = {"nome": "Steve", "sobrenome": "Jobs"}
        self.aluno = v_construtor  # Atributo criado a partir do parâmetro do construtor

    # Os atributos podem receber vários tipos de valores com origem de dentro e/ou fora da classe

    def unir_nomes(self):
        self.nome_completo = self.nome + self.sobrenome
        print(f"O nome completo é {self.nome_completo}")
        print(f"O nome completo é {self.lista_nomes[:]}")  # [:] cria uma cópia da lista
        print(f"O nome completo é {self.dicionario}")
        print(f"O nome do aluno é {self.aluno}")


# Valor passado para o construtor
v_construtor = "Joãozinho"

# Criação de uma instância de Pessoa
pessoa = Pessoa(v_construtor)
# Chamada ao método que faz as impressões
pessoa.unir_nomes()
