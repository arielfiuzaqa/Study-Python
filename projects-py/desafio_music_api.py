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

@app.route('/cancao', methods=['GET']) # Todos os itens
def obter_todas_cancoes():
    return jsonify(cancoes)


@app.route('/cancoes/<int:cancao_id>', methods=['GET']) # Item especifico
def obter_todas_cancoes():
    return jsonify(cancoes)


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
    del cancoes[cancao_id]
    return jsonify({'mensagem': 'A canção foi excluída com sucesso'})