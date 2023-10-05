# First Project - Register me!
'''
Objetivo de Projeto

Estamos criando um módulo de login do nosso aplicativo, e você deve obter
as seguintes informações do funcionário

Módulo 1 - Gerar registro do funcionário

Funcionalidades do módulo 1
1. Obtenha o nome do usuário
2. Obtenha a idade do usuário
3. Registre de forma automática a data do cadastro do usuário, usando a data do
registro como data de registro.
4. Para cada novo funcionário que é registrado na empresa, ela recebe um dos seguintes
cartões, que é sorteado de forma aleatória.

cartoes = ['R$50,00', 'R$250,00', 'R$120,00',]

5. Guarde as informações sobre a data de aniversário do funcionário(dd/mm/aaaa).
'''

'''
Módulo 2 - Gerar apresentação do usuário

Funcionalidade do usuário 2 - Mensagem de boas vindas!
Usando os dados obtidos no módulo 1, exiba as seguintes informações:

1. Olá(nome do usuário), seu registro foi concluído com sucesso no 
dia(data de cadastro no formulário dd/mm/aaaa). 
    Parabéns, houve um sorteio e você ganhou um cartão de compras no 
    valor de (Valor sorteado)
'''


# Módulo 1
import random
from datetime import datetime

print('---------Olá, Bem-vindo a nossa Equipe dos Dragões Brancos-----------')
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
data_cadastro = datetime.now()
cartoes = ['R$50,00', 'R$250,00', 'R$120,00',]
cartao = random.choice(cartoes)
aniversario = datetime.strftime(input("Qual dia deseja ser seu Aniversário? "),
                               '%d/%m/%Y')
# Módulo 2 - Está dando problema na forma em que esta
print(f'Olá {nome}, seu registro foi concluído com sucesso no dia'+ 
      {data_cadastro.day}/{data_cadastro.month}/{data_cadastro.year})
print(f'Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de {cartao}')