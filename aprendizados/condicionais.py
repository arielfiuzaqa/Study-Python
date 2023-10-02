# Os condicionais em Python são usados para controlar o fluxo de execução de um programa. 
# Os condicionais mais comuns são `if`, `elif` e `else`.

# O condicional `if` é usado para executar um bloco de código se uma condição for verdadeira. 
# Por exemplo:

maior_idade = 18 # Esse é o caso estatico, a baixo esta o dinâmico
maior_idade = int(input('Digite sua idade: ')) # A função input() pede ao usuário que digite algo, 
# nesse caso.
if maior_idade >= 18:
  print("Você é maior de idade.")

#O condicional `elif` é usado para executar um bloco de código se uma condição for 
# verdadeira e todas as condições anteriores forem falsas. 
# Por exemplo:

if maior_idade >= 18:
  print("Você é maior de idade.")

elif maior_idade >= 13:
  print("Você é um adolescente.")

#O condicional `else` é usado para executar um bloco de código se todas as condições 
# anteriores forem falsas. 
# Por exemplo:

if maior_idade >= 18:
  print("Você é maior de idade.")
elif maior_idade >= 13:
  print("Você é um adolescente.")
else:
  print("Você é uma criança.")


# Outro exemplo é comparando dois valores dados pelo usuário, o que ficaria assim

primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor = input('Digite o segundo valor: ')

if int(primeiro_valor) > int(segundo_valor):
  print('O primeiro valor é maior')
else:
  print('O segundo valor é maior')
