''' Lista de Tarefas Simples!! 
    Com as opções: 
        1 - Adicionar, 
        2 - Atualizar, 
        3 - Deletar e 
        4 - Visualizar'''

tarefas = [] # 1° Lista de Tarefas - com valor vazio

# Adicionando Tarefa - append( )
# Loop While - Assim podemos sempre adicionar mais. Por isso precisamos de um loop
while True:
        # Criar uma variável para receber os inputs e guardar essa informação
        item = str(input('Item: ')).strip() # strip( ) remove os espaços
        tarefas.append(item) # Adicionamos a tarefa na nossa lista de tarefas o que foi dado no input
        # Parando o loop de adição sem parar.
        continuar = str(input('Deseja continuar? [S/N]\n: ')).upper()[0]
        if continuar == 'N':
            break
        elif continuar == 'S':
            continue
        else:
            print('\33[4;32mOpção Inválida!\33[m')
            break

# Atualizar

# Excluir

# Visualizar
            
# Mostrando itens de forma mais organizada
contador = 0
for item in tarefas:
    print(contador," - " , item, end='\n')
    contador += 1

