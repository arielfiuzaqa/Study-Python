# Condicionais: Usando if / elif / else

'''Condicionais necessitam de variáveis para poder controlar o fluxo dentro do pc
Essa variáveis são as entradas e dependendo da entrada a condição do resultado muda.

Aqui vamos aplicar alguns exemplos usando o que já aprendi.

''' 

# Exemplo 01 => Vamos sair hoje? Condição: Se eu terminar o trabalho hoje, sim!
trabalho_terminado = True
if trabalho_terminado == True:
    print('Bora sair hoje!')
else: # Caso não seja verdadeiro...
    print("Não posso sair hoje!!")

# Exemplo 01 Modo Random! => Vamos sair hoje? Condição: Se eu terminar o trabalho hoje, sim!
import random
# Gere um valor aleatório (0 ou 1)
valor_aleatorio = random.randint(0, 1)
# Use o valor aleatório para determinar se o trabalho está terminado
trabalho_terminado = valor_aleatorio == 1
# Verifique a condição e imprima a mensagem correspondente
if trabalho_terminado:
    print('Bora sair hoje!')
else:
    print("Não posso sair hoje!!")

'''# Exemplo 2 - Atraso na aula, 
Condições: Caso esteja chegando atrasado pela 3° vez, não posso!
Mas se tiver 1 ou 2 vezes de atraso, recebo uma mensagem com aviso!'''
numero_atrasos = 2 # Estabelecido antes de rodar o código
if numero_atrasos >= 3:
    print ("Vá para a diretoria!")
elif numero_atrasos == 2:
    print ('Segundo atraso. Estude bem!')
elif numero_atrasos == 1:
    print('Essa é sua primeira falta. Preste atenção!')
else:
    print('Pode entrar!')

# Exemplo 2 Modo Random - Atraso na aula
import random
# Gere um número aleatório de atrasos (entre 0 e 3)
numero_atrasos = random.randint(0, 3)
# Verifique o número de atrasos e imprima a mensagem correspondente
if numero_atrasos >= 3:
    print("Vá para a diretoria!")
elif numero_atrasos == 2:
    print('Segundo atraso. Estude bem!')
elif numero_atrasos == 1:
    print('Essa é sua primeira falta. Preste atenção!')
else:
    print('Pode entrar!')

''' Exemplo 03 - Limite de velocidade
Vamos multar todos aqueles que passarem do limite de velocidade.

Velocidade máx da rua 50km/h
Cruzou entre 50km/h a 60km/h, levou multa de 2 pontos
Cruzou entre 61km/h a 75km/h, levou multa de 3 pontos
Cruzou a cima de 75km/h, levou multa de 7 pontos
'''
velocidade = 55
if velocidade <= 50:
    print('Ok')
elif velocidade >= 51 and velocidade <= 60:
    print('Multado em 2 pontos por excesso de velocidade.')
elif velocidade >= 61 and velocidade <=75:
    print('Multado em 2 pontos por excesso de velocidade.')
else:
    print('MULTADO EM 7 PONTOS POR EXCESSO DE VELOCIDADE!!!')


# Exemplo 03 Modo Random - Limite de velocidade
import random
# Gere uma velocidade aleatória (entre 30 e 80)
velocidade = random.randint(30, 80)
# Verifique a velocidade e imprima a mensagem correspondente
if velocidade <= 50:
    print('Ok')
elif velocidade >= 51 and velocidade <= 60:
    print('Multado em 2 pontos por excesso de velocidade.')
elif velocidade >= 61 and velocidade <= 75:
    print('Multado em 2 pontos por excesso de velocidade.')
else:
    print('MULTADO EM 7 PONTOS POR EXCESSO DE VELOCIDADE!!!')

''' !!! Desafio !!! - Salão de beleza - Corte de cabelo
-> Se o cabelo estiver com ou abaixo de 20cm você paga o valor de R$ 50,00
-> Se o cabelo estiver entre 21cm a 30cm você paga o valor de R$70,00
-> Se o cabelo estiver entre 31cm a 50cm você paga o valor de R$100,00
-> Se o cabelo estiver acima de 51cm consultar na recepção
'''
tamanho_cabelo = 51
if tamanho_cabelo <= 20:
    print('Pagar R$50,00')
elif 21 <= tamanho_cabelo <= 30:
    print('Pagar R$70,00')
elif 31 <= tamanho_cabelo <= 50:
    print('Pagar R$100,00')
else:
    print('Consultar a recepção, por favor!')

''' !!! Desafio Modo Random !!! - Salão de beleza - Corte de cabelo'''
import random

# Gere um tamanho de cabelo aleatório (entre 1 e 60)
tamanho_cabelo = random.randint(1, 60)

# Verifique o tamanho do cabelo e imprima a mensagem correspondente
if tamanho_cabelo <= 20:
    print('Pagar R$50,00')
elif 21 <= tamanho_cabelo <= 30:
    print('Pagar R$70,00')
elif 31 <= tamanho_cabelo <= 50:
    print('Pagar R$100,00')
else:
    print('Consultar a recepção, por favor!')


''' Exemplo 04 - Maior de idade
Casos a idade seja maior ou igual a 18 anos, essa pessoa é maior de idade,
caso contrário é menor de idade

Básico- Vamos lá!! 
Vamos fazer com que as idades sejam randomicas
'''
import random
idades = random.randint(10, 80)

if  10 <= idades <= 17:
    print("Menor de Idade não entra parceirinho!")
elif 18 <= idades <= 61:
    print('Pode entrar!!')
else:
    print('Tu vai morrer véi safado!')

# Exemplo 04 Com código mais limpo. Expressão if condição else (Forma rápida!)
idades = random.randint(10, 80)
print('Pode entrar!!') if idades >= 18 else print('Menor de Idade não entra parceirinho!')



# FAÇAMOS MAIS EXEMPLOS!! - VAMOS BUSCAR DESAFIOS MAIS DIFICEIS.








