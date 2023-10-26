''' Calculadora de Juros Compostos:

Peça ao usuário que insira o valor principal, taxa de juros anual e tempo.
Calcule e exiba o montante final após um determinado período. 

Solicitamos ao usuário que insira o valor principal (quantia inicial), a taxa de juros anual (em porcentagem) e o tempo em anos usando input. Os valores inseridos são convertidos em números de ponto flutuante.

Convertemos a taxa de juros anual de porcentagem para um valor decimal dividindo por 100.

Calculamos o montante final usando a fórmula de juros compostos: Montante Final = P * (1 + r) ^ n

Exibimos o montante final com duas casas decimais usando print.'''



# Solicitar ao usuário que insira o valor principal, a taxa de juros anual e o tempo em anos
valor_principal = float(input("Digite o valor principal (em reais): "))
taxa_juros_anual = float(input("Digite a taxa de juros anual (em porcentagem): "))
tempo_anos = float(input("Digite o tempo em anos: "))
# Converter a taxa de juros anual de porcentagem para decimal
taxa_juros_decimal = taxa_juros_anual / 100
# Calcular o montante final com juros compostos
montante_final = valor_principal * (1 + taxa_juros_decimal) ** tempo_anos
# Exibir o montante final
print(f"O montante final após {tempo_anos} anos é: R${montante_final:.2f}")







