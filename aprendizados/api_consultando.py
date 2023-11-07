# Como usar 4 principais comandos(verbos) de uma API

import requests # Para importar e visualizar melhor os requests da API
from pprint import pprint

# Comando GET: Obtém informações do servidor.
resultado_get = requests.get('https://jsonplaceholder.typicode.com/todos')
#pprint(resultado_get.json())

# Get com id - Obter recurso único
print('\nGet com id\n')
resultado_get_id = requests.get('https://jsonplaceholder.typicode.com/todos/2')
pprint(resultado_get_id.json())

# POST - Criar um novo recurso
print('\nPOST - Criar um novo recurso\n')
nova_tarefa = {'completed': False,
                'title': 'Lavar a moto',
                'userId': 1}

resultado_post = requests.post('https://jsonplaceholder.typicode.com/todos', nova_tarefa)
pprint(resultado_post.json())

# PUT - Alterar um recurso existente
print('\nPUT - Alterar um recurso existente\n')
alterando_tarefa = {'completed': False,
                'title': 'Lavar o Avião',
                'userId': 1}
resultado_put = requests.put('https://jsonplaceholder.typicode.com/todos/2', alterando_tarefa)
pprint(resultado_put.json())

# DELETE - Excluir um recurso
print('\nDELETE - Excluir um recurso\n')
resultado_delete = requests.delete('https://jsonplaceholder.typicode.com/todos/2')
pprint(resultado_delete.json())

# Tudo certo, vamos ao postman
