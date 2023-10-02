# Haverá um momento que vc vai quere separar uma string em várias partes.
frase = 'Olá, bem-vindo a este treinamento'
print(frase.split()) # vai separar em strings na tela
print(frase.split(',')) # Onde tive a virgula ira separar em strings
print(frase.split('-')) # Onde tive a o traço ira separar em strings
nomes = 'ariel, raphael, yuri, carol, amanda, bruno'
print(nomes.split())  # vai separar em strings na tela
print(nomes.split(',')) # Onde tive a virgula ira separar em strings
hashtags = 'music #guitar #gamer #coder #python'
print(hashtags.split())
print(hashtags.split('#')) # Onde tive a hashtag ira separar em strings
print(hashtags.split('#', 3)) # Onde tive a hashtag ira separar em strings ate o 3°

# Como concatenar(combinar) strings
hashtag_separadas_por_espaco = hashtags.split(' ')
print(hashtag_separadas_por_espaco) # o que temos no momento a hashtag normal
print(','.join(hashtag_separadas_por_espaco)) # Em cada um é add uma vírgula que os separa - junto
print('.'.join(hashtag_separadas_por_espaco)) # Em cada um é separado por um ponto - junto
print(' '.join(hashtag_separadas_por_espaco)) # Em cada um é separada por um espaço - junto


# Desafio 
frase1 = 'Desafio manipulação de strings'
frase2 = 'jhonatan,rafael,carol,camilla,ariel'

# ​Desafio 1: Transforme a frase1 em uma lista de palavras e guarde o resultado em uma variável chamada palavras1
palavras1 = frase1.split()
# Desafio 2: Transforme a frase2 em uma lista de palavras e guarde o resultado em uma variável chamada palavras2
palavras2 = frase2.split()
# Desafio 3: Pegue o palavras1 e transforme elas no seguinte string: "Desafio,manipulação,de,strings". Imprima o resultado no console.
print(','.join(palavras1))
# Desafio 4: Pegue o palavras2 e transforme elas no seguinte string: frase2 = "jhonatan & rafael & carol & camilla & ". Imprima o resultado no console.
print(' & '.join(palavras2))
