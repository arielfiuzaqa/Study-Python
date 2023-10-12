''' Projeto 2 - mini-game da tartaruga.
Onde devo passar os comandos para que a tartaruga ande de acordo com a pergunta.
Rudimentar mas o inicio é assim mesmo.

Otimo jogo para criar figuras geometricas como desafios

Pensando em usar uma IA para aprender a fazer várias formas geometricas O.o
'''
from turtle import Turtle
# Inicializar uma turtle
t = Turtle()
# Definir a velocidade
t.speed(1) # 0 - mais rápido, 10 - mais lento
# Movimentar a turtle
t.forward(50) # Avança em X unidades
# Rotacionar em X graus para a direita / Esquerda se usa left()
t.right(90)   # ou esquerda (360 - 90)
t.forward(100) # Avança em X unidades
# Rotacionar em X graus para a direita / Esquerda se usa left()
t.left(90) # Rotacionar em X graus para a esquerda
t.forward(100) # Avança em X unidades
# Movimentar a turtle para trás em X unidades
t.backward(200)

input() # Input ao final para evitar que ela feche quando concluir os comandos
