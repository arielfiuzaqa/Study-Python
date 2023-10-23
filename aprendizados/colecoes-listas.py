'''vamos aprender sobre coleções mais especificamente sobre listas
Para não precisar guardar várias variáveis semelhantes em uma por uma, podemos criar uma lista, 
ex: da coleção
'''
# Coleções - Listas - Modo Oficial!! 4° Pilar da programação
# Itens - Valor individual
preco_1 = 20
preco_2 = 50
preco_3 = 80
# Lista - Valor coletivo - Coleção dos dados
preco = [20, 50, 80, 100, 120, 150, 180, 200, 250]
#       [ 0 , 1 , 2 ]  Indice inicia no zero (0) 
preco[2] # Para acessar um item especifico da lista, indice (Referente a um item da lista)
print(preco[2]) # Imprime o indice 2 que é o 3° elemento da lista

# Forma Dinâmica do Indice - função Index
'''Como encontro o item que tem valor de 150 sem ter que contar ate achar o indice?'''
print('\nForma Dinâmica do Indice - Função Index\n')
preco[preco.index(150)] # É a forma de se achar dentro da lista o indice correspondente a 150
print(preco[preco.index(150)]) # Imprimindo o resultado
'''Listas em Python são dinâmicas aceitando qualquer valor desde numeros a boleanos, strings, 
etc'''

# Forma Diferentes de Gerar Listas
# Multiplicando Valores(Repetição de valores)
print('\nMultiplicando Valores(Repetição de Valores)\n')
valores = [7] * 10 # Uma lista de 7 repetidos 10 vezes - Serve para qualquer tipo essa REGRA.
print(valores) # Imprimindo o Resultado
# Usando gerador Range(Sequência) - de 1 até 29
print('\nGerador Range(Sequência)\n')
faixa_de_numeros = list(range(30)) # Range cria a sequência, list cria a lista e tudo dentro da nossa variável
print(faixa_de_numeros) # Imprimimos o resultado da nossa variável
# Gerar a partir de Strings
print('\nGerar a partir de Strings\n')
print(list('Bem-vindo ao Treinamento')) # Todas as letras transformadas em itens de lista, ate ' '
# Lista de Lista(matriz)
print('\nLista de Lista(Matriz)\n')
lista_de_listas = [['Carol', 30], ['Felipe', 25]] # Acessando 1° item e 1° propriedade que é 'Carol'
print(lista_de_listas[0]) # Retorna a primeira lista
print(lista_de_listas[0][0]) # Retornou apenas Carol pois só queremos saber qual nome está
print(lista_de_listas[1][0]) # Retorna apenas Felipe
''' Slicing (Fatiamento) -  permite que você crie uma nova lista que consiste em um subconjunto 
dos elementos da lista original, especificando um intervalo de índices.'''
print('\nSlicing (Fatiamento)\n')
minha_lista = [1, 2, 3, 4, 5]
fatia = minha_lista[1:4]  # Isso criará uma nova lista [2, 3, 4]
print(fatia)
'''Adição e Remoção de Itens - Os métodos append() e remove() permitem adicionar e remover 
elementos de uma lista, respectivamente.'''
print('\nAdição e Remoção de Itens\n')
minha_lista = [1, 2, 3]
minha_lista.append(4)  # Adiciona 4 à lista
minha_lista.remove(2)  # Remove o elemento 2 da lista
print(minha_lista)
''' Ordenação - O método sort() classifica a lista em ordem crescente. Você também pode usar 
sorted() para criar uma nova lista ordenada sem modificar a original. '''
print('\nOrdenação de Lista\n')
minha_lista = [3, 1, 2]
minha_lista.sort()  # Ordena a lista em ordem crescente
print(minha_lista)
''' Operações de Lista - O operador + permite concatenar (juntar) duas listas em uma única lista.'''
print('\nOperação de Listas\n')
lista1 = [1, 2]
lista2 = [3, 4]
lista3 = lista1 + lista2  # Combina as listas em uma única lista
print(lista3) # Resultado [1, 2, 3, 4]
''' List Comprehensions - São uma maneira concisa de criar listas aplicando uma expressão a 
cada item de outra lista (ou iterável). '''
print('\nList Comprehensions\n')
numeros = [1, 2, 3, 4, 5]
quadrados = [x ** 2 for x in numeros]  # Cria uma lista de quadrados [1, 4, 9, 16, 25]
print(quadrados) # Cria uma lista dos Quadrados da outra lista
''' Funções Built-in - A função len() retorna o número de elementos em uma lista.'''
print('\nFunções Built-in - len()\n')
minha_lista = [2, 4, 6, 8]
comprimento = len(minha_lista)  # Retorna o comprimento da lista (4)
print(comprimento) # Retorna o numero de elementos da lista
''' Métodos Built-in - Os métodos insert() e pop() permitem inserir elementos em uma 
posição específica e remover elementos, respectivamente. '''
print('\nMétodo Built-in - insert() e pop()\n')
minha_lista = [1, 2, 3]
minha_lista.insert(0, 4)  # Insere o valor 4 na posição 1
elemento = minha_lista.pop()  # Remove o último elemento e retorna (3)
print(minha_lista)
print(elemento)
''' Operações de Conjuntos - Você pode usar operadores de conjunto (|, &, -) 
para realizar operações de conjunto em listas. '''
print('\nOperações de Conjuntos - (|, &, -)\n')
A = [1, 2, 3]
B = [3, 4, 5]
uniao = list(set(A) | set(B))  # Cria uma lista com a união de A e B
print(uniao)
''' Gerador de Listas - A função map() aplica uma função a cada item da lista numeros 
e list() cria uma lista a partir do resultado.'''
print('\nGerador de Listas - Função map()\n')
numeros = [1, 2, 3, 4, 5]
quadrados = list(map(lambda x: x ** 2, numeros))  # Cria uma lista de quadrados
print(quadrados) # Resultado [1, 4, 9, 16, 25]

# Desafios #
'''Desafio #1 Crie uma lista que tenha os nomes dos 3 objetos que você mais usa durante o dia 
e imprima ele na tela.
'''
print('\nDesafio #1\n')
objetos = ['computador', 'caneta azul', 'agenda', 'café']
print(objetos)
''' Desafio #2 Usando apenas uma linha de código, crie uma lista de 10 a 131'''
print('\nDesafio #2\n')
lista_de_10_a_131 = list(range(10, 132))
print(lista_de_10_a_131)
''' Desafio #3 Imprima na tela o resultado da combinação da lista do desafio 1 e desafio 2 '''
print('\nDesafio #3\n')
print(objetos + lista_de_10_a_131)
''' Desafio #4 Crie uma lista de listas(matriz) que tenha os nomes dos 3 objetos
 que você mais usa durante o dia, mas agora dentro de cada item você vai colocar 
uma informação extra, coloque o valor em reais desse objeto também e imprima ele 
na tela '''
print('\nDesafio #4\n')
itens_mais_usados = [['computador', 5000],['caneta azul', 1.50],['agenda', 15],['café', 2]]
print(itens_mais_usados[0][0]) # Vem o 'computador'
print(itens_mais_usados[0][1]) # Vem o '5000'
print(itens_mais_usados[1][0]) # Vem o 'caneta azul'
print(itens_mais_usados[1][1]) # Vem a '1.50'


''' Manipulação de Listas - Manipular os elementos dentro das listas '''

print('\nAdicionando valores na lista com append( )\n')
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
anos = [2020, 2030, 2040, 2050]
# Adicionando item no final da lista - append()
values.append(11) # Adicionei o valor 11 no final da lista
print(values)
# Extendendo a lista values para os anos também, somando as listas
print('\nUnir lista com método - extend( )\n')
values.extend(anos) # Lista values foi extendida com a lista anos
print(values)
# Adicionar listas sem modificar a atual - '+'
print('\nSomando listas - Sem modificar as atuais\n')
novos_valores = values + anos   # Novo vetor criado juntando values e anos
print(novos_valores)
# Adicionando novo valor a lista - insert( )
print('\nAdicionar Novo Valor a Lista - insert( )\n')
values.insert(0, 'Olá Mundo!') # Inserindo um novo elemento no inicio da lista 0=posição 1° da lista
print(values) 
# Extrair com base no indice - pop( )
print('\nExtrair com base no Indice - pop( )\n')
valor_ola = values.pop(0) # Como quero extrair o primeiro valor o indice é o zero (0)
print(valor_ola) # Extrai o olá mundo! e imprimi como resultado
# Remove Item da Lista - Modificar a lista original
print('\nRemove Item da Lista - remove( )\n')
values.remove(1) # Removido o 1 da lista .remove(valor que quero remover)
print(values) # Como remove dar um erro falando que não existe o item da lista
# Remove Item da lista por Indice - del
del anos[3] # Remove o 4° item da lista no caso 2050
print(anos) # Resultado [2020, 2030, 2040] sem 2050
# Exemplo 2 - del - Podemos remover uma 'faixa de valores' inclusive ex: del y[x2:x6]
print('\nExemplo 2 - del\n')
del values[1:9]
print(values) # Resultado [2, 11, 2020, 2030, 2040, 2050]  de 3 a 10 somem
# Contando Ocorrências de valor - count( )
print('\nContando Ocorrencia do Valor - count()\n')
anum = [0, 0, 10, 20, 25, 50, 55, 60, 70, 100]
print(anum.count(0))  # Quantas vezes o zero aparece (apenas o zero)
# Resetar Itens de uma Lista - Todos
print('\nResetar Itens de Uma Lista - clear( )\n')
resetar = ['a','b','c'] # Lista para resetar
resetar.clear() # Limpa todos os itens da lista
print(resetar) # Volta a lista vazia []

''' Ordenando Listas - Simples. Mais prática!! '''
# Ordem Crescente
print('\nOrdenação de Listas - sort( )\n')
numeros = [10, 2, 5, 3, 1, 8, 7, 6, 4, 0]
numeros.sort() # Ordem Crescente - Decrescente coloca o valor .sort(reverse=True)
print(numeros) # Resultado [0, 1, 2, 3, 4, 5, 6, 7, 8, 10]
# Ordem Decrescente
print('\nOrdem Decrescente\n')
numeros.reverse() # Ordem Decrescente
print(numeros) # Resultado [10, 8, 7, 6, 5, 4, 3, 2, 1, 0]

''' Trabalhar com Multiplas Listas - Zip '''
# Combinar multiplas listas em pares
print('\nCombinação de Multiplas Listas\n')
a_lista = ['A', 'B', 'C', 'D', 'E', 'F']
b_lista = [1, 2, 3, 4, 6, 7]
c_lista = [10, 20, 30, 40, 50, 60]
# Inteirando as listas a e b temos
for a,b in zip(a_lista, b_lista): # Imprime em ordem sequencial cada item das listas
    print(a)
    print(b)
# Incluindo na frase duas listas de mesmo tamanho
print('\nIncluindo duas Listas de mesmo tamanho em uma frase\n')
produtos = ['produto 1','produto 2','produto 3','produto 4','produto 5']
precos = [50, 100, 150, 200, 250]
for a,b in zip(produtos, precos): # Com duas listas do mesmo tamanho
    print(f'Salvando produto {a} valor R$ {b}') # Bem simples O.O

# Listas de Tamanhos diferentes
from itertools import zip_longest # Como vou ate o ultimo item da lista mais longa
print('\nListas de Tamanhos Diferentes\n')
titulos = ["Titulo 1", "Titulo 2", "Titulo 3", "Titulo 4"]
descricao = ['Desc 1', 'Desc 2', 'Desc 3']

for titulos, descricao in zip_longest(titulos, descricao):
    print(f'Encontramos o {titulos} descrição: {descricao}')

''' DESAFIOS 🥇 - Usando as listas abaixo:'''
print('\nDesafio Zip Longest - Listas de Diferentes tamanhos\n')
from itertools import zip_longest
produtos = ['Produto 1', 'Produto 2', 'Produto 3', 'Produto 4', 'Produto 5']
precos = ['R$500,00', 'R$1500,00', 'R$2700,00', 'R$5000,00']
for produto, preco in zip_longest(produtos, precos):
    print(f'Produto: {produto} encontramos no valor de {preco}')

############################################ ORDENANDO COLEÇÕES ###################################
print('\nOrdenando de Forma Crescente\n')
names = ['Zeck', 'Xangu', 'Abdael', 'Anexus', 'Pasquinel', 'Edrus']
valores = [31, 55, 10, 21, 7, 18, 99, 91]

names.sort() # Ordenando em ordem crescente
valores.sort() # Ordenando em ordem crescente
print('Nomes:\n', names)
print('Valores:\n', valores)

# Utilizando Itemgetter

# Ordene a lista de produtos abaixo pelo preço em ordem crescente - Pelos indices
print('\nItemgetter - Lista sem chaves\n')

from operator import itemgetter

prod = [
    {'nome': 'Celular', 'preco': 1500},
    {'nome': 'Monitor', 'preco': 500},
    {'nome': 'Microfone', 'preco': 300}
]

# Ordenar a lista de dicionários pelo preço
prod_ordenados = sorted(prod, key=itemgetter('preco'))
print(prod_ordenados)
print(type(prod))


# Ordene em ordem descrescente a lista de equipamento_filmagem por valor do equipamento
print('\nItemgetter - Atraves do Indice\n')

equipamento_filmagem = [
    ('Tripé', 300),
    ('Câmera', 1700),
    ('Iluminação', 200),
]
equipamento_filmagem.sort(key=itemgetter(1), reverse=True)
print(equipamento_filmagem)
print(type(equipamento_filmagem))


# Ordene em ordem crescente a cotacao_moedas com base no valor da moeda
print('\nItemgetter - Moedas\n')
cotacao_moedas = [['usd', 5.25], ['brl', 1.56], ['eur', 6.47]]
cotacao_moedas.sort(key=itemgetter(1))
print(cotacao_moedas)
print(type(cotacao_moedas))



# Como Criar uma Lista? - Usando Loops e Range()
print('\nCriando Lista - Loop e Range()\n')
numeros = []
for i in range(5):
    numeros.append(i)
print(numeros)

# Map
print('\nMAP\n')
nomes = ['Larissa', 'Daniela', 'Carolzinha', 'Marcus']

def aprovados(nome):
    return nome + ' APROVADO'

print(list(map(aprovados, nomes)))

# MAP - Exemplo 2
print('\nMap - Exemplo 2\n')
numeros = [1, 2, 3, 4, 5]
resultado = map(lambda x: x * 2, numeros)
lista_duplicada = list(resultado)
print(lista_duplicada)

''' Filtrando dados de uma coleção - Filter.  Retorna aqueles dados que são avaliados como
verdadeiros atendendo um determinado parametro'''
print('\nFILTER\n')
list_nomes = ['Larissa', 'Joana', 'Claudisleia', 'Diovanni']

def pessoas_aprovada(pessoa):
    if pessoa == 'Claudisleia':
        return True
    else:
        return False
# Observe a construção
print(list(filter(pessoas_aprovada, list_nomes)))
# Tudo que foi considerado como false no reflexo do pedido
print(list(map(pessoas_aprovada,list_nomes)))


# Exemplo 2 - Filter
print('\nExemplo 2 - Filter\n')
pinturas = []

def eh_antiguidade(pintura):
    if pintura[2] < 1800:
        return True
    else:
        return False
    
print(list(filter(eh_antiguidade, pinturas)))
# Observe as respostas
print(list(map(eh_antiguidade, pinturas)))

# DESAFIO 1 🥇
print('\nDesafio Filter\n')
'''Usando a lista abaixo, filtre apenas as vagas com salário acima de R$2500'''
vagas = [
    ['vaga 1', 1200],
    ['vaga 2', 2550],
    ['vaga 3', 5000]
]     
def salario(valor):
    if valor[1] > 2500:
        return True
    else:
        return False
    
print(list(filter(salario, vagas)))
print(list(map(salario, vagas)))

