'''Arrays - Armazena uma coleção de itens como as listas porém apenas do mesmo tipo.
3 Tipos são aceitos dentro de um Array - Inteiros, numeros decimais e caracteres'''

from array import array

numeros = array('i', [1,2,3,4,5,6])
print(numeros)
numeros.append(10) # Adicionando 10 a lista
print(numeros)
numeros.insert(5,200) # Posição 5 de valor 200
print(numeros)
numeros.pop(1) # Para extrair um numero da lista nesse caso o 1°
print(numeros)
numeros.remove(5) #Remove, no caso o item 5
print(numeros)
del numeros[1] # Removendo o indice de numero 1
print(numeros)

''' QUANDO USAR O ARRAYS? '''
