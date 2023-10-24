# Conversões entre Tipos
idade = input('Digite sua idade: ') # Não esta como inteiro!
print(int(idade) > 17) # Convertemos para valor inteiro!

# Conversão Outro exemplo
ano_publicacao = 2020
print('Este livro foi criado em ' + str(ano_publicacao)) # Repare que se não tiver o tipo str da erro.

# Conversão Mais um Exemplo
altura = input('Qual a altura da parede? ') # Está sem o tipo determinado de entrada
print(float(altura) > 2.50) # Colocamos o tipo float

# Conversões entre Coleções
saudacao = 'Hello!'
print(list(saudacao)) # Conversão para lista
print(set(saudacao)) # Conversão para dicionario
print(tuple(saudacao)) # conversão para tupla
print(list(range(30))) # Convertendo uma range para uma lista

# Faça os tipos
numeros = [10,10,20,20,30,40,50,60,60]