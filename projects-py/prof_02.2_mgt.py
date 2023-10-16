'''Melhorando o arquivo prof_02_mgt.py (Mini-game da Turtle) - Usando decorators. Diminuindo numero
de repetições e deixando o chamado "clean code"
Como fazer? Primeiro se perguntar é: O que esta sendo repetido?
Segundo é: Como poderia transformar isso em uma função?'''
from turtle import Turtle

t = Turtle()
t.speed(1)  # drawing speed fastest, slowest speeds are: 0 (very fast), 1 (fast),
# Função da distância
def obter_distancia():
    resposta = int(input('Quanto? '))
    return resposta
# Função da Rotação da Turtle
def rotacionar_turtle(turtle):
    mov_lado = input('Rotacionar para "d:direita", "e:esquerda" ou "n:não" rotacionar? ')
    if mov_lado == 'd':
        rotacionar_right(turtle)
    elif mov_lado == 'e':
        rotacionar_left(turtle)
# Função Rotacionar para Direita
def rotacionar_right(turtle):   
    angulo = int(input('Quanto a direita? '))        
    t.right(angulo)
# Função Rotacionar para Esquerda
def rotacionar_left(turtle):
    angulo = int(input('Quanto a esquerda? '))
    t.left(angulo)
# Mini-Game Turtle - Mode Normal
while True:
    # Escolha da opção f:frente ou t:trás
    direcao = input('Qual direção? "f:frente" ou "t:trás" ')
    # Direção frente
    if direcao == 'f':
        distancia = obter_distancia()
        rotacionar_turtle(t)
        t.forward(distancia)
    # Direção trás
    if direcao == 't':
        distancia = obter_distancia()
        rotacionar_turtle(t)
        t.backward(distancia)
    # Perguntar se quer Continuar andando
    resposta = input('Continuar andando? ')
    if resposta not in ('sim', 's'):
        break
