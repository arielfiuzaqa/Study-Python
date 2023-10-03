# Tipos de números que podem ser usados no Python
a = 20 # inteiro (int)
b = 20.5 # Decimais (Float)

# Para descobrir qual o tipo de variável basta imprimir com o método type
print(type(a))
print(type(b))

# Operações Matemáticas - Possíveis no python, basta usar o literal praticamente.
print(10 + 6)
print(10 - 6)
print(10 * 6)
print(10 / 6)
print(10 // 6) # Divisão de inteiro (quantos vezes o numero pode ser incerido dentro de outro)
print(10 % 6) # modulos (o que sobra de uma divisão - o resto da divisão de modo inteiro)
print(10 ** 6) # exponenciais

'''Atalho para distribuição mais rápida se utilizando das mesma variáveis com os números que você
deseja utilizar novamente'''
a = 10
a = a + 5
a += 5

b = 20
b = b - 2
b -= 2

'''Operações matemáticas mais comuns - No caso o aredondamento para o valor mais próximo usamos
o seguinte método'''
print(round(3.3))
print(round(5.7))

#Mas se for para valores para cima usa-se
import math
print(math.ceil(2.2))
print(math.ceil(3.1))

'''Para saber mais sobre as operações matemáticas em python, pesquise por:
'python math documentation'. Assim consigo ver os modulos e funções possíveis de usar.
Inclusive vá ver alguns!'''


