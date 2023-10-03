# vamos aprender sobre coleções mais especificamente sobre listas
# Para não precisar guardar várias variáveis semelhantes em uma por uma, podemos criar uma lista, ex: da coleção
preco_1 = 20
preco_2 = 50
preco_3 = 80

#Coleçao(lista) Acessamos os valores através dos indices
preco = [20, 50, 80]
#         0,  1,  2   para acessaar cada um, vamos averiguar agora. Vamos acessar cada um assim!
print(preco[0])
print(preco[1])
print(preco[2])

# Posso fazer buscando pelo valor o indice. Fica assim nosso exemplo:
print(preco.index(20))
print(preco.index(50))
print(preco.index(80))

# Outro exemplo semelhante usando tipos diferentes, temos:
diversidade = [29, 'Ariel', True]
print(diversidade[0])
print(diversidade[1])
print(diversidade[2])

# Existe um modo mais fácil de repetir os valores que é através dos laços de repetição
for precos in preco:
    print(precos)
# Outro exemplo
for diversidades in diversidade:
    print(diversidades)


# Desafio - Exercicio
'''Some os valores com coleção, dado uma coleção de dados de 'idades' [15, 46, 75, 34, 23] 
imprima na tela a soma deste valor'''

idades = [15, 46, 75, 34, 23]
total = 0

for idade in idades:
    total = total + idade
    print(total)

