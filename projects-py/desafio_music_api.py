from flask import Flask, jsonify, request

app = Flask(__name__)

cancoes = [
    {
        'cancao': 'cancao 1',
        'estilo':  'hip-hop'
    },
    {
        'cancao': 'cancao 2',
        'estilo':  'rock and roll'
    },
    {
        'cancao': 'cancao 3',
        'estilo':  'classic'
    },
    {
        'cancao': 'cancao 4',
        'estilo':  'pop'
    }
]

@app.route('/cancoes', methods=['GET']) # Todos os itens http://localhost:5000/cancoes
def obter_todas_cancoes():
    return jsonify(cancoes)


@app.route('/cancoes/<int:cancao_id>', methods=['GET']) # Item especifico http://localhost:5000/cancoes/1
def obter_todas_por_id(cancao_id):
    return jsonify(cancoes[cancao_id])

@app.route('/cancoes', methods=["POST"]) # ADD Nova canção
def nova_cancao():
    cancao= request.get_json()
    cancoes.append(cancao)
    return jsonify(f'A {cancao} adicionada com sucesso', 201)

@app.route('/cancoes/<int:cancao_id>', methods=['PUT'])
def atualizar_campo(cancao_id):
    cancao_alterada = request.get_json()
    cancoes[cancao_id].update(cancao_alterada)
    return jsonify(cancoes[cancao_id],200)


@app.route('/cancoes/<int:cancao_id>', methods=['DELETE'])
def remover_cancao(cancao_id):
    try:
        del cancoes[cancao_id]
        return jsonify({'mensagem': 'A canção foi excluída com sucesso'})
    except:
        return jsonify('Não foi encontrado uma canção com este id', 404)
    
app.run(port=5000, host='localhost', debug=True)