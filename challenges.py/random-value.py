# Valores aleatórios com a biblioteca random, alguns exemplos:
'''
Simular uma moeda que vai cair em cara ou coroa. Ou
Um sorteio de 1 nome em meio a uma lista de 300 nomes. Ou
Escolher aleatoriamente um numero de 1 a 100. Ou
Extrair aleatoriamente uma carta dentro de um baralho. Ou
Precisa gerar senhas aleatórias seguras. 
ETC.
'''

import random

print(random.random()) # Gera um valor de 0.0 a 1.0
print(random.uniform(4,10)) # Gera um valor decimal, mínimo e máximo
print(random.randint(1,100)) # Gera um valor inteiro, mínimo e máximo

# Vamos fazer com cores, escolhendo aleatoriamente
cores = ['vermelha', 'amarela', 'verde', 'azul', 'rosa', 'roxo', 'lilas']
escolhe_cor = random.choice(cores)
print(escolhe_cor)

print(random.choices(cores, k=2)) # Escolhe mais de um valor aleatório


'''Embaralhar valores - Ele embaralha os valores que foram dados, ou seja,
ele dar a lista novamente só que em uma sequência diferente.
'''
cartas_baralho = ['cart 1', 'cart 2', 'cart 3', 'cart 4', 'cart 5',]
print(random.shuffle(cartas_baralho)) # aplica o embaralhar
print(cartas_baralho) # Dar o resultado do embaralhamento

################################################################################################################
#​​🥇 DESAFIOS 🥇 - Desafios Random

'''1. Você quer simular a opção de jogar uma moeda e resultar em cara ou coroa
    jogue as opções dentro de uma variável e depois crie um programa que imprimir 'cara' ou 'coroa' na tela
   > Modo mais simples de fazer!!
    '''
moeda = ['cara', 'coroa']
print(random.choice(moeda))
    
'''2. Você quer fazer um sorteio entre 5 nomes em uma lista de nomes
    Crie uma lista de 5 nomes e sorteie um nome de dentro dessa lista e exiba na tela
   > Modo mais simples de fazer!!    
    '''
sorteio = ['Celio', 'Weudo', 'Titi', 'Ariel', 'Bruna', 'Jessica', 'Thaís']
print(random.choice(sorteio))



'''3. você quer escolher aleatóriamente um número de 10-100
    Imprima na tela um valor aleatório entre 10 e 100
   > Modo mais simples de fazer!! 
    '''
print(random.randint(1, 100)) # Gera um valor inteiro, mínimo e máximo



# ​​🥇​​🥇 Melhorando os desafios!! ​​🥇​​🥇

'''1. Você quer simular a opção de jogar uma moeda e resultar em cara ou coroa
    jogue as opções dentro de uma variável e depois crie um programa que imprimir 'cara' ou 'coroa' na tela
'''
escolha = input('Escolha cara ou coroa: ')
moeda = ['cara', 'coroa']
resultado = random.choice(moeda)
if (escolha == resultado): 
    print("Você ganhou!")
else:
    print(f'Você jogou {escolha} e saiu {resultado}, você errou!!')


'''2. Você quer fazer um sorteio entre 5 nomes em uma lista de nomes
    Crie uma lista de 5 nomes e sorteie um nome de dentro dessa lista e exiba na tela
'''
sorteio = ['Celio', 'Weudo', 'Titi', 'Ariel', 'Bruna', 'Jessica', 'Thaís']
print(random.choice(sorteio))



'''3. você quer escolher aleatóriamente um número de 10-100
    Imprima na tela um valor aleatório entre 10 e 100'''
print(random.randint(1, 100)) # Gera um valor inteiro, mínimo e máximo

