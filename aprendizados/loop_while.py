''' Loop While (Laço While): É uma estrutura de controle de fluxo que permite que você 
execute um bloco de código repetidamente enquanto uma determinada condição for verdadeira.

Ele é usado quando você não sabe antecipadamente quantas vezes precisará executar o código, 
pois a condição é verificada antes de cada iteração.

Vamos a um exemplo prático para aprender.
Imagine que você tem 3 tentativas ate bloquear sua senha, ou seja se repete ate a 3° tentativa
se tornar falsa.
'''
tentativas = 0 # declare primeiro a quantidade de tentativas inicial
while tentativas < 3: # Declaramos a condição baseada na nossa variável inicial
    print('Tente novamente')   # Bloco de Código a ser Repetido
    tentativas += 1 # incrementa a cada erro 1 a mais na nossa variável inicial
# O Código para de rodar na 3° tentativa.

# Teste de Senha. - Enquanto a senha for diferente da nossa variável não vai ter o acesso.
print('\nSenha diferente\n')
senha = ''
while senha != '123456':
    senha = input('Digite sua senha: ')
print("Bem-vindo")

# Recebendo o nome ate dar certo.
print('\nRecebendo nome.\n')
nome = ''
while nome == '':
    nome = input('Digite seu nome: ')
print(f'Bem vindo {nome}')

# Contagem Regressiva
print('\ncontagem Regressiva\n')
contador = 100
while contador >= 0:
    print(contador)
    contador -= 1

# Desafio - Jogo da Adivinhação - Numero de tentativas a seu cargo
import random

# Gerar um número secreto entre 1 e 100
numero_secreto = random.randint(1, 100)

# Inicializar as variáveis
tentativas = 0
limite_tentativas = 10
acertou = False

print("Bem-vindo ao Jogo de Adivinhação!")
print("Você tem", limite_tentativas, "tentativas para adivinhar o número secreto entre 1 e 100.")

# Começar o loop while
while tentativas < limite_tentativas:
    # Solicitar a entrada do jogador
    palpite = int(input("Tentativa " + str(tentativas + 1) + ": Digite sua adivinhação: "))

    # Verificar se o palpite está correto
    if palpite == numero_secreto:
        print("Parabéns! Você acertou o número secreto:", numero_secreto)
        acertou = True
        break
    elif palpite < numero_secreto:
        print("Tente novamente. O número secreto é maior.")
    else:
        print("Tente novamente. O número secreto é menor.")

    # Incrementar o contador de tentativas
    tentativas += 1

# Verificar se o jogador não acertou após todas as tentativas
if not acertou:
    print("Suas", limite_tentativas, "tentativas acabaram. O número secreto era:", numero_secreto)












#🥇 DESAFIOS🥇

'''DESAFIO 1 - Crie um loop while que irá contar e imprimir no console de 1 até 120'''

'''DESAFIO 2 - Crie um loop while que irá continuamente pedir ao usuário a senha para 
entrada, e só irá permitir o programa continuar caso ele digite a senha 'secreto'''

''' DESAFIO 3 - Crie um loop que conte e imprima na tela o valor em ordem descrescente 
de 100 para 1'''
