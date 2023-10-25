''' Logging - Uma forma de salvar o que esta acontecendo com seu código durante um tempo,
salvando seus status na memoria para poder ver como está seu código.

Nível de Logging - Para descrever a gravidade do logging
-> debug - Só estou informando informações para os desenvolvedores. (Não exibido)
-> info - Só quero infomar algo que está acontecendo no programa, mas que não é um erro.(Não exibido)
-> warning - Quero alertar sobre algo que está acontecendo, possivelmente fora do esperado mas
ainda não se trata de um erro mas pode vir a ser futuamente.(Exibido)
-> error - Um erro que ocorreu na aplicação.(Exibido)
-> critical - Um erro com consequências graves acaba de ocorrer na aplicação.(Exibido)

° level=logging.DEBUG - Setar o nível minimo para exibir no teminal.
° filename='app.log' - Onde será guardado as informações e o nome do arquivo.
° filemode='a' - Definido para acrescentar novas linhas com o 'a'.
° format='%(levelname)s - %(message)s' - Formato que deve ser apresentado com o level e a mensagem a
ser apresentada.
'''

import logging # Para usar o módulo logging

'''logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='a', format='%(levelname)s - %(message)s') #

logging.debug('Logging nível debug.') # (Não Exibido)
logging.info('Logging nível info.') # (Não Exibido)
logging.warning('Logging nível warning.') # (Exibido)
logging.error('Logging nível error.') # (Exibido)
logging.critical('Logging nível critical.') # (Exibido)
'''


# Mantendo Histório c/ Logging e log - Utilizando as informações. (Exemplo 2)
import logging

logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='a', 
                    format='%(levelname)s - %(message)s - %(asctime)s')

try:
    email = input('Digite seu e-mail: ')
    senha = int(input("Digite sua senha bancária: "))
    if senha == 1234:  # Comparando com um número, não uma string
        print("Acesso permitido.")
        logging.info(f'{email} entrou em sua conta bancária')
    else:
        print("Acesso negado. Senha incorreta.")
except ValueError as erros: # ValueError é apenas para valores diferentes de inteiros
    print('Digite apenas números.')
    logging.error('Erro de entrada de senha: ' + str(erros))
