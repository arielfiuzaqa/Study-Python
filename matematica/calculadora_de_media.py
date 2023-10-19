''' Calculadora de Média:

Solicite ao usuário que insira uma lista de números.
Calcule e exiba a média desses números.

Solicitamos ao usuário que insira uma lista de números separados por vírgulas. 
O input captura a entrada do usuário como uma string.

Usamos split(',') para dividir a string de entrada em uma lista de números. 
A função float é usada para converter cada número em um número de ponto flutuante.

Verificamos se a lista de números não está vazia. Se estiver vazia, exibimos uma 
mensagem informando que a lista está vazia.

Se a lista não estiver vazia, calculamos a média dos números somando todos os números e 
dividindo pelo número de elementos na lista. A média é então exibida.'''

# Solicitar ao usuário que insira uma lista de números separados por vírgulas
entrada = input("Digite uma lista de números separados por vírgulas: ")

# Dividir a entrada em uma lista de números
numeros = [float(numero) for numero in entrada.split(',')]

# Verificar se a lista de números não está vazia
if len(numeros) == 0:
    print("A lista de números está vazia.")
else:
    # Calcular a média dos números
    media = sum(numeros) / len(numeros)
    print(f"A média dos números é: {media}")



# Melhore em uma versão 2




