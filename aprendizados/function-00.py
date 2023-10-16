''' Function (Funções) - funções são blocos de código nomeados que realizam uma 
tarefa específica quando chamados. As funções permitem a organização e reutilização 
de código, tornando o código mais modular e legível.

Pode usar a 'def' para criar uma função, onde depois da função criada podemos chamar ela
pelo nome que demos a ela. 

Algumas funções incluem:  print(), len(), input(), range(), entre outras.

input() - Função que recebemos um dado
len() - Função que vai mensurar o tamanho de um objeto
split() - Função que transforma strings em listas

Como Cria uma?

def nome_da_função(parametros):
    bloco do codigo
'''
def dar_boas_vindas(): # podemos deixar sem parametros para tornar mais legivel as funções
    print('Bem-vindo!')

dar_boas_vindas()

# Personalizada
def dar_boas_vindas_personalizadas(nome): 
    print(f'Bem-vindo! {nome}')

dar_boas_vindas_personalizadas('Ariel')

# Valor Padrão
def apresentar_lugar(lugar='Nossa Loja'): # Parametro com valor padrão(designado o valor)
    print(f'Visite {lugar}.')
    
apresentar_lugar() # Com valor padrão não precisa definir, mas quando define é substituido
apresentar_lugar('a Disney') # Retorna o valor designado

'''🥇Desafio🥇'''
''' 
DESAFIO 1 - Crie uma função chamada gerar_nome_completo que recebe como parâmetro o nome 
e sobrenome de alguém e dá boas vindas para essa pessoa
'''
def nome_e_sobrenome(nome, sobrenome):
    print(f'Olá {nome} {sobrenome}') # processando um valor, diferente de retornar um valor

nome_e_sobrenome('Ariel', 'Fontenele')

''' 
DESAFIO 2 - # Crie uma função chamada calcular_valores que recebe 2 parâmetros o primeiro 
o preco de um produto e o segundo parâmetro é a quantidade, porém a quantidade deve haver um 
valor padrão de 1. Sua função deve exibir o resultado do preço do produto, multiplicado a 
quantidade escolhida.
'''
def calcular_valor(preco, quantidade=1):
    print (f'{preco * quantidade:.2f}') # Ou print(preco * quantidade)

calcular_valor(10, 2)


''' Preocessar VS Retornar (Funções) - 
Função que apenas processa dados ex: -> print()
Função que retorna dados ex: -> input() e eu posso guarda esse input em uma variavel.

Como posso escolher entre funções que processam dados e os que retornam dados? Depende!
Vou precisar usar essa informação na lógica do meu programa ainda?
Ou só preciso processaar esse dado, mas não irei utilizar mais ele depois?

Vamos aos exemplos para entender.
'''
# A primeira função não será usada para calculos ou logicas, apenas informa o usuario.
def exibir_cotacao_do_dia(moeda):
    if moeda == 'usd':
        print ('US$5,47')

exibir_cotacao_do_dia('usd')

''' O segundo vai estar devolvendo um resultado para quem chamou ela, ou seja, permite que re-use
dentro da função, colocando assim várias condições caso eu queira por-las'''
def obter_cotacao_do_dia(moeda):
    if moeda == 'usd':
        return 5.47
    
# Podemos cria condições como essa na segunda forma
cotacao = obter_cotacao_do_dia('usd')
if 4 > cotacao > 5.50:
    print('Cotacao alta, cuidado com saque!')
else:
    print("Investir em ações americanas")


''' Argumentos Posicionais VS Argumentos Nomeados
> Argumentos Posicionais:
Argumentos posicionais são passados para a função na ordem em que os parâmetros são definidos.
Eles não são seguidos pelo nome do parâmetro na chamada da função.
A ordem é importante, pois a função associa os valores passados com os parâmetros com base na ordem.

> Argumentos Nomeados (ou Argumentos de Palavra-Chave):
Argumentos nomeados são passados para a função com o nome do parâmetro ao qual eles devem ser associados.
Eles são úteis quando você deseja especificar apenas alguns dos parâmetros de uma função e deseja ignorar os demais.
A ordem não é importante ao usar argumentos nomeados.

Caso coloque um * Todos os parametros apos o * precisam ser nomeados, isso é uma forma de obrigar
a quem for mexer no código nomear determinados parametros dentro do argumento.

Vamos aos exemplos:
'''

print('\nExemplos de Argumentos Nomeados e Posicionados\n')
def exibir_preco(nome_produto, preco): # Parametros - Observe a ordem deles.
    print(f'{nome_produto} custa {preco}.')

exibir_preco('Iphone', 5000) # Corresponde a posição dos parametros - Argumentos Posicionais
exibir_preco(preco=5000, nome_produto='Iphone') # Corresponde independente da ordem - Arg. Nomeados


''' 🥇 Desafio 🥇

Crie uma função chamado gerar_objeto_personalizado que irá receber 3 parâmetros, cor, altura, 
formato.
A sua função deve apenas imprimir na tela o que foi passado para ela, nada mais, nada menos.
Porém ela deve seguir as seguintes regras:

1 - O primeiro argumento deve ser posicional
2 - Os argumentos altura e formato precisam OBRIGATORIAMENTE serem nomeados
'''

print('\nDesafio dos Argumentos\n')
def gerar_objeto_personalizado(cor, *, altura, formato): # Após * todos devem ser nomeados
    print(f'Sua caixa tem {altura}cm e {formato} na {cor}, tudo bem assim?')    

gerar_objeto_personalizado('Azul', formato='Retangular', altura=50)


''' Argumentos Dinâmicos - Funções com numeros de argumentos. Argumentos dinâmicos são um conceito 
em programação que se refere à capacidade de uma função ou método receber um número variável de 
argumentos durante sua chamada. Em Python, esse conceito é implementado usando os operadores 
"*args" e "**kwargs" (abreviações para "argumentos" e "argumentos de palavra-chave").

> *args (Argumentos Posicionais Dinâmicos):
O operador *args permite que uma função aceite um número arbitrário de argumentos posicionais.
Os argumentos passados são empacotados em uma tupla (uma sequência imutável) e podem ser acessados 
dentro da função usando essa tupla.
Isso é útil quando você não sabe antecipadamente quantos argumentos a função receberá.

> **kwargs (Argumentos de Palavra-Chave Dinâmicos):
O operador **kwargs permite que uma função aceite um número arbitrário de argumentos de 
palavra-chave (também conhecidos como argumentos nomeados).
Os argumentos de palavra-chave passados são empacotados em um dicionário (um conjunto de pares 
chave-valor) e podem ser acessados dentro da função usando esse dicionário.
Isso é útil quando você deseja fornecer argumentos opcionais com nomes específicos.

Exemplos:
'''
# *Args(Arguments) - Argumentos posicionais dinâmicos
print('\nAmostra do aprendizado anterior.\n')
def somar(valor, b): # Função com 2 argumentos definidos, valor e b. 
    print(valor + b) # papel que essa função deve desempenhar, que é trazer a somar dos argumentos
somar(10, 10) # Resultado impimido será 20

print('\nExemplo com *args\n')
def somar(*valores, b): # Com * posso estar recebendo mais de um valor no argumento
    print(valores) # Imprime primeiro os valores na tela que estão armazenados
    for valor in valores: 
        b += valor # Pegar o valor dentro de b e somar com os valores
    print(b) # O Resultado final é a soma de tudo com o b.

somar(10, 20, 5, b=5) # Com isso, outros argumentos devem ser nomeados para sua identificação

# **Kwargs(Keyword arguments) - Argumentos nomeados dinâmicos
print('\nExmplo com **kwargs\n')
def concatenar(**palavras):
    frase = ''
    for palavra in palavras.values():
        frase += palavra + ' '
        print(frase)

concatenar(a='Nós', b='Somos', c='Pythonista', d='Profissionais')

# Usando todos os argumentos que aprendemos
print('\nUsando todos os argumentos juntos.\n')
def contagem_de_letras(nome, *args, **kwargs):
    print(nome)
    print(args)
    print(kwargs)
    for arg in args:
        print(arg)
    for kwarg in kwargs.values():
        print(kwarg)

contagem_de_letras('Gugu',5,7,9,11,a=1,b=2,c=3)

# Próximo - Decorators