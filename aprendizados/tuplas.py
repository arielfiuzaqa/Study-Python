''' Tuplas: É uma estrutura de dados semelhante a uma lista, mas com uma diferença importante: 
as tuplas são imutáveis. Isso significa que, uma vez que você cria uma tupla, não pode alterar, 
adicionar ou remover elementos dela. As tuplas são frequentemente usadas para representar 
coleções de itens relacionados que não devem ser modificados. 

Podemos usar vários tipos dentro das tuplas. '''

# Tuplas
site1 = 'youtube.com'
site2 = 'facebook.com'
site3 = 'instagram.com'
# ou
valor1 = 23
valor2 = 43
valor3 = 65

sites = ('youtube.com', 'facebook.com', 'instagram.com') # Sintaxe para criar tuplas
valores = (23, 43, 65) # Sintaxe para criar tuplas

print(sites[1]) # Para acessar o youtube.com
print(valores[1]) # Vai vir 43 como resultado.

# Vamos tentar mudar as Tuplas - O que não é possível
print('\nTentando Mudar Tuplas\n')
'''sites[1] = 'google.com'
print(sites[1]) # Vai gerar um erro!'''

# União de Tuplas
dados_sistemas = sites + valores
print('Dados Sistemas:\n', dados_sistemas) # Tupla com a informação das duas Tuplas
print('\nDados Sistemas item 3:' ,dados_sistemas[2]) # Acessamos o 3° item da nova Tupla 'instagram.com'

############################### Aprofundando o Assunto ##########################################






