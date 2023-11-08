from flask import Flask, jsonify, request

# Defina o objetivo da api - Nesse Caso é um blog, onde posso: Consultar, editar, criar e excluir postagens usando api

app = Flask(__name__) # Instanciando o flask
postagens = [
    {
        'titulo': 'Minha História',
        'autor': 'Amandinha'
    },
    {
        'titulo': 'Viagem ao Sol',
        'autor': 'Ariel Gold'
    },
    {
        'titulo': 'O melhor',
        'autor': 'Célio'
    }
]

# Rota padrão - GET http://localhost:5000/
@app.route('/')
def obter_postagens():
    return jsonify(postagens)

# GET com Id - GET http://localhost:5000/postagem/2
@app.route('/postagem/<int:id>',methods=['GET']) # Colocando o tipo e onde buscar
def obter_postagem_por_indice(id):
    return jsonify(postagens[id])

# POST - Criando uma nova postagem - http://localhost:5000/postagem
@app.route('/postagem', methods=['POST'])
def nova_postagem():
    postagem = request.get_json()
    postagens.append(postagem)

    return jsonify(postagem, 200)

# PUT - Alterar uma postagem existente (Alterar 1) - http://localhost:5000/postagem/0
@app.route('/postagem/<int:indice>', methods=['PUT'])   
def alterar_postagem(indice):
    postagem_alterada = request.get_json()
    postagens[indice].update(postagem_alterada)

    return jsonify(postagens[indice], 200)

# DELETE - Excluir uma postagem - http://localhost:5000/postagem/0
@app.route('/postagem/<int:indice>', methods=['DELETE'])
def excluir_postagem(indice):
    try:
        if postagens[indice] is not None:
            del postagens[indice]
            return jsonify(f'Foi excluido com sucesso {postagens[indice]}', 200)
    except:
        return jsonify('Não foi possível encontrar a postagem para exclusão', 404)

app.run(port=5000, host='localhost', debug=True)

