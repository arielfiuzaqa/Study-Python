''' Conversor de Temperatura:

Peça ao usuário que insira uma temperatura em graus Celsius.
Converta e exiba a temperatura em graus Fahrenheit.

Solicitamos ao usuário que insira a temperatura em graus Celsius usando input. O valor inserido 
é convertido em um número de ponto flutuante usando float.

Realizamos a conversão da temperatura de graus Celsius para graus Fahrenheit usando a fórmula 
F = C * 9/5 + 32, onde F é a temperatura em Fahrenheit e C é a temperatura em

Exibimos a temperatura convertida em graus Fahrenheit com duas casas decimais usando print.'''

# Solicitar ao usuário que insira a temperatura em graus Celsius
celsius = float(input("Digite a temperatura em graus Celsius: "))

# Realizar a conversão de Celsius para Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Exibir a temperatura em graus Fahrenheit
print(f"A temperatura em graus Fahrenheit é: {fahrenheit:.2f}")


# Crie um nivel 2 da Logica para aplicar




