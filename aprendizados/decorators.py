# Decorator - Muito importante!!! SABER DE CÔR.
'''
 Decorator é uma função que permite modificar o comportamento de outra função ou método. 
 Os decorators são amplamente usados para adicionar funcionalidades a funções ou métodos sem 
 modificar diretamente o código deles. Eles são geralmente aplicados usando o símbolo @ antes 
 da definição de uma função.
'''
# Simple exemple:
print('\nSimple Exemple\n')
def meu_decorator(funcao):
    def wrapper(): # wrapper é qualquer nome, poderia ser qualquer outro nome
        print("Antes da função ser chamada")
        funcao()
        print("Depois da função ser chamada")
    return wrapper

@meu_decorator # Com essa linha ativada não precisa da linha 20 e 21
def saudacao():
    print("Olá, mundo!")

saudacao()


# Exemple 2: 
print('\nExemplo 2 - Depositando dinheiro\n')
from datetime import datetime
def depositar_dinheiro():
    print('Depositando Dinheiro')

    def depositando_dolar():
        print('Depósito em Dolar Realizado.')

    def depositando_reais():
        print('Depósito em Reais Realizados.')

    depositando_dolar()
    depositando_reais()

depositar_dinheiro()
'''
Com isso não tenho como chamar as funções porque já fazem parte de outra função.
'''

# Exemple 3: Podemos retornar uma referencia de funções
print('\nExemple 3\n')
def pai(numero):
    def filho_1():
        print('Sou filhos 1')
    def filho_2():
        print('Sou filho 2')
    if numero == 1:
        return filho_1
    elif numero == 2:
        return filho_2
    
resultado = pai(2)
resultado() # Só pode executar se eu passo o parametro para a variavel resultado

# Exemple 4: 
from datetime import datetime
print('\nExemple 4\n')
def imp_hora(horario):
    def hora():
        print(datetime.now().strftime('%H:%M:%S'))
        horario()
        print(datetime.now().strftime("%d:%m:%Y"))
    return hora
@imp_hora
def ponto():
    print("Ponto registrado")

ponto()

# Exercicio 01 - Area do Retângulo #
print('\nExercicio #01 - Area do Retângulo\n')
def validar_numeros_positivos(f):
    def validacao_area(largura, altura):
        if largura <= 0 or altura <= 0:
            raise ValueError("A largura e a altura devem ser números positivos.")
        return f(largura, altura)
    return validacao_area

@validar_numeros_positivos
def calcular_area_retangulo(largura, altura):
    return largura * altura
# Inputs da largura e altura do retângulo
largura = float(input("Digite a largura do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))
# Calculo e resultado da área
area = calcular_area_retangulo(largura, altura)
print(f"A área do retângulo é {area}")

# Exercicio #02 - Volume de um cubo
print('\nExercicio #02 - Volume de um Cubo\n')
def calcular_volume_do_cubo(lado):
    if lado <= 0:
        raise ValueError("O lado do cubo deve ser um número positivo.")
    volume = lado ** 3
    return volume

try:
    lado = float(input("Digite o comprimento de um lado do cubo: "))
    volume = calcular_volume_do_cubo(lado)
    print(f"O volume do cubo é {volume}")
except ValueError as e:
    print(f"Erro: {e}")

# Exercicio #03 - Volume do Paralelepipedo
print('\nExercicio #03 - Volume do Paralelepipedo\n')
def calcular_volume_do_paralelepipedo(comprimento, largura, altura):
    if comprimento <= 0 or largura <= 0 or altura <= 0:
        raise ValueError("Os tamanhos devem ser números positivos.")
    volume = comprimento * largura * altura
    return volume

try:
    comprimento = float(input("Digite o comprimento: "))
    largura = float(input("Digite a largura: "))
    altura = float(input("Digite a altura: "))
    volume = calcular_volume_do_paralelepipedo(comprimento, largura, altura)
    print(f"O volume do paralelepípedo é {volume}")
except ValueError as e:
    print(f"Erro: {e}")



