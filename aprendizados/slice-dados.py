# Como receber e trabalhar com dados?

#  Outra forma de se trabalha é utiliza a indexão onde selecionamos uma parte da variável
teclado = 'Teclado'
print (teclado[-1]) # imprime o caractere na posição 8
print(teclado.index('l')) # mostra em que posição está a letra l 
print(teclado[teclado.index('l')]) # agora ele vai imprimir na tela o l caso encontre.

link = 'facebook.com/devaprender'
print(link[0]) # Primeiro item dentro de uma string
print(link[-1]) # último string
print(link[0:5]) # Pegamos parte de um string pegando onde ele começa e termina
print(link[0:]) # inicia e vai ate o final
print(link[-5:]) # de tras para frente, então volta 5 indeces
print(link[5:]) # Começa no 5 e vai ate o final
print(link[:-5]) # Que que inicie do zero ate os ultimos -5

# Em alguns casos eu quero acessar a ultima informação/ caracter repetido.
frase = 'Clean Code'
print(frase.rindex('C'))

# DESAFIO 1 🥇
# Desafio 1 Encontre o índice de 'o' dentro da variável biblioteca
biblioteca = 'Biblioteca'
print(biblioteca.index('o'))

# Desafio 2
# Usando a frase
frase = 'Desenvolvimento De Aplicações'
# Imprima apenas 'De Aplicações'
print(frase[16:])
print(frase[16:29])
print(frase[-13:])
# também podemos fazer assim. Que é o melhor para se utilizar na pratica real.
indece_d = frase.rindex('D')
indece_s = frase.rindex('s')
print(frase[indece_d:indece_s+1])
