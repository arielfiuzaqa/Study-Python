''' Um conjunto (SET) é uma estrutura de dados que representa uma coleção de elementos 
únicos e não ordenados. Em outras palavras, um conjunto não permite elementos duplicados, 
e os elementos não estão armazenados em uma ordem específica. Os conjuntos são úteis quando 
você precisa armazenar um grupo de valores onde a ordem não é importante e a duplicação de 
elementos é indesejada. 


Elementos Únicos: Os conjuntos garantem que cada elemento seja único. Se você tentar adicionar 
um elemento que já está no conjunto, ele não será duplicado.

Não Ordenados: Os elementos em um conjunto não têm uma ordem específica. Isso significa que 
você não pode acessar elementos por índice, como faria em uma lista.

Mutabilidade: Os conjuntos são mutáveis, o que significa que você pode adicionar e remover 
elementos de um conjunto após a criação.

Sintaxe de Criação: Você pode criar um conjunto em Python usando chaves {} ou a função set().

Adição de Elementos: Para adicionar um elemento a um conjunto, você pode usar o método add()

Remoção de Elementos: Para remover um elemento de um conjunto, você pode usar o método remove() 
ou discard(). A diferença entre eles é que remove() gera um erro se o elemento não existir, 
enquanto discard() não gera um erro

União de Conjuntos: Para criar um novo conjunto que contenha todos os elementos de dois 
conjuntos existentes, você pode usar o operador | ou o método union()

Interseção de Conjuntos: Para criar um novo conjunto que contenha os elementos que estão 
presentes em ambos os conjuntos, você pode usar o operador & ou o método intersection()

Diferença de Conjuntos: Para criar um novo conjunto que contenha os elementos presentes 
em um conjunto, mas não no outro, você pode usar o operador - ou o método difference()

Verificação de Pertinência: Você pode verificar se um elemento está presente em um conjunto 
usando a palavra-chave in'''

# SET
print('\nSET\n')
numeros = [2, 2, 5, 5, 8 , 9]
frutas = {'banana', 'uva', 'mamao', 'tangirina', 'manga', 'uva', 'mamao'}
# Convertendo para SET
set_numeros = set(numeros)
set_frutas = set(frutas)
# Imprimindo o Resultado temos. Observe que não se repetem valores no resultado
print('Conjunto numeros : ', set_numeros)
print('Conjunto frutas : ', set_frutas)

# Adicionando elementos utilizando SET - add(numero que quero por)
set_numeros.add(10)
print(set_numeros)

# Conjuntos
numeros1 = [2, 2, 5, 5, 8 , 9, 12]
numeros2 = [2, 2, 4, 3, 7 , 9, 11, 11]
# Convertendo para SET em duas variaveis
a = set(numeros1)
b = set(numeros2)
# Printando o Resultado
print(a.symmetric_difference(b)) # Adiciona os valores dos dois sem repetir os valores.
'''Percebi que quando ser repete um numero nos dois não sai esse numero, teoria dos conjuntos?'''

# Intercessão dos Conjuntos
print(a.intersection(b)) # O que ambos os conjuntos tem

# União de Conjuntos
print(a.union(b)) # União dos conjuntos removendo as duplicadas

# Faça mais exercicios sobre o assunto.
