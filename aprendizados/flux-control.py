'''
Controle de Fluxo - Para começar é necessário entender que temos alguns tipos de
operadores diferentes que requerem tratamentos diferentes, que são maneiras de
tomar decisões diferentes dentro da programação python.

Operadores Lógicos
Operadores Booleanos
Operadores Igualdade

# Comparações, o que são? São perguntas que fazemos para obter uma resposta ou resultado.

'''

'''# Vamos pensar nas seguintes operações e suas lógicas a seguir, apesar de serem
semenlhantes, eles são diferentes.

Ex: Para entrar em uma festa podemos ter 3 condições.
Melhore o código como um desafio
'''
# Situação
idade = 21
possui_convite = False
filho_dono = True
# Aceita se tiver acima ou igual a 21 anos e se tiver o convite!
print((idade >= 21) and (possui_convite == True))
# Aceita se tiver acima ou igual a 21 anos ou o Convite!
print((idade >= 21 or possui_convite == True))
# Aceita se tiver acima ou igual a 21 anos e o Convite ou ser filho do dono
print((idade >= 21 and possui_convite == True) or (filho_dono == True))
# Aceita se tiver acima ou igual a 21 anos ou o Convite ou ser filho do dono
print((idade >= 21 or possui_convite == True or filho_dono == True))



'''# Exemplo 2: Você só pode trabalhar aqui se for maior de idade e tiver carteira de
trabalho.
Situação.
'''
maior_de_idade = True
possui_carteira_de_trab = True
esta_trabalhando_atualmente = True
possui_veiculo_proprio = False
# Queremos pessoas que seja maior de idade e possuam carteira de trabalho
print(maior_de_idade == True and possui_carteira_de_trab == True)
# Queremos pessoas que ainda não possuem um veiculo, mas já tem carteira de trab.
print(possui_carteira_de_trab == True and not possui_veiculo_proprio)
print(possui_carteira_de_trab and not possui_veiculo_proprio) # mesmo ex. mas escrito diferente


'''
Desafio 1 - Uma pessoa só pode viajar se possuir passaporte e tiver passagem 
comprada e não for menor de idade.
Os dados dão as condições atuais para que se faça as comparações.
Ver um jeito de dar respostas diferentes para dar as respostas das comparações.

Dados:
'''
possui_passaport = True
passagem_comprada = True
menor_de_idade = False
print((possui_passaport and passagem_comprada) and not menor_de_idade)

