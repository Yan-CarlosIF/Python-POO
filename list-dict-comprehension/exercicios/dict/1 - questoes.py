# Crie um dicionário onde as chaves são números de 1 a 5 e os valores são seus quadrados.
numbers_and_squares = {(number + 1): (number + 1) ** 2 for number in range(5)}
print(numbers_and_squares)

# Dada a lista de nomes abaixo, crie um dicionário onde as chaves são os nomes e os valores são o número de letras de cada nome.
nomes = ["Ana", "Beatriz", "Carlos", "Davi"]

names_and_length = {name: len(name) for name in nomes}
print(names_and_length)

# Dado um dicionário de produtos e seus preços, crie um novo dicionário apenas com os produtos que custam mais de R$ 50.
produtos = {"camiseta": 30, "calça": 80, "tênis": 150, "boné": 25, "moletom": 90}

products_50 = {product: price for product, price in produtos.items() if price > 50}

print(products_50)

# Dado o dicionário abaixo, crie outro invertendo as chaves e os valores.
alunos = {"João": 1, "Maria": 2, "Pedro": 3}

inverted_students = {size: name for name, size in alunos.items()}

print(inverted_students)
