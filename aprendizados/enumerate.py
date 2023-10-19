''' ENUMARATE -  é uma função embutida em Python que permite iterar sobre uma sequência 
(como uma lista, tupla ou string) juntamente com um contador que representa o índice ou 
posição do item atual na sequência. Isso é útil quando você precisa acompanhar a posição 
dos elementos durante a iteração. A função enumerate retorna um objeto enumerado que pode 
ser usado em um loop for. '''

# Range Feito Normalmente
for i in range(5): #0,1,2,3,4
    print(i)


# Enumerate Simples
print('\nEnumerate Simples\n')
frutas = ['maçã', 'banana', 'laranja', 'uva']

for indice, fruta in enumerate(frutas):
    print(f'Índice {indice}: {fruta}')

# Enumerate c/ Range - Indice com criação automatica da lista
print('\nEnumarate c/ Range\n')
for indice, numero in enumerate(range(1,21), 0): # Valores gerados e depois o indice que começa
    print(indice, numero)
    if indice == 5: # Diz o indice que quero tomar uma decisão
        print('Estamos na metade da lista!') # Decisão de falar algo

# Enumerate Menos Simples
print('\nEnumarate Menos Simples\n')
nomes = ['Rafael', 'Daniela', 'Joice', 'Gugu', 'Freira']

for indi, nome in enumerate(nomes, 1):
    print(indi, nome)
    if indi == 1:
        print('O primeiro nome registrado')

# Desafio - Fruta em Promoção
print('\nDesafio - Promoção\n')
fruits = ['Maça', 'Laranja', 'Morango', 'Limão']
for indice, fruit in enumerate(fruits, 0):
    if indice == 3:
        print(f'{indice} {fruit} Em PROMOÇÃO!')
    else:
        print(indice, fruit)
