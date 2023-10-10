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


''' Loops aninhados - geralmente os loops usamos um unico interavel mas em alguns
casos podemos acabar tendo que usar mais de um interavel.
    Como se fosse uma lista ou uma faixa de valores por exemplo.

    Exemplo prático: Estamos criando um sistema de calendário e precisamos digitar a seguinte 
    combinação para todos os países do mundo:
    Nome do País + Estação. 

    Podemos criar uma lista com todos os países mas vamos usar 3 para exemplificar.
'''
print('\nLoops Aninhados\n')
paises = ['Brasil', 'India', 'EUA']
estacao_do_ano = ['primavera', 'verão', 'outono', 'inverno']
# Para cada pais dentro da lista paises iremos percorrer as estações do ano usando um loop for
for pais in paises:
    for estacao in estacao_do_ano:
        print(f'{pais} está na estação {estacao}.')
'''É perceptível a lógica bela desse código. 
Vai percorrer cada item pais => paises individualmente e onde cada pais => estacao e como
estacao esta para => estacao_do_ano, percorre tudo antes de voltar e pegar o segundo item 
pais => paises.
'''
# Na forma numerica do exemplo anterior
print('\nExemplo Numérico\n')
for x in range(1, 11):
    for y in range(1, 4):
        print(f'Valor externo {x} e interno {y}')

''' 🥇🥇🥇 Desafio 3 🥇🥇🥇 - Sabemos que os celulares que são lançados hoje em dia tem sempre
as versões mais simples ate as versões premium, pois bem. Vamos agora usar isso para indicar os
celulares que serao lançados no futuro.
'''
print('\nDesafio 3\n')
celulares = ['Asus', 'Sansung', 'Sony', 'IPhone']
versoes = ['Plus', 'Premium Plus', 'Premium Deluxe', 'Plus Premium Ultra']
# Percorrendo todas as posições das listas celular e versão
for celular in celulares:
    for versao in versoes:
        print(f'{celular} {versao}')


''' Interável(iterable) é um objeto que pode ser percorrido, elemento por elemento, 
usando um loop ou uma estrutura de controle de fluxo. Em outras palavras, um iterável é 
uma sequência de elementos que você pode iterar (ou seja, percorrer) um por um.

Os iteráveis são uma parte fundamental da linguagem Python e são amplamente utilizados 
em loops, compreensões de lista, funções que aceitam iteráveis como argumentos e muito mais.

Alguns exemplos de interáveis a baixo.
'''
'''Listas (Lists): Uma lista é uma sequência ordenada de elementos, e você pode iterar 
por ela usando um loop for ou outras construções de controle de fluxo.'''
print('\nList\n')
my_list = [1, 2, 3, 4, 5, 6, 7]
for item in my_list:
    print(item)

'''Tuplas (Tuples): Assim como as listas, as tuplas são iteráveis e podem ser percorridas 
da mesma forma.'''
print('\nTurple\n')
my_tuple = (10, 20, 30, 40, 50)
for item in my_tuple:
    print(item)

# Strings: As strings são sequências de caracteres e também são iteráveis.
print('\nString\n')
my_string = "Pythonista"
for char in my_string:
    print(char)

'''Dicionários (Dictionaries): Os dicionários em Python são iteráveis, mas você pode iterar 
pelas chaves, pelos valores ou pelos pares chave-valor.'''
print('\nDict\n')
my_dict = {"a": 1, "b": 2, "c": 3}
for key in my_dict:
    print(key, my_dict[key])

#Conjuntos (Sets): Os conjuntos também são iteráveis.
print('\nSets\n')
my_set = {1, 2, 3, 4, 5}
for item in my_set:
    print(item)
'''Iteradores Personalizados: 
Você pode criar seus próprios objetos iteráveis definindo uma classe que implementa 
os métodos __iter__() e __next__().'''
