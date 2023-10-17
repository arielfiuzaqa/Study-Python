''' Dicionários: É uma estrutura de dados que permite armazenar um conjunto de pares chave-valor. 
Cada elemento em um dicionário é uma associação de uma chave a um valor correspondente. 
Os dicionários são extremamente flexíveis e versáteis, tornando-os adequados para muitas tarefas, 
incluindo mapeamento de informações, contagem de ocorrências, configurações, traduções e muito mais.'''

# Criando um dicionário
pessoa = {
    "nome": "Alice",
    "idade": 30,
    "cidade": "Exemploville"
}

# Acessando valores por chave
print("Nome:", pessoa["nome"])  # Acesso ao valor da chave "nome"
print("Idade:", pessoa["idade"])  # Acesso ao valor da chave "idade"
print("Cidade:", pessoa["cidade"])  # Acesso ao valor da chave "cidade"
print(pessoa) # Acessa todos os valores em forma de dicionario
# Alterando valores - Ainda temos dessa outra forma
print('\nAlterando Valores\n')
pessoa_1 = dict(nome='Carol', idade=21, altura=1.71) # Sai na forma de dicionario ainda
print(pessoa_1)
# Dicionário(Chave, Valor)
print('\nDicinário(Chave, Valor)\n')
dict_pessoa = {"nome": "Alice","idade": 30,"cidade": "Fortalcity"}
print(dict_pessoa.keys()) # Trás apenas as chaves
print(dict_pessoa.values()) # Trás apenas os valores
print(dict_pessoa.items()) # Trás itens (chave e valores) separados por virgula (tuplas)
# Interar sobre um dicionário
print('\nInterando sobre um dicionário\n')
for item in dict_pessoa.items():
    print(item[1]) # Intera item por item - Organizado

# Grupo de Listas de Listas com caracteristicas dentro de um Dicionário


# Agrupando informações das Listas de Listas com caracteristicas dentro de um Dict



