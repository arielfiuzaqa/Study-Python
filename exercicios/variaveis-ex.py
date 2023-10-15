'''Exercício 1: Variáveis e Impressão

Crie uma variável chamada idade e atribua sua idade a ela.
Crie uma variável chamada altura e atribua sua altura em centímetros a ela.
Crie uma variável chamada nome e atribua seu primeiro nome a ela.
Exiba os valores das variáveis usando a função print.'''

# Fácil - Variáveis e tipos básicos
print('\nVariáveis e tipos básicos\n')
numero = 42              # Um número inteiro
pi = 3.14159265359       # Um número de ponto flutuante (float)
nome = "Alice"           # Uma string
verdadeiro = True        # Um valor booleano (True ou False)

# Exibindo valores
print(numero)
print(pi)
print(nome)
print(verdadeiro)

# Exemplo 2: Operações com Variáveis - Intermediário
print('\nOperações com variáveis\n')
a = 10
b = 5

# Soma
soma = a + b
print("Soma:", soma)

# Subtração
subtracao = a - b
print("Subtração:", subtracao)

# Multiplicação
multiplicacao = a * b
print("Multiplicação:", multiplicacao)

# Divisão
divisao = a / b
print("Divisão:", divisao)

# Potenciação
potencia = a ** b
print("Potenciação:", potencia)

# Resto da divisão
resto = a % b
print("Resto da divisão:", resto)


# Criando uma lista
print('\nListas e Índices\n')
frutas = ["maçã", "banana", "laranja", "uva", "manga"]

# Acessando elementos por índice
primeira_fruta = frutas[0]
terceira_fruta = frutas[2]

# Modificando elementos
frutas[1] = "pera"

# Adicionando elementos
frutas.append("abacaxi")

# Removendo elementos
frutas.remove("laranja")

# Tamanho da lista
tamanho = len(frutas)

# Exibindo a lista completa
print("Lista de Frutas:", frutas)
print("Primeira Fruta:", primeira_fruta)
print("Terceira Fruta:", terceira_fruta)
print("Tamanho da Lista:", tamanho)

'''Exercício 3: Listas e Índices

Crie uma lista chamada numeros com os números de 1 a 5.
Acesse o terceiro número da lista e armazene-o em uma variável chamada terceiro_numero.
Modifique o quarto número da lista para ser 10.
Adicione o número 6 ao final da lista.
Remova o segundo número da lista.
Exiba a lista resultante e o valor da variável terceiro_numero.'''

print('\nExercício 3: Listas e Índices\n')
# Lista de numeros
numeros = [1, 2, 3, 4, 5]
# Acessar o terceiro numero(indice 2) e armazena-lo na variável 'terceiro_numero'
terceiro_numero = numeros[2]
# Modificar o quarto numero(indice 3) para ser 10
numeros[3] = 10
# Adicionar o numero 6 no fim da lista
numeros.append(6)
# Remover o segundo numero(indice 1)
del numeros[1]
# Exibir a lista resultante e o valor da variavel 'terceiro_numero'
print('Lista resultante:', numeros)
print('Valor da terceira posição:', terceiro_numero)


''' Exercicio 5: Escopo de Variáveis - Nivel Hard variáveis

Crie uma variável global chamada total e defina-a como 0.
Crie uma função chamada adicionar que aceita um número como argumento e adiciona esse número ao total.
Crie outra função chamada subtrair que aceita um número como argumento e subtrai esse número do total.
Chame as funções adicionar e subtrair várias vezes com diferentes números para modificar o total.
Exiba o valor final do total.'''

print('\nExercício 5: Escopo de Variáveis\n')
# Crie uma variável global chamada total e defina-a como 0.
total = 0
# Crie uma função chamada adicionar que aceita um número como argumento e adiciona esse número ao total.
def adicionar(numero):
    global total # Informa que estamos modificando a variável global
    total += numero
# Crie outra função chamada subtrair que aceita um número como argumento e subtrai esse número do total.
def subtrair(numero):
    global total # Informa que estamos modificando a variável global
    total -= numero
#Chame as funções adicionar e subtrair várias vezes com diferentes números para modificar o total.
adicionar(10)
adicionar(5)
subtrair(3)
adicionar(8)
# Exiba o valor final do total
print("Valor final do total:", total)


################################################################################################
''' Métodos e Palavras-chaves usadas e seus significados.

> global: A palavra-chave global é usada em Python para declarar uma variável como global, o que 
significa que a variável pode ser acessada de qualquer lugar no código, não apenas no escopo local 
onde foi definida. Isso é útil quando você deseja modificar uma variável global de dentro de uma 
função.

> len(): A função len() é usada para obter o número de elementos em um objeto iterável, como uma 
lista, string, tupla, etc. Por exemplo, len(lista) retorna o número de elementos na lista.

> .append(): O método .append() é usado em listas (e algumas outras estruturas de dados) para 
adicionar um elemento no final da lista. Por exemplo, minha_lista.append(10) adiciona o valor 10 
ao final da lista minha_lista.

> .remove(): O método .remove() é usado em listas para remover a primeira ocorrência de um 
elemento específico da lista. Por exemplo, se você tem uma lista minha_lista e deseja remover o 
número 5, você pode fazer minha_lista.remove(5).
'''
################################################################################################