1. Como começar a resolver um problema complexo em programação?
R1:. Responda a pergunta. Qual é a ideia principal que estou tentando resolver?

2. Problema complexo demais para você resolver?
R2:. Quebre o problema em problemas menores. E em passos menores ainda!

3. Mito: Eu preciso saber a sintaxe ou como programar algo antes o criar.
R3:. Errado: Não foqueem saber a sintaxe exata ou como programar algo, quando estiver tentando resolver um problema, foque em enteder e definir muito bemo que deve ser resolvido no menor passo possível. Quebre problemas maiores em problemas menores.

4. Fato: Você pode aprender o que precisa, exatamente no momento em que precisar implementar aquilo em sua aplicação.
R4:. Se você seguiu os passos anteriores e quebrou um grande problema em problemas menores, então agora você deve ter uma lista de pequenos problemas que são pesquisáveis, e podem ser encontrados através de umapesquisa, artigo, video, curso, ou outro recurso para te guiar a conseguir alcançar a implementação daquela funcionalidade.

5. Mito: Não existe código perfeito.
R5:. Todos os códigos possuem algum tipo de erro ou podem ser infinitamente melhorados para sua total performance.

6. Usuário não é Programador.
R6:. As mensagens de erros devem aparecer pensando nas pessoas que são totalmente leigas, então mensagens claras que qualquer um possa entender ate uma criança. Seja direto com as mensagens e especifico para que ele possa fazer algo.

7. Como Criar Funções Limpas e Elegantes
-> Dê nomes significativos as suas funções (Fica mais fácil de identificar do que se trata)
-> Funções devem ser pequenas e fazer apenas uma coisa. (Pensando sempre em uma manuntenção futura e saber descrever a função mostra dominio)
-> Quanto menor a quantidade de argumentos melhor (Só caso necessário e no máximo 3)
-> Use funções para organizar seu código e economizar linhas de código (DRY - Don't Repeat Your-self).


8. Como Transfomar Ideias em Software?
R8:.
Passo 1: Ter uma ideia ou pegar uma ideia com alguém e anotar tudo sobre ela. Busque pegar o máximo de detalhes
Passo 2: Agora quebre sua ideia em menores passos/ partes
Passo 3: Organize e comece a trabalhar nas pequenas tarefas, uma a uma. Uso de software de organização de projeto é opcional, porém recomendado(Trello/ Note/ Bloco de Notas/ Papel e caneta) - Usando a metodologia Kanban(ToDO/Doing/Done).
Passo 4: Preencha as lacunas do conhecimento, quando necessário.
Passo 5: Publique seu projeto e acrescente ele ao seu portfólio.


9. O que são Módulos?
R9:. Módulo é um bloco de códigos reutilizável. Um arquivo python, nada mais e nada menos. Onde você pode usa-ló em várias aplicações que desejar dependendo da forma com que você crie esse módulo. São puxados da seguinte maneira
Exemplo: O "as" é opcional para dar um apelido a função
from "nome do módulo" import "nome da função" as "nf"

10. Porque eu devo usar módulos?
R10:. Para evitar conflitos entre pacotes diferentes.

11. Quando usar módulos?
R11:. Quando for preciso deixar seu código muito mais claro e fácil de entender.
1° - Separar funcionalidades relacionadas(Separando os Modulos em funcionalidades)
2° - Não acoplar o seu código(É mais fácil fazer manuntenção em um código que sei onde encontrar)
3° - Não ter uma arquivo gigante(Clear Code - Tornando tudo mais limpo e entendível)

12. Módulos VS Pacote
R12:. Um módulo é algo individual como um arquivo e possui um nome próprio, já o pacote é feito de vários módulos individuais na sua construção e seu nome tem __init__ exemplo. Isso dentro de uma pasta que comporta todos os módulos relacionados aquela identidade de pacote. Assim temos exemplo:

from imagens(nome da pasta).modulo2(nome do módulo usado) import "nome da função"

Resposta do ChatGPT
Em Python, um módulo é um arquivo que contém definições e instruções da linguagem Python. O nome do arquivo é o nome do módulo com a extensão .py anexada. Qualquer arquivo Python pode ser considerado um módulo, desde que possua definições e instruções da linguagem 1.

Por outro lado, um pacote é uma forma de estruturar o namespace do módulo Python usando “nomes de módulo pontilhados”. Basicamente, um pacote Python é um diretório que contém módulos. Para utilizar um módulo de um pacote, basta importá-lo utilizando os nomes pontilhados 1.

Em resumo, a diferença entre um pacote e um módulo em Python é que o pacote é uma coleção de módulos organizados em uma hierarquia de diretórios. O pacote é usado para organizar os módulos em subpacotes, permitindo que inúmeros módulos de mesmo nome coexistam sem interferência 1.

13. O que são ambientes virtuais?
R13:. Ambiente virtual é uma instância isolada de Python.





======================================================= Resumão =======================================================
O processo de aprendizado da programação envolve muitos conceitos, técnicas e práticas. Aqui está os pilares principais que devem ser um guia para a construção do meu aprendizado.

1° Variaveis: Como armazenar e usar informações e Aprendi os diferentes tipos de variaveis.

2° Controle de Fluxo: Para criar regras para solucionar os problemas armazenados é preciso ensinar o programa a tomar decisões atraves de regras. Baseadas em condições e comparações, bem especificas - Dominando o controle de fluxos(<, >, if, elif, else).

3° Funções: Como utilizar as funcionalidades e os codigos soltos dentro do programa, como empacotar tudo dentro de funções especificas para melhorar a legibilidade, organização e elegância.

4° Coleções: São usadas para armazenar e gerenciar múltiplos valores de dados em uma única estrutura. Elas são úteis para organizar, acessar e manipular conjuntos de elementos, como listas(list), tuplas(tuple), dicionários(dict) e conjuntos. As coleçoes facilitam a interação, pesquisa e manipulação de dados.

5° Classes: As classes servem para organizar nosso código, reutiliza-lo como comportamento, herdar e controlar propriedades, gerenciar dados e instâncias dentro do nosso código.







