# Recebendo dados do usuário. Para poder salvar ao input recebido é preciso
# esta como uma variável
senha = input('Digite sua senha: ') # incere um input
print(f'Senha digitada foi {senha}') # mostra a senha com uma string antes.
print(type(senha)) # diz o tipo que está dentro do input()

# Se precisar de um tipo(type) diferente vc tem que incerir antes do input
qtd_de_filmes = input('Quantos filmes você já viu esse mês?')
print(type(qtd_de_filmes))
# Incerindo com tipo int - Mas isso só converte de forma mecânica o tipo
qtd_de_filmes = int(input('Quantos filmes você já viu esse mês?'))
print(type(qtd_de_filmes))

