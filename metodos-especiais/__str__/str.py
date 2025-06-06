class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f"{self.titulo} por {self.autor} ({self.paginas} paginas)"


livro = Livro("Harry Potter", "JK Rowling", 400)
print(livro)
