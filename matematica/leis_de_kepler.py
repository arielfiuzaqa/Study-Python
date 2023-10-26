''' Leis de Kepler (Lei das Órbitas) 

Solicitamos ao usuário que insira o raio médio da órbita (semieixo maior) em metros e o período de revolução do planeta em segundos.

Usamos a fórmula  
para calcular a velocidade orbital, onde v é a velocidade orbital, r é o raio médio da órbita e T é o período orbital.
Exibimos a velocidade orbital com duas casas decimais usando print.'''

import math

# Solicitar ao usuário que insira o raio médio da órbita (semieixo maior) em metros
raio_medio_orbita = float(input("Digite o raio médio da órbita (em metros): "))

# Solicitar ao usuário que insira o período de revolução do planeta em segundos
periodo_revolucao = float(input("Digite o período de revolução (em segundos): "))

# Calcular a velocidade orbital usando a fórmula v = 2πr / T
velocidade_orbital = (2 * math.pi * raio_medio_orbita) / periodo_revolucao

# Exibir a velocidade orbital
print(f"A velocidade orbital é: {velocidade_orbital:.2f} metros por segundo")





