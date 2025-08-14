from biblioteca import Livro

# Criando 3 instâncias de Livro
livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1200)
livro2 = Livro("Dom Casmurro", "Machado de Assis", 256)
livro3 = Livro("Clean Code", "Robert C. Martin", 464)

# Adicionando avaliações ao livro1
livro1.adicionar_avaliacao('Rondi', 8)
livro1.adicionar_avaliacao('Samara', 3)
livro1.adicionar_avaliacao('Heitor', 2)

livro1.emprestar()
livro1.devolver()   

# Testando o __str__
# print(livro1)
# print(livro2)
# print(livro3)

Livro.visualizar_livro()