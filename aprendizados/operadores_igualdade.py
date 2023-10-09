# Operadores de igualdade
a = 'Python'
b = 'Python'
print(a == b) # Vai comparar o valor em si
print(a is b) # Compara a identidade - referencias que estão preenchendo.
'''
Isso significa que se comparar-mos com == teremos a avaliação do conteúdo da nossa variavel mas 
se compartar-mos com 'is' vamos está comparando a tudo incluindo o endereços e espaços.
E ambos possuem endereços e espaços diferentes dentro do pc mesmo tendo o mesmo valor.

No próximo exemplo temos que uma comparação a um valor determinado dentro da mesma variável e por
isso usar o 'is' é melhor nesse caso já que estamos usando o mesmo indereço e espaço da variável.

No primeiro exemplo vai dar True e no Segundo False. É assim a melhor forma de usar.
'''
cor_preferida = None
print(cor_preferida is None)

cor_preferida = 'Azul'
print(cor_preferida is None)


# Aprenda a controlar fluxo - Como usar comparação para Converter entre tipos - 
'''Conversão de tipo
Nesse primeiro exemplo vamos ter um erro já que o input esta definido normalmente como uma string,
Podemos fazer essa mudança na própria variável idade ou dentro do print.

Já no segundo caso colocamos como o parametro correto e assim tudo deu certo! Vamos fazer pelo 
print. Assim preservamos o parametro da variável inicial.

Assim podemos mudar também transformando um numero em uma string.
'''
# Converções possíveis de Tipos - int(), str(), float(), list(), tuple(), dict() 

'''idade = input('Qual sua idade? ')
print(idade > 18)'''

idade = input('Qual sua idade?')
print(int(idade) > 18)

# Exemplo 2 - Usando tipo float

altura_parede = input('Qual é a altura da parede? ')
print(float(altura_parede) > 2.20)





