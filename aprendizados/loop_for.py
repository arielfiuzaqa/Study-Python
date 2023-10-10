'''Loop For (Laço For) - As vezes quando estamos fazendo algum tipo de processamento de dados
é possível que precise fazer a mesma ação várias vezes. Como por exemplo escrever carregando...
Mas escrever várias vezes não é a solução, existem formas melhores de se fazer isso e vou abordar
Aqui! - Através do laços de repetição, através do comando for e range, 
Isso para o número de repetições que você sabe que quer.
'''
print("Exemplo 1\n")
for numero in range(5): # for(laço), numero(), in(dentro de), range(repete tantas vezes) o codigo abaixo
    print('Carregando') # o que queremos repetir apenas
    print('Contando', numero) # O que queremos repetir mas a contagem ate acabar
'''OBS: Dentro do range eu posso escolher um intervalo de inicio e fim exemplo range(1,6) onde
nesse caso vai contar a repetição de 1 ate 5 já que começar em zero a contagem
    Temos ainda um terceito parametro do range(0,0,0) onde o terceiro se refere a como vai ser
    repetir, se vai ser de 2 em 2, 3 em 3 etc.
'''
print('\nExemplo 2\n')
for y in range(1, 21, 2): # y está representando que pode ser qualquer nome aqui que você queira
    print('Contando', y) # usamos nomes para facilitar mas não existe obrigatoriedade especifica


''' Caso Não saiba o numero de repetição que eu tenho que fazer? 
    No caso de uma Lista qualquer: Quero que repita o comando de printar cada nome ate acabar
a lista sendo que não sei quantos nomes eu tenho mas quero que todos sejam ditos.

'''
print("\nExemplo 3\n")
nomes = ["Alice", "Bob", "Carol", "David", "Eva", "Frank", "Grace", "Helen", "Igor", "Julia"]
for nome in nomes:
    print(nome) # passa por cada item de unidade, é intuitivo quando se testa


'''​🥇 Desafio 1 🥇
Usando um loop for, exiba na tela: 
Estamos em X, onde x é um valor iniciando em 18 e finalizando em 110
'''
print('\nDesafio 1\n')
for contagem in range(19, 111):
    print('Estamos em', contagem)

''' 🥇🥇 Desafio 2 🥇🥇
 Você precisa de 10 passos para finalizar uma tarefa exiba na tela: 
 Usando loop for a seguinte frase: "Explosão em X" onde X vai de 10 ate 1
'''
print('\nDesafio 2\n')
for explosao in range(1, 11):
    print('Explosão em', explosao)


print('\nDesafio 2 - Escrita de código\n')
for explosao in range(1, 11):
    print(f'Explosão em {explosao}')


'''

'''