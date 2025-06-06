class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __len__(self):
        return self.paginas


livro = Livro("O Senhor dos Aneis", "JRR Tolkien", 1000)
print(len(livro))
