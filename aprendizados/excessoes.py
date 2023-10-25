''' Tratando Erros e Excessões dentro do Python - Utilizando try/except'''

# Transformando Erros em algo amigavel
try:
    meses = [1,2,3,4,5,6,7,8,9,10,11,12]
    print(meses[15])

except IndexError as erro: # Catching the error and giving a name to it.
    print('Por favor acessar um índice válido.') # Mensagem amigavel - Cliente
    print(erro) # Mensagem na integra - programador

# Finally - Execute o código mesmo com erro! Após o Erro ocorrer.
internet = None
try:
    print('Fazendo conexão com internet ' + internet)
except TypeError as erro:
    print('Não há conexão com a internet')
finally: # Ação feita após falha
    print('Desfazendo Compra')

# Outro exemplo
try:
    valor = int(input('Digite um valor: '))
    print(valor / 0)
except ZeroDivisionError as erro:
    print('Erro: Não é possível dividir por zero')
except ValueError as erro:
    print('Por favor, digitar apenas números.')
finally:
    print('Operação Finalizada!')




