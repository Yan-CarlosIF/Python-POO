# Dada uma lista de palavras, crie um dicionário onde a chave
# é o número de letras e o valor é uma lista com todas as palavras desse tamanho, em minúsculas.
palavras = ["Python", "é", "fantástico", "e", "poderoso", "para", "desenvolvedores"]
lower_words = [word.lower() for word in palavras]

# Resultado esperado: {6: ['python'], 1: ['é'], 10: ['fantástico'], 8: ['poderoso'], ...}

words_and_length = {
    size: [word for word in lower_words if len(word) == size]
    for size in set(len(word) for word in lower_words)
}

print(words_and_length)

# Dadas duas listas, crie um dicionário em que a chave é o elemento da primeira
# e o valor o da segunda, somente se ambos forem strings que começam com a mesma letra (case insensitive).
chaves = ["Nome", "Email", "Telefone", "Idade"]
valores = ["nina", "equipe@gmail.com", "tim", "Instagram"]

# Resultado esperado: {'Nome': 'nina', 'Email': 'equipe@gmail.com'}

key_value = {chaves[index]: valores[index] for index in range(4)}

# key_value = { # Estudar isso depois
#     k: v
#     for k, v in zip(chaves, valores)
#     if isinstance(k, str) and isinstance(v, str)
#     and k[0].lower() == v[0].lower()
# }

print(key_value)

# Dado um dicionário com categorias e listas de valores,
# crie um novo dicionário com a soma apenas dos números pares de cada categoria.
dados = {
    "categoria1": [1, 2, 3, 4],
    "categoria2": [10, 11, 12],
    "categoria3": [7, 9, 13],
}

# Resultado esperado: {'categoria1': 6, 'categoria2': 22, 'categoria3': 0}
even_some_data = {
    key: sum([number for number in value if number % 2 == 0])
    for key, value in dados.items()
}

print(even_some_data)
