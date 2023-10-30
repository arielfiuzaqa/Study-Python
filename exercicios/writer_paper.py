# Serve para treino de "escrita" / digitação dos conhecimentos para treinar usuabilidade!


string_de_teste = 'ariel é super foda! quero poder fazer mais. muito e muito mais'
string_de_teste2 = 'ariel É UM CARA MUITO TOP. MUITO FODA MESMO! QUERIA SER COMO ELE E ESTA COM DEUS'

testando_o_teste = string_de_teste.capitalize()
testando_o_teste2 = string_de_teste2.capitalize()

print(testando_o_teste)
print(testando_o_teste2)
print(string_de_teste.capitalize())
print(string_de_teste2.capitalize())


criando_lista = [1,2,3,4,5,6,7,8,9]
criando_outra_lista = ['a', 'b' ,'c', 'c', 'd', 'e', 'f', 'g' ,'h']

criando_outra_lista.clear()

print(criando_lista)
print(criando_outra_lista)
print(criando_lista.clear())
print(criando_outra_lista.clear())

print('\nFormat - formatadas\n')

nome = 'Vaciloun'
idade = 1001
altura = 2.55

mensagem = "Eu me chamo {} e tenho apenas {idade} e {altura} de altura, você quer levar?"
mensagem_formatada = mensagem.format(nome, altura=altura, idade=idade)

print(mensagem_formatada)
