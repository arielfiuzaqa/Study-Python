from turtle import Turtle

t = Turtle()
t.speed(1)  # drawing speed fastest, slowest speeds are: 0 (very fast), 1 (fast),

# Mini-Game Turtle - Mode Normal
    # Escolhendo ir para frente
while True:
    direcao = input('Qual direção? "f:frente" ou "t:trás" ')
    if direcao == 'f':
        distancia = int(input('Quanto? '))
        mov_lado = input('Rotacionar para "d:direita", "e:esquerda" ou "n:não" rotacionar? ')
        if mov_lado == 'd':
            angulo = int(input('Quanto a direita? '))
            t.right(angulo)
        elif mov_lado == 'e':
            angulo = int(input('Quanto a esquerda? '))
            t.left(angulo)

        t.forward(distancia)
    # Escolhendo ir para trás
    if direcao == 't':
        distancia = int(input('Quanto? '))
        mov_lado = input('Rotacionar para "d:direita", "e:esquerda" ou "n:não" rotacionar? ')
        if mov_lado == 'd':
            angulo = int(input('Quanto a direita? '))
            t.right(angulo)
        elif mov_lado == 'e':
            angulo = int(input('Quanto a esquerda? '))
            t.left(angulo)

        t.forward(distancia)
    
    # Perguntar se quer Continuar andando
    resposta = input('Continuar andando? ')
    if resposta not in ('sim', 's'):
        break
