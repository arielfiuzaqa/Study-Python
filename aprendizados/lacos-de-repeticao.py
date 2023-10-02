# Laços de repetição + Listas, esses dois conceitos estão ligados
# O que são? Sâo maneiras de executar o mesmo comando várias vezes

# Os laços de repetição em Python são estruturas de controle que permitem 
#que um bloco de código seja executado repetidamente. Os laços de repetição 
#mais comuns em Python são o laço `for` e o laço `while`.
# O laço `for` é usado para iterar sobre uma sequência de valores. 
#A sintaxe do laço `for` é a seguinte:

# Exemplo:
for palavras in range(1, 4): # não inclui o ultimo, repete 3x nesse caso.
    print("Carregando...")

for item in range(1, 21): # vai repetir numero +1 ate o 20° numero
    print(item)

for item in range(1, 22, 2): # vai repetir numero +1 ate o 21° numero, pulando de 2 em 2
    print (item)

# Os Laços de repetição estão atrelados as listas, e criar uma lista é simples
nomes = ['ariel', 'cristina', 'tiazinha', 'r7', 'frodo']

for nome in nomes: # percebe como eu chamo cada unidade da minha lista
    print(nome) # Isso se reflete loga a baixo

# vamos resolver um problema agora
# Problema 1 a n - Imprimir valores de 1 a n

'''input numero maximo
valor inicial = 1
loop de valor inicial a numero maximo
print valor'''

valor_maximo = int(input('Digite o valor máximo: '))
valor_inicial = 1

for numero in range(valor_inicial, valor_maximo + 1):
    print ('Valor atual:',numero )