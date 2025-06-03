# A partir da frase abaixo, crie uma lista contendo as palavras invertidas, sem vogais, com 4 letras ou mais.
frase = "Python é impressionantemente poderoso e elegante"  # Exemplo de saída: ['nhtyP', 'tnmrssnp', 'rdvs', 'tngl']
vowels = "aeiouáéíóúâêôãõAEIOUÁÉÍÓÚÂÊÔÃÕ"
words = frase.split(" ")

inverted_words = [
    "".join(
        [letter for letter in word[::-1] if letter.isalpha() and letter not in vowels]
    )
    for word in words
    if len(word) > 1
]
print(inverted_words)

# Dada uma matriz 3x3, crie a matriz transposta usando list comprehension aninhada.
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Resultado esperado:
# [[1, 4, 7],
#  [2, 5, 8],
#  [3, 6, 9]]

matriz_transposta = [  # Loucura do Yan
    [matriz[0][index], matriz[1][index], matriz[2][index]]
    for index, _ in enumerate(matriz)
]

matriz_transposta2 = [[vector[i] for vector in matriz] for i in range(len(matriz))]

print(matriz_transposta)

# Dada uma lista de palavras, crie um dicionário onde a chave é o número de letras e o valor é uma
# lista com todas as palavras desse tamanho, em minúsculas.
palavras = ["Python", "é", "fantástico", "e", "poderoso", "para", "desenvolvedores"]
