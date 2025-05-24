from abc import ABC, abstractmethod

# ABC = Abstract Base Class
class Animal(ABC):  # classe abstrata
    @abstractmethod
    def fazer_som(self):  # método abstrato
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return "Au au!"

class Gato(Animal):
    def fazer_som(self):
        return "Miau"

# animal = Animal()        # ❌ ERRO: não pode instanciar classe abstrata
c = Cachorro()             # ✅ funciona
print(c.fazer_som())       # Saída: "Au au!"
