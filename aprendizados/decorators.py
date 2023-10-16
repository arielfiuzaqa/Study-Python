# Decorator - Muito importante!!! SABER DE CÔR.
'''
 Decorator é uma função que permite modificar o comportamento de outra função ou método. 
 Os decorators são amplamente usados para adicionar funcionalidades a funções ou métodos sem 
 modificar diretamente o código deles. Eles são geralmente aplicados usando o símbolo @ antes 
 da definição de uma função.
'''
# Simple exemple:
def meu_decorator(funcao):
    def wrapper(): # wrapper é qualquer nome, poderia ser qualquer outro nome
        print("Antes da função ser chamada")
        funcao()
        print("Depois da função ser chamada")
    return wrapper

#@meu_decorator # Com essa linha ativada não precisa da linha 20 e 21
def saudacao():
    print("Olá, mundo!")

result = meu_decorator(saudacao) # Linha 20
result() # Linha 21


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
    
resultado = pai(1)
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
