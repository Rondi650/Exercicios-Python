import os

def exercicio_nome():
      nome = 'Rondi'
      idade = 35

      print(f'meu nome e {nome} e tenho {idade} anos')
      
      
def exercio_quebra_de_linha():
      #modo 1
      print("""
            A
            L
            U
            R
            A
            """ )

      #modo 2
      letras = ["A", "L", "U", "R", "A"]
      print(*letras, sep="\n")

      #modo 3
      for letra in "ALURA":
            print(letra)


def exercicio_mostrar_pi():
      pi = 3.14159
      arredondado = round(pi, 2)
      print(f'O valor arredondado de pi é: {arredondado}')
      print(f'O valor arredondado de pi é: {pi:.2f}')


def exercicio_verificar_par_impar():
# 1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

      verificar_numero = int(input('Insira um numero: '))

      if (verificar_numero % 2 == 0):
            print('esse numero e par')
      else:
            print('esse numero e impar')


def exercicio_verificar_idade():
# 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias 
# de acordo com as seguintes condições:

# Criança: 0 a 12 anos;
# Adolescente: 13 a 18 anos;
# Adulto: acima de 18 anos.

      verificar_idade = int(input('Informe sua idade: '))
      
      if(verificar_idade >=0 and verificar_idade <=12):
            print('Criança')
      elif(verificar_idade >=13 and verificar_idade <=18):
            print('Adolescente')
      elif(verificar_idade > 18): 
            print('Adulto')
      else:
            print('Valor Invalido')
            
            
def exercico_validacao_dados():
# 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a 
# senha fornecidos correspondem aos valores esperados determinados por você.

      usuario_correto = 'Rondi'
      senha_correta = 35
      
      usuario = str(input('Qual seu usuario?'))
      senha = int(input('Qual sua senha?'))
      
      if(usuario == usuario_correto and senha == senha_correta):
            print('Usuario e senha corretos')
      elif(usuario == usuario_correto and senha != senha_correta):
            print('Usuario correto e senha incorreta')
      elif(usuario != usuario_correto and senha == senha_correta):
            print('Usuario incorreto e senha correta')
      else:
            print('Usuario e senha incorretos')
                     

def exercicio_plano_cartesiano():
# 4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else 
# para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

# Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
# Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
# Terceiro Quadrante: os valores de x e y devem ser menores que zero;
# Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
# Caso contrário: o ponto está localizado no eixo ou origem.

      x = int(input('Digite o valor de x: '))
      y = int(input('Digite o valor de y: '))
      
      if(x >0 and y>0):
            print('Primeiro Quadrante')
      elif(x<0 and y>0):
            print('Segundo Quadrante')
      elif(x<0 and y<0):
            print('Terceiro Quadrante')
      elif(x>0 and y <0):
            print('Quarto Quadrante')
      else:
            print('O ponto está localizado no eixo ou origem')      
            
            
def exemplos_GPT_for():
      # Somar números de uma lista
      numeros = [1, 2, 3, 4, 5]
      soma = 0
      for numero in numeros:
            soma += numero
      print(f"Soma: {soma}")

      # Contar caracteres específicos
      texto = "Python é incrível"
      contador = 0
      for caractere in texto:
            if caractere.lower() == 'i':
                  contador += 1
      print(f"Letra 'i' aparece {contador} vezes")

      # Criar uma nova lista com condições
      numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
      pares = []
      for numero in numeros:
            if numero % 2 == 0:
                  pares.append(numero)
      print(f"Números pares: {pares}")


def listas_simples():
# 1 - Crie uma lista para cada informação a seguir:
# Lista de números de 1 a 10;
# Lista com quatro nomes;
# Lista com o ano que você nasceu e o ano atual.

      numeros = [1,2,3,4,5,6,7,8,9,10]
      for numero in numeros:
            print(numero)
            
      lista_de_nomes = ['Rondi','Maura', 'Samara', 'Heitor']
      for nomes in lista_de_nomes:
            if nomes == 'Rondi':
                  print(nomes)
                  
      lista_datas = [1990,2025]
      idade = lista_datas[1] - lista_datas[0]
      print(f'{lista_datas[1]} - {lista_datas[0]} = {idade}')
                  
                  
def loop_simples():
# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
      mercado = ['macarrao','arroz','oleo']
      for produtos in mercado:
            print(produtos)


def soma_impares_loop():
# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
      numeros = [1,2,3,4,5,6,7,8,9,10]
      soma = 0
      for numero in numeros:
            if(numero % 2 != 0):
                  soma += numero
      print(f'Resultado final: {soma}') # fora do loop
      
      soma_impares = 0
      for impares in range(1,11,2):
            soma_impares += impares
            print(soma_impares) # dentro do loop
                  

def contador_1_a_10():
# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
      contador = 10
      while(contador > 0):
            print(contador)
            contador -= 1
            
      for contador in range(10,0,-1):
            print(contador)


def tabuada():
# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
      numerador = int(input('Inorme o numerador: '))
      quantidade_de_multiplicacoes = int(input('Quantas vezes deseja que esse numero seja multiplicado: '))
      
      for i in range(1,quantidade_de_multiplicacoes +1):
            resultado = numerador * i
            print(f'{numerador} x {i} = {resultado}')


def try_except():
# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.
      numeros_e_outros = [1,2,3,4,True,6,7,'abc',9,10]
      soma = 0
      try: 
            for numeros in numeros_e_outros:
                  if isinstance(numeros,int) and not isinstance(numeros,bool):
                        soma += numeros
                  print(soma)      
      except Exception as e:
            print(f'Erro: {e}')
     
      
def media_lista():
    # 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
    numeros_e_outros = [1,2,3,4,True,6,7,'abc',9,25]
    soma = 0
    quantidade = 0

    try:
        for numeros in numeros_e_outros:
            if isinstance(numeros, (int, float)) and not isinstance(numeros, bool):
                soma += numeros
                quantidade += 1
        tamanho_da_lista = len(numeros_e_outros)
        print(f'Tamanho da lista: {tamanho_da_lista}')
        print(f'Soma dos números válidos: {soma}')
        print(f'Quantidade de números válidos: {quantidade}')
        print(f'Média dos números válidos: {soma/quantidade}')
    except ZeroDivisionError:
        print("A lista está vazia, não é possível calcular a média.")
    except Exception as e:
        print(f'Ocorreu um erro ao calcular a média: {e}')


def dicionario_basico():
# 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
# 2 - Utilizando o dicionário criado no item 1:
      # Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
      # Adicione um campo de profissão para essa pessoa;
      # Remova um item do dicionário.

            
      def exibirOpcoes():
            print('1. Mostrar Tabela')
            print('2. Alterar Dados lista')
            print('3. Remover item da lista')
            print('3. Sair')
 
            
      def main():
            exibirOpcoes()
            
            opcao_escolhida = int(input('Escolha uma opcao '))
            
            if opcao_escolhida == 1:
                  tabela()
            if opcao_escolhida == 2:
                  alterar_dados_lista()     
            if opcao_escolhida == 3:
                  remover_item_da_lista()                                    
            if opcao_escolhida == 4:
                  sair()                     
                              

      informacoes_pessoais = [{'nome': 'Rondinelle','idade': 35,'cidade': 'Vitoria'},
                              {'nome': 'Samara','idade': 28,'cidade': 'Belo Horizonte'},
                              {'nome': 'Heitor','idade': 7,'cidade': 'Belo Horizonte'}]

      def titulo():
            titulo = f'{'NOME'.ljust(20)} | {'IDADE'.ljust(20)} | {'CIDADE'.ljust(20)} | {'PROFISSAO'}'
            print(titulo)
            print('-' * (len(titulo)+10))
      
      def tabela():
            titulo()
            try:
                  for name in informacoes_pessoais:
                        nome = name.get('nome', '')
                        idade = str(name.get('idade', ''))
                        cidade = name.get('cidade', '')
                        profissao = name.get('profissao', '')
                        print(f"{nome.ljust(20)} | {idade.ljust(20)} | {cidade.ljust(20)} | {profissao}")
            except Exception as e:
                        print(f'Erro: {e}')
            
            main()
      
      def alterar_dados_lista():
            nome_validacao = input('Digite o nome da pessoa que deseja atualizar a idade: ')
            idade = int(input('Atualize a idade: '))
            profissao = input('Digite o nome da profissao: ')
            
            for dado_lista in informacoes_pessoais:
                  if nome_validacao == dado_lista['nome']:
                        dado_lista['idade'] = idade
                        dado_lista['profissao'] = profissao
                        
            main()     
            
            
      def remover_item_da_lista():
            nome_validacao = input('Digite o nome da pessoa que deseja remover algum item: ')    
            item_removido =   input('Digite o nome do item que deseja remover: ')      
            
            for nome in informacoes_pessoais:
                  if nome_validacao == nome['nome']:
                        if item_removido in nome:
                              nome.pop(item_removido) # remove todo o campo dentro do dicionario
                              nome[item_removido] = None  # Coloca None no valor escolhido
                              
            main() 

      def sair ():
            os.system('cls')

      if __name__ == '__main__':
            main()


def quadrados():
# 3 - Crie um dicionário que relacione os números de 1 a 5 aos seus respectivos quadrados.

      # Com dictionary comprehension:
      numeros_quadrados = {x: x**2 for x in range(1, 6)}
      print(numeros_quadrados)

      # Sem dictionary comprehension:
      numeros_quadrados = {}
      for x in range(1, 6):
            numeros_quadrados[x] = x**2
      print(numeros_quadrados)


def validacao_dicionario():
# 4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.

      pessoa = {'nome': 'Amanda', 'idade': 19, 'cidade': 'São Luís'}
      if 'nome' in pessoa:
            print("A chave 'nome' existe no dicionário.")
      else:
            print("A chave 'nome' não existe no dicionário.")


def verificacao_frequencia_palavras():
# 5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.

      frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
      contagem_palavras = {}
      palavras = frase.split()

      for palavra in palavras:
            contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
      
      print(contagem_palavras)

      # mesma coisa mais simples de entender
      frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
      contagem_palavras = {}
      palavras = frase.split()

      for palavra in palavras:
            if palavra in contagem_palavras:
                  contagem_palavras[palavra] += 1
      else:
            contagem_palavras     

      print(contagem_palavras)
      
      
def exercicios_extras_dicionario_palavras():
      frase = 'O sol brilha brilha sem parar'
      dicionario = {}
      quebrar_frase = frase.split()
      print(f'Antes do for {quebrar_frase}')
      contador = 1
            
      for palavras in quebrar_frase:
            print(f'Contador: {contador}')
            contador += 1            
            if palavras in dicionario:
                  print(f'Dentro do for no if no loop: {palavras}')
                  print(f'Dentro do for, no if no dicionario: {dicionario}')
                  dicionario[palavras] += 1
            else:
                  dicionario[palavras] = 1
                  print(f'Dentro do else no loop: {palavras}')
                  print(f'Dentro do else no dicionario: {dicionario}')
            
      print(f'Saida final do programa: {dicionario}')
      
      # JS FAZENDO A MESMA COISA:
      # let frase = 'O sol brilha brilha sem parar'
      # let dicionario = {}
      # let quebrar_frase = frase.split(" ")
      # console.log(quebrar_frase)

      # for (let palavra of quebrar_frase) {
            # if (palavra in dicionario) {
            #       dicionario[palavra] += 1
            # } 
            # else {
            #       dicionario[palavra] = 1
            #  }      
      # }
 
exercicios_extras_dicionario_palavras()