''' Como criar e modificar arquivos: 
    'r' -> Usado somente para ler algo
    'w' -> Usado somente para escrever algo
    'r+' -> Usado para ler e escrever algo 
    'a' -> Usado para acrescentar algo '''

import os

with open('celulares.txt', 'w') as arquivo:
    arquivo.write('Celular 2')

with open('nomes.txt', 'a', newline='') as arquivo:
    arquivo.write('amanda' + os.linesep)

# Caso precise escrever numeros devemos está transformando eles em string primeiro
numeros = [0,1,2,3,4,5,6,7,8,9]
with open('numeros.txt', 'a', newline='') as arquivo:
    for numero in numeros:
        arquivo.write(str(numero) + os.linesep) # Convertendo para int para string
    

# Agora vamos ler os nomes dentro dos arquivos
with open('nomes.txt','r') as arquivo:
    for linha in arquivo:
        print(f"Nome: {linha}")

# Agora vamos ler nomes dentro do arquivo e acrecentar algo
with open('numeros.txt','r+') as arquivo:
    for linha in arquivo:
        print(linha)
    arquivo.write('10000')



''' 🥇DESAFIO Manipulação de Arquivos🥇


Veja o desafio, tente fazer por conta própria e depois veja a solução que estou passando aqui

# Primeiro crie 3 listas

 * Uma lista que contem 5 frutas

 * Uma lista que contem 5 cores

 * Uma lista que contem 5 linguagens de programação

# Desafio 1 - Crie um novo arquivo chamado frutas.txt e insira dentro dele todos as 5 frutas 
que estão na lista de frutas
# Desafio 2 - Imprima na tela todas as linhas que estao dentro do arquivo frutas.txt
# Desafio 3 - Sem apagar os dados que já estão dentro de frutas.txt, adicione todas as cores 
que estão dentro da sua lista de cores ao arquivos frutas.txt
# Desafio 4 - Crie um novo arquivo chamado 'Top 5 Linguagens.txt' e popule o arquivo, de forma 
com que cada linuguagem ocupe apenas uma linha.
# BONUS - Como você poderia criar vários arquivos diferentes usando um laço for e strings 
dinâmicos(f'{}'), e também não escrever nada dentro deles?
'''

# Criando as listas
frutas = ['banana', 'laranja', 'melancia', 'abacate', 'morango']
cores = ['azul', 'verde', 'branco', 'preto', 'cinza']
linguagens = ['python', 'java', 'javascript', 'php', 'ruby']

with open('frutas.txt','w',newline='') as arquivo:
    for fruta in frutas:
        arquivo.write(f"{fruta}{os.linesep}")

# Imprima na tela todas as linhas que estão dentro do arquivo frutas.txt
with open('frutas.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha)

# Sem apagar os dados dentro de frutas.txt adicione todas as cores
with open('frutas.txt', 'a') as arquivo:
    for cor in cores:
        arquivo.write(cor + os.linesep)

# Crie um novo arquivo chamado 'Top 5 Linguagens.txt' faça uma linha ter todas as informaçoes
with open('Top 5 Linguagens.txt', 'w', newline='') as arquivo:
    for linguagem in linguagens:
        arquivo.write(linguagem + os.linesep)

# Como poderia criar vários arquivos vazios, usando um laço for?
arquivos = ['music.mp3', 'foto.jpg', 'senhas.txt', 'relatorio.pdf']
for arquivo in arquivos:
    with open(f'{arquivo}', 'w') as arquivo:
        pass

