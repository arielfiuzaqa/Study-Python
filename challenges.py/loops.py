''' Aprenda a controlar o Fluxo de seus Programas através do Continue e Break

-> Continue, te permite ignorar ou pular um item dentro de um loop ou laço

-> Break, ele simplesmente interrompe a interação

Exemplos: 
'''

for numero in range(100):
    if numero % 2 == 0:
        print(numero)
    else:
        continue


frutas = ['maça', 'manga', 'laranja', 'morango']
for fruta in frutas:
    if fruta == 'manga': # vai pular a manga e continuar
        continue
    print(f'{fruta} adicionada a dieta')



for numero in range(100):
    if numero % 2 == 0:
        print(numero)
    else:
        break


frutas = ['maça', 'manga', 'laranja', 'morango']
for fruta in frutas:
    if fruta == 'manga': # assim que chegar em manga vai parar
        break
    print(f'{fruta} adicionada a dieta')



'''
- Use aoperação necessária para que a seguinte condição seja realizada

Desafio 1 - Ao chegar ao estilo "Rap" o mesmo não deve ser impresso na tela!
'''
print('\nDesafio 1\n')
estilos = ['hip-hop', 'rock', 'rap', 'pop']

for estilo in estilos:
    if estilo == 'rap':
        continue
    print(f'{estilo} adicionado a playlist.')

'''
Desafio 2 - Ao chegar ao estilo "Rock" a execução deve ser interrompida.
'''
print('\nDesafio 2\n')
for estilo in estilos:
    if estilo == 'rock':
        break
    print(f'{estilo} adicionado a playlist.')



