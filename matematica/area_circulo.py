''' Calculadora de Área de um Círculo:

Solicite ao usuário que insira o raio de um círculo.
Calcule e exiba a área do círculo. 

Importamos o módulo math para acessar a constante matemática pi.

Solicitamos ao usuário que insira o raio do círculo usando input. O valor inserido é convertido em um número de ponto flutuante usando float.

Calculamos a área do círculo usando a fórmula área = pi * r²

Exibimos a área calculada com duas casas decimais usando print.'''

import math  # Importe o módulo math para acessar a constante 'pi'

# Solicitar ao usuário que insira o raio do círculo
raio = float(input("Digite o raio do círculo: "))

# Calcular a área do círculo usando a fórmula A = πr²
area = math.pi * (raio ** 2)

# Exibir a área do círculo
print(f"A área do círculo é: {area:.2f}")
