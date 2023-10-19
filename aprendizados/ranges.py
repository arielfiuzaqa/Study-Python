''' Range(Geradores) - '''

'''print(type(range(30))) # Class Range
for num in range(30):
    print(num)
'''
for num in range(10, 30, 2): # Escolhendo inicio e fim da range (inicio, fim, pulos)
    print(num)

# Criar Listas Rapidamente
print('\nCriando Listas Rapidamente\n')
result = list(range(0, 201, 10)) # Criando rapidamente uma lista
print(result)

# Invertendo a sequência
print('\nInvertendo a Sequência\n')
for i in range(10, 0, -1):
    print(i)



############################### Mais Explicações sobre Range ######################################

''' A função range() em Python, embora seja uma construção fundamental na programação, pode ser 
usada em várias situações da vida real em que seja necessário criar sequências de números inteiros.

Aqui estão algumas aplicações práticas onde o range() é útil:
Gestão de Inventário: Você pode usar o range() para gerar números que representam os IDs dos 
produtos em um sistema de gerenciamento de inventário.

Contagem Regressiva: Em aplicações como temporizadores ou contadores regressivos, o range() é útil 
para gerar uma sequência decrescente.

Geração de Calendários: Para criar um calendário, você pode usar o range() para gerar os dias de 
um mês ou os meses de um ano.

Impressão e Documentação: Ao criar relatórios, você pode usar o range() para criar números de 
página ou seções.

Animações e Gráficos: Em computação gráfica e animação, o range() é usado para controlar os 
quadros ou etapas de uma animação.

Processamento de Imagens: O range() pode ser usado para iterar sobre pixels em uma imagem para 
aplicar filtros ou transformações.

Jogos e Simulações: O range() pode ser usado para controlar o tempo, os turnos ou os eventos em 
jogos e simulações.

Agendamento e Programação: Em programação, o range() é usado para criar horários, agendamentos ou 
planejamento de tarefas.

Matemática e Estatísticas: Em cálculos matemáticos, o range() pode ser usado para definir 
intervalos em equações ou criar séries de números para análises estatísticas.

Loops e Iterações: O uso mais comum é em loops, onde o range() é usado para repetir um bloco de 
código um número específico de vezes.

Construção de Sequências e Listas: Para criar listas ou sequências de números específicas, você 
pode usar o range() com a função list().

Modelagem de Dados: O range() pode ser usado na geração de números de identificação, códigos ou 
qualquer aplicação onde a sequencialidade seja necessária.

Em resumo, o range() é uma ferramenta versátil que pode ser aplicada em muitos domínios da vida 
real onde a criação, iteração ou manipulação de sequências de números inteiros é necessária. '''





