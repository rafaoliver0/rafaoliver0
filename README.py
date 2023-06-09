class Livro:
  def __init__(self, titulo, autor, disponivel=True):
   self.titulo = titulo
   self.autor = autor
   self.disponivel = disponivel

class Biblioteca:
  def __init__(self):
       self.livros = []

def adicionar_livro(self, livro):
    	self.livros.append(livro)

def emprestar_livro(self, titulo):
    for livro in self.livros:
      if livro.titulo == titulo:
        if livro.disponivel:
         livro.disponivel = False
        print(f"O livro '{livro.titulo}' foi emprestado com sucesso.")
    else:
        print(f"O livro '{livro.titulo}' não está disponível no momento.")
    return
print("Livro não encontrado.")

def devolver_livro(self, titulo):
    	for livro in self.livros:
         if livro.titulo == titulo:
            if not livro.disponivel:
             livro.disponivel = True
            print(f"O livro '{livro.titulo}' foi devolvido com sucesso.")
        else:
            print("Este livro já está disponível na biblioteca.")
        return
print("Livro não encontrado.")

def exibir_livros(self):
    	if len(self.livros) == 0:
         print("A biblioteca está vazia.")
        else:
           for livro in self.livros:
            status = "Disponível" if livro.disponivel else "Indisponível"
            print(f"Título: {livro.titulo}, Autor: {livro.autor}, Status: {status}")


# Exemplo de uso
biblioteca = Biblioteca()

livro1 = Livro("A Guerra dos Tronos", "George R.R. Martin")
livro2 = Livro("1984", "George Orwell")
livro3 = Livro("O Hobbit", "J.R.R. Tolkien")

biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)

biblioteca.emprestar_livro("A Guerra dos Tronos")
biblioteca.emprestar_livro("1984")

biblioteca.exibir_livros()

biblioteca.devolver_livro("A Guerra dos Tronos")
biblioteca.exibir_livros()
