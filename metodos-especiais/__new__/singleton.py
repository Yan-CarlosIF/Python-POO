# Singleton - Criar uma classe que só possa ser instanciada uma vez

class BancoDados:
    _instancia = None  # atributo de classe

    def __new__(cls):
        if cls._instancia is None: # se nenhuma instância foi criada, cria uma nova
            print("Criando nova conexão...")
            cls._instancia = super().__new__(cls)
        else: # senão, reutiliza a instância
            print("Reutilizando conexão existente...")
        return cls._instancia

    def __init__(self):
        print("Inicializando...")

# Teste
a = BancoDados()
b = BancoDados()

print(a is b)  # True — aponta para o mesmo objeto
