# Projeto de Prática – Biblioteca de Livros (Python Classes)

## **Passo 1 – Criar a classe Livro**
**Objetivo:** Criar uma classe básica com atributos e um método de exibição.

1. Crie a classe `Livro`.
2. Adicione atributos de instância:  
   - `titulo`  
   - `autor`  
   - `paginas`
3. Crie o método `__str__` para retornar algo como:  
   `"O Senhor dos Anéis por J.R.R. Tolkien - 1200 páginas"`.
4. Instancie alguns livros e imprima para testar.

---

## **Passo 2 – Adicionar atributos e métodos extras**
**Objetivo:** Praticar métodos, `property` e controle de atributos.

1. Adicione atributo `avaliacoes` (lista de notas, de 0 a 5).
2. Crie uma `@property` chamada `media_avaliacao` que calcula a média das notas.
3. Adicione método `adicionar_avaliacao(nota)` que insere uma nota na lista.
4. Teste adicionando avaliações e imprimindo a média.

---

## **Passo 3 – Criar a classe Biblioteca**
**Objetivo:** Praticar atributos de classe e gerenciamento de objetos.

1. Crie a classe `Biblioteca`.
2. Adicione um **atributo de classe** `livros = []`.
3. Crie método `adicionar_livro(livro)` que adiciona um objeto `Livro` à lista.
4. Crie método `listar_livros()` que imprime todos os livros cadastrados.

---

## **Passo 4 – Usar método estático**
**Objetivo:** Praticar métodos que não dependem de instâncias.

1. Dentro de `Livro`, crie um método estático `validar_nota(nota)` que retorna `True` se a nota for entre 0 e 5.
2. Use esse método dentro de `adicionar_avaliacao` para validar a nota antes de adicionar.

---

## **Passo 5 – Mini-desafios extras**
**Objetivo:** Consolidar aprendizado e explorar casos reais.

1. Adicione um atributo `disponivel` (True/False).
2. Crie método `emprestar()` que muda `disponivel` para `False`.
3. Crie método `devolver()` que muda `disponivel` para `True`.
4. Crie uma **propriedade** `estado` que retorna:
   - `"Disponível"` se `disponivel` for True.
   - `"Emprestado"` se `disponivel` for False.
5. Teste simulando empréstimos e devoluções.

---
