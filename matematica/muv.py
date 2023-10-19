''' Movimento Uniformemente Acelerado (MUA)
Solicitamos ao usuário que insira a velocidade inicial, a aceleração e o tempo em segundos.

Usamos a fórmula v_final = v_inicial + at * t
Exibimos a velocidade final com duas casas decimais usando print.
'''

# Solicitar ao usuário que insira a velocidade inicial, a aceleração e o tempo
velocidade_inicial = float(input("Digite a velocidade inicial (m/s): "))
aceleracao = float(input("Digite a aceleração (m/s²): "))
tempo = float(input("Digite o tempo (s): "))

# Calcular a velocidade final usando a fórmula Vf = Vi + at
velocidade_final = velocidade_inicial + (aceleracao * tempo)

# Exibir a velocidade final
print(f"A velocidade final é: {velocidade_final:.2f} m/s")
