# exemplo de variavel
velocidade_internet = 10
print(velocidade_internet)

# Quais tipos de dados podemos guardar dentro da memoria do pc, os mais comuns? 
# numeros
velocidade_internet = 10
# Valores booleanos
esta_aberto = True
# Strigs
slogan = 'Feito é mellhor que perfeito!'

a,b,c,d = 1, 2, 3, 4,
print(a)
print(b)
print(c)
print(d)

print(type(a))
print(type(velocidade_internet))


#execicio 1.0
variavel_1 = 25.87
variavel_2 = True
variavel_3 = 'Bom dia!'
variavel_4 = 15


print(type(variavel_1))
print(type(variavel_2))
print(type(variavel_3))
print(type(variavel_4))

#==================================================================================================

# Tipo Inteiro (int)

# O tipo inteiro é um tipo composto por caracteres numéricos (algarismos) inteiros.
# É um tipo usado para um número que pode ser escrito sem um componente decimal, podendo ter ou não sinal, isto é: ser positivo ou negativo.
# Por exemplo, 21, 4, 0, e −2048 são números inteiros, enquanto 9.75, 1/2, 1.5 não são.
# Exemplos:

idade = 18
ano = 2002

print(type(idade))
print(type(ano))



# Ponto Flutuante ou Decimal (float)

# É um tipo composto por caracteres numéricos (algarismo) decimais.
# O famoso ponto flutuante é um tipo usado para números racionais (números que podem ser 
# representados por uma fração) informalmente conhecido como “número quebrado”.
# Exemplos:

altura = 1.80
peso = 73.55

print(type(peso))
print(type(altura))



#Boolean (bool)

# Tipo de dado lógico que pode assumir apenas dois valores: falso ou verdadeiro (False ou True em Python).
# Na lógica computacional, podem ser considerados como 0 ou 1.
# Exemplos:

fim_de_semana = True
feriado = False

print(type(fim_de_semana))
print(type(feriado))



#Listas (list)

# Tipo de dado muito importante e que é muito utilizado no dia a dia do desenvolvedor Python!
# Listas agrupam um conjunto de elementos variados, podendo conter: inteiros, floats, strings, outras listas e outros tipos.
# Elas são definidas utilizando-se colchetes para delimitar a lista e vírgulas para separar os elementos, 
# veja alguns exemplo abaixo:

alunos = ['Amanda', 'Ana', 'Bruno', 'João']
notas = [10, 8.5, 7.8, 8.0] 

print(alunos)
print(type(alunos))
print(notas)
print(type(notas))



# String (str)

# É um conjunto de caracteres dispostos numa determinada ordem, 
# geralmente utilizada para representar palavras, frases ou textos.
# Exemplos:

nome = 'Guilherme'
profissao = "Engenheiro de Software"

print(profissao)
print(type(profissao))
print(nome)
print(type(nome))

# Utilizando o \n na string para quebra de linha e \\ para evidenciar a barra
print('''Estou codando todos os dias
      e estou aprendendo muito! ''')
print('Olá meu nome é Ariel Fiuza \nmas pode me chamar de \namor da sua vida.')
# Utilizando o len para dizer a quantidade de caracteres da string
print(len(nome))

# Strings Dinâmicos
# Quando você se escreve em um site e logo depois você recebe uma mensagem personalizada 
# com seus nome tipo, Olá Fulando, seja bem-vindo ao nosso curso. Como se faz isso?
# Isso é chamado de string dinâmico
#exemplo:

nome = 'Rafael'
email = 'rafafa@gmail.com'
# Mensagem que quero colocar: Olá Rafael, você cadastrou o email rafafa@gmail.com,
#essa informação esta correta?
print(f'Olá {nome}, você cadastrou o email {email}, essa informação esta correta?')

# # Métodos comuns de strings
# Dentro de uma string podemos fazer diversas operações colocando após o nome da 
# variável um simples ponto, vou estudar os mais importantes nesse momento
# Podemos colocar direto na variável após defini-lá em outra instancia ou diretamento
# dentro do print
#Exemplo:
curso_rapido = ' Aprendendo a programar '

print(curso_rapido.upper()) # deixa todas as letras maiusculas
print(curso_rapido.lower()) # deixa todas as letras minusculas
print(curso_rapido.strip()) # Pode remover todos os espaços em branco,
print(curso_rapido.lstrip()) # Pode remover todos os espaços em brancos da esquerda
print(curso_rapido.rsplit()) # Pode remover todos os espaços em brancos da direita
print(curso_rapido.find('amar')) # Caso queira encontra alguma informação dentro do script
print(curso_rapido.replace('Aprendendo', 'Cantar')) # Vai substituir a primeira palavra que vc colocar pela segunda que vc quer que substitua
print('https://site/dfhdufdu=relogio'.replace('relogio','carro')) # muda a palavra, serve para mudança de categoria por exemplo

#exercicio
# DESAFIO 🥇
# Através da criação de string dinâmicos e os métodos de um string que acabou de aprender, 
# use como base as variáveis a seguir para criar as seguintes frases

a = 'é'
b = 'MELHOR'
c = 'QUE'
d = 'feito'
e = 'perfeito'

print('É melhor FEITO que PERFEITO') # o de baixo deve sair igual
print(f'{a.upper()} {b.lower()} {d.upper()} {c.upper()} {e.upper()}')


# Complexo (complex)

# Tipo de dado usado para representar números complexos (isso mesmo, aquilo que 
# provavelmente estudou no terceiro ano do ensino médio).
# Esse tipo normalmente é usado em cálculos geométricos e científicos.
# Um tipo complexo contem duas partes: a parte real e a parte imaginária, 
# sendo que a parte imaginária contem um j no sufixo.
# A função complex(real[, imag]) do Python possibilita a criação de números 
# imaginários passando como argumento: real, que é a parte Real do número complexo 
# e o argumento opcional imag, representando a parte imaginária do número complexo.
# Exemplos:

a = 5+2j
b = 20+6j

print(type(a))
print(type(b))
print(complex(2, 5))


#Tuplas (tuple)

# Assim como Lista, Tupla é um tipo que agrupa um conjunto de elementos.
# Porém sua forma de definição é diferente: utilizamos parênteses e também separado por vírgula.
# A diferença para Lista é que Tuplas são imutáveis, ou seja, após sua definição, 
# Tuplas não podem ser modificadas.
# Vamos ver alguns exemplos:

valores = (90, 79, 54, 32, 21)
pontos = (100, 94.05, 86.8, 62)

print(type(valores))
print(type(pontos))


# Dicionários (dict)

# Dict é um tipo de dado muito flexível do Python.
# Eles são utilizados para agrupar elementos através da estrutura de chave e valor, 
# onde a chave é o primeiro elemento seguido por dois pontos e pelo valor.
# Vamos ver alguns exemplos:

altura = {'Amanda': 1.65, 'Ana': 1.60, 'João': 1.70}
peso = {'Amanda': 60, 'Ana': 58, 'João': 68}

print(altura)
print(type(altura))
print(peso)
print(type(peso))