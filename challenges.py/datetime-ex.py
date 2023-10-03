'''Como trabalhar com dados - Datetime e tempo'''
from datetime import datetime

# Para saber o horário atual
print(datetime.now()) # Momento atual completo
print(datetime.now().day) # Momento atual day (property)
print(datetime.now().month) # Momento atual month (property)
print(datetime.now().year) # Momento atual year (property)

# Criar uma data - Veja cada item e leia para entender melhor
cab_sistemas = datetime(2023, 10, 4)
print(cab_sistemas)

'''# Quero receber uma data de lançamento do meu cliente.
data_de_lancamento = input('Digite a data de lançamento: ')
print(type(data_de_lancamento)) # aparece o tipo string e não como date
print(data_de_lancamento)

# Como colocar um tipo date?
data_de_lancamento = datetime.strptime(input('Digite a data de lançamento: '), '%d/%m/%Y')
print(type(data_de_lancamento))
print(data_de_lancamento)'''


# Como calcular um intervalo entre uma data e outra?
# Definindo as datas
data1 = datetime(2023, 10, 3)
data2 = datetime(2024, 1, 1) # ou datetime.now() em uma variável
data3 = datetime.now()


# Calculando a diferença entre as datas
diferenca = data2 - data1
diferenca2 = data2 - data3

# Exibindo a diferença em dias
print(f"A diferença entre as datas é de {diferenca.days} dias.")
print(f"A diferença entre as datas é de {diferenca2.days} dias.")

