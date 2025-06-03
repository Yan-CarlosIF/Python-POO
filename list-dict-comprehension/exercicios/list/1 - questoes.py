# Crie uma lista com os quadrados dos números de 1 a 10 usando list comprehension.
numbers_square = [(number + 1) ** 2 for number in range(10)]
print(numbers_square)

# Crie uma lista com apenas os números pares entre 0 e 20.
even_numbers = [number for number in range(21) if number % 2 == 0]
print(even_numbers)

# A partir de uma lista de palavras, crie uma nova lista contendo apenas as palavras que têm mais de 4 letras.
palavras = ["casa", "computador", "sol", "livro", "água", "inteligência"]
words_greater_then_4 = [word for word in palavras if len(word) > 4]
print(words_greater_then_4)

# Crie uma lista com as letras minúsculas da string abaixo, excluindo vogais.
frase = "List Comprehension é poderosa!"
lower_phrase = [
    letter.lower()
    for letter in frase
    if letter not in "aeiouáéíóú" and letter.isalpha() or letter == " "
]

print(lower_phrase)
