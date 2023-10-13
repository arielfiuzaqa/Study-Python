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