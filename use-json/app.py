''' JSON - (Javascript Object Notation) - é uma forma comum de armazenar e trocar dados 
estruturados entre sistemas. O JSON é um formato de texto leve e independente de linguagem 
de programação que é amplamente utilizado para representar objetos e dados em uma estrutura 
hierárquica. '''

# Para abri um arquivo JSON em Python
import json

with open('use-json/usuario1.json', encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json) # Converter um arquivo JSON -> String
    print(data['nome'])

with open('use-json/usuario2.json', encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json) # Converter um string JSON -> Objeto
    print(data['permissões'][1])

with open('use-json/usuario3.json', encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json)
    print(data["usuários"][0]["telefone"])
    print(data["usuários"][1]["admin"])

with open('use-json/usuario4.json', encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json)
    print(data["usuários"][0]["plano"]["preco"])

with open('use-json/usuario4.json', encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json)
    print(data["usuários"][0]["admin"])
    
# Faça mais alguns exercicios para melhorar dentro do 
# Desafio #
with open('use-json/desafio.json', encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json)
    print(data["user"][1]["email"])
    print(data["user"][0]["address"]["city"])
    print(data["user"][1]["orders"][0]["total"])


''' Como criar ou ler arquivos JSON no python '''
import json
# Criar ou ler JSON existente
print('\nCriar ou Ler JOSON existente\n')
computador_json = """ {
    "marca": "Dell",
    "preço": "15000"
} """
# String JSON
data = json.loads(computador_json)
print(data["preço"])
# Salvar um string JSON -> Arquivo JSON
with open('computador_json','w',encoding='utf-8') as arquivo_json:
    json.dump(computador_json, arquivo_json)
# Para Ler um arquivo JSON
with open('computador_json', encoding='utf-8') as arquivo_json:
    string_computador_json = json.load(arquivo_json) # Convertendo JSON -> String
    dicionario_computado_json = json.loads(string_computador_json) # Converte string em dicionario
    print(dicionario_computado_json["marca"])

# Desafio #2 - Criando JSON
print('\nDesafio #2 - Criando JSON\n')
import json
# Criar ou ler arquivo JSON existente
usuarios_json = """{
    "nome":"Jonny Dell",
    "age":"3000",
    "city":"Nova AU",
    "isStudent": true,
    "gpa": 3.5
}"""
# Salvar um string JSON -> Arquivo JSON
with open('desafio_json','w',encoding='utf-8') as arquivo_json:
    json.dump(usuarios_json, arquivo_json)


