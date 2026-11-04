# Q1 - Livro
class Livro:
    def __init__(self, titulo, autor, paginas, paginas_lidas=0):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.paginas_lidas = paginas_lidas

    def ler(self, quantidade):
        self.paginas_lidas = min(self.paginas_lidas + quantidade, self.paginas)
        print(f"Foram lidas {quantidade} páginas")

    def progresso(self):
        porcentagem = (self.paginas_lidas / self.paginas) * 100
        print(f"Você já leu {porcentagem:.1f}% do livro")


livro = Livro("Dom Casmurro", "Machado de Assis", 200, 0)
livro.ler(50)
livro.progresso()
 
print("")

livro1 = Livro("Dom Casmurro", "Machado de Assis", 100)
livro1.ler(80)   
livro1.ler(500)  
livro1.progresso()  