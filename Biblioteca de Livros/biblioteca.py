from avaliacoes import Avaliacoes

class Livro:
    livros = []
    
    def __init__(self, titulo, autor, paginas):
        self._titulo = titulo
        self._autor = autor
        self._paginas = paginas
        self._disponivel = True
        self._avaliacao = []
        Livro.livros.append(self)
    
    @property
    def disponivel(self):
        return 'Disponível' if self._disponivel else 'Emprestado'
    
    def __str__(self):
        return f'{self._titulo} | {self._autor} | {self._paginas} | {self.media_avaliacao}'
    
    @staticmethod
    def validar_nota(nota):
        return 0 < nota <= 5

    def adicionar_avaliacao(self, cliente, nota):
        if Livro.validar_nota(nota):
            avaliacao = Avaliacoes(cliente, nota)
            self._avaliacao.append(avaliacao)
                       
    def emprestar(self):
        self._disponivel = False
      
    def devolver(self):
        self._disponivel = True
            
    @classmethod     
    def visualizar_livro(cls):
        string = f'{'LIVRO'.ljust(20)} | {'AUTOR'.ljust(20)} | {'PAGINAS'.ljust(20)} | {'AVALIACAO'.ljust(20)} | {'DISPONIVEL'}'
        print(string)
        linha = '-' * (len(string) + 10)
        print(linha)
        
        for livro in cls.livros:
            print(f'{livro._titulo.ljust(20)} | {livro._autor.ljust(20)} | {str(livro._paginas).ljust(20)} | {str(livro.media_avaliacao).ljust(20)} | {livro.disponivel.ljust(20)}')
              
    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return "Sem avaliações"
        soma_notas = sum(soma._nota for soma in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media = round(soma_notas / quantidade_notas, 1)
        return media
            