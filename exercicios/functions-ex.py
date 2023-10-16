# Nível Básico: Definindo Funções Simples

# Exercício 1: Cumprimento
print('Exercício 1: Cumprimento\n')
def cumprimentar(nome):
    saudacao = 'Olá ' + nome + '!'
    print(saudacao)
# Chamando a função e exibindo o resultado
cumprimentar(" Mack Lov")


# Exercício 2: Soma
print('\nExercício 2: Soma\n')
def soma(a, b):
    resultado = a + b
    print("A soma é:", resultado)
# Chamando a função e exibindo o resultado
soma(5, 3)


# Exercício 3: Média de uma Lista
print('\nExercício 3: Média de uma Lista\n')
def media_lista(lista):
    if len(lista) == 0:
        media = 0
    else:
        media = sum(lista) / len(lista)
    print("A média da lista é:", media)
# Chamando a função e exibindo o resultado
valores = [10, 20, 30, 40, 50] # Lista usada
media_lista(valores)


# Exercício 4: Números Primos
print('\nExercício 4: Números Primos\n')
def eh_primo(numero):
    if numero <= 1:
        primo = False
    else:
        primo = True
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                primo = False
                break
    if primo:
        print(numero, "é primo.")
    else:
        print(numero, "não é primo.")
# Chamando a função e exibindo o resultado
eh_primo(17)
eh_primo(4)


# Exercício 5: Fatorial Recursivo
print('\nExercício 5: Fatorial Recursivo\n')
def fatorial(n):
    if n == 0:
        return 1
    resultado = n * fatorial(n - 1)
    print("O fatorial de", n, "é:", resultado)
    return resultado
# Chamando a função e exibindo o resultado
fatorial(5)


# Exercício 6: Fibonacci Recursivo
print('\nExercício 6: Fibonacci Recursivo\n')
def fibonacci(n):
    if n <= 1:
        return n
    resultado = fibonacci(n - 1) + fibonacci(n - 2)
    print("O termo", n, "da sequência de Fibonacci é:", resultado)
    return resultado
# Chamando a função e exibindo o resultado
fibonacci(7)



# Exercício 7: Função com Argumentos Opcionais
print('\nExercício 7: Função com Argumentos Opcionais\n')
def soma_valores(a, b, c=0): # a e b Posicionais e c é argumento nomeado
    resultado = a + b + c
    return resultado
# Chamando a função com diferentes números de argumentos
print(soma_valores(2, 3))       # Resultado: 5
print(soma_valores(2, 3, 4))    # Resultado: 9
'''
Neste exercício, a função soma_valores aceita três argumentos: a, b e c, sendo c opcional. 
Se c não for fornecido, ele assume o valor padrão de 0.
'''


# Exercício 8: Função Lambda
print('\nExercício 8: Função Lambda\n')
quadrado = lambda x: x ** 2
# Chamando a função lambda
resultado = quadrado(5)
print("O quadrado de 5 é:", resultado)
'''
A função lambda chamada quadrado aceita um argumento x e retorna o seu quadrado. 
Chamamos essa função lambda com 5 como argumento, o que resulta no quadrado de 5.
'''


# Exercício 9: Compreensão de Listas
print('\nExercício 9: Compreensão de Listas\n')
numeros = list(range(1, 11))
pares = [x for x in numeros if x % 2 == 0]
# Exibindo a lista de números pares
print("Números pares:", pares)
'''
criamos uma lista de números de 1 a 10 usando a função range, e depois usamos uma compreensão 
de lista para criar uma nova lista chamada pares que contém apenas os números pares. 
O resultado é exibido na tela.
'''

# Exercício 10: Função Recursiva para Cálculo de Potência
print('\nExercício 10: Função Recursiva para Cálculo de Potência\n')
def potencia(a, b):
    if b == 0:
        return 1
    elif b < 0:
        return 1 / (a * potencia(a, -b - 1))
    else:
        return a * potencia(a, b - 1)
# Testando a função
resultado = potencia(2, 10)
print("2 elevado à potência 3 é:", resultado)


# Exercício 11: Função de Ordem Superior
print('\nExercício 11: Função de Ordem Superior\n')
def aplicar_funcao(funcao, numeros):
    return [funcao(x) for x in numeros]
# Funções que podemos aplicar
def quadrado(x):
    return x ** 2
def cubo(x):
    return x ** 3

numeros = [1, 2, 3, 4, 5]
# Aplicando as funções aos números
resultados_quadrado = aplicar_funcao(quadrado, numeros)
resultados_cubo = aplicar_funcao(cubo, numeros)

print("Quadrados:", resultados_quadrado)
print("Cubos:", resultados_cubo)



# Exercício 12: Compreensão de Listas Avançada
print('\nExercício 12: Compreensão de Listas Avançada\n')
def eh_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Lista para testar
primos = [x for x in numeros if eh_primo(x)]

print("Números primos:", primos)
'''
Esse é um bom exemplo para testar com números random onde ele dá a resposta
'''


# Exercício 13: Funções Recursivas com Memoização
print('\nExercício 13: Funções Recursivas com Memoização\n')
# Dicionário para memoização
memo = {}
# Função
def fibonacci(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        result = n
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)
    memo[n] = result
    return result
# Testando a função com memoização
resultado = fibonacci(12)
print("O décimo termo da sequência de Fibonacci é:", resultado)


# Exercício 14: Função Decoradora
print('\nExercício 14: Função Decoradora\n')
def verificar_tipo(tipo_retorno):
    def decorador(funcao):
        def wrapper(*args, **kwargs):
            resultado = funcao(*args, **kwargs)
            if not isinstance(resultado, tipo_retorno):
                raise TypeError(f"A função deve retornar um valor do tipo {tipo_retorno}.")
            return resultado
        return wrapper
    return decorador
# Usando a função decoradora
@verificar_tipo(int)
def duplicar_numero(x):
    return x * 2
# Testando a função decorada
resultado = duplicar_numero(5)
print("Resultado:", resultado)

'''
Estes exercícios avançados abordam funções complexas, ordem superior e manipulação avançada 
de listas, e são uma excelente maneira de aprofundar seu entendimento das capacidades de 
funções em Python.
'''

############################################ EXPERT ##############################################

# Exercício 14: Função Recursiva com Memoização Avançada
print('\nExercício 14: Função Recursiva com Memoização Avançada\n')
# Dicionário para memoização com cache
cache = {} # Dict = Dicionario que é um tipo de lista, mas está vazia para receber valores
def fibonacci(n):
    if n in cache:
        return cache[n]
    if n <= 1:
        result = n
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)
    cache[n] = result
    return result
# Testando a função com memoização avançada
resultado = fibonacci(100)
print("O centésimo termo da sequência de Fibonacci é:", resultado)


# Exercício 15: Funções Geradoras
print('\nExercício 15: Funções Geradoras\n')
def gerar_primos():
    numero = 2
    primos = []
    while True:
        for p in primos:
            if numero % p == 0:
                break
        else:
            primos.append(numero)
            yield numero
        numero += 1
# Testando a função geradora para gerar números primos
gerador = gerar_primos()
for _ in range(10):
    primo = next(gerador)
    print(primo, end=" ")
'''
criamos uma função geradora gerar_primos que gera uma sequência infinita de números primos. 
Ela usa um loop infinito e verifica se cada número é primo antes de gerá-lo.
'''

# Exercício 16: Funções Aninhadas
print('\nExercício 16: Funções Aninhadas\n')
def criar_contador():
    contador = 0
    def incrementar():
        nonlocal contador
        contador += 1
        return contador
    return incrementar

contador1 = criar_contador()
contador2 = criar_contador()

print(contador1())  # Saída: 1
print(contador1())  # Saída: 2
print(contador2())  # Saída: 1
'''
a função criar_contador retorna uma função interna incrementar que mantém o estado do contador 
usando a variável nonlocal.
'''

# Exercício 17: Uso Avançado de Funções de Ordem Superior
print('\nExercício 17: Uso Avançado de Funções de Ordem Superior\n')
def memoizacao(funcao):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = funcao(*args)
        return cache[args]
    return wrapper

@memoizacao
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
# Testando a função decorada com memoização avançada
resultado = fibonacci(100)
print("O centésimo termo da sequência de Fibonacci é:", resultado)
'''
 criamos um decorador memoizacao que adiciona a capacidade de memoização a uma função. 
 A função fibonacci é decorada com este decorador, permitindo cálculos eficientes de números 
 de Fibonacci.
'''

# Exercício 18: Decoradores Personalizados
print('\nExercício 18: Decoradores Personalizados\n')
import time
def calcular_tempo(funcao):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcao(*args, **kwargs)
        fim = time.time()
        print(f"A função '{funcao.__name__}' levou {fim - inicio:.4f} segundos para ser executada.")
        return resultado
    return wrapper

@calcular_tempo
def exemplo_demora():
    time.sleep(2)

exemplo_demora()
'''
criamos um decorador calcular_tempo que mede o tempo de execução de uma função e exibe o tempo 
gasto na conclusão da função.
'''


########################################### MODE GOD #############################################

################################## COMPREENDENDO ALGUNS TERMOS ###################################




