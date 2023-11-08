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

13. Como usar o if__name_ == '__main__' ?
É usado em Python para determinar se um arquivo Python está sendo executado como um programa principal ou se está sendo importado como um módulo em outro programa. Isso é útil quando você deseja separar o código que deve ser executado quando o arquivo é o programa principal do código que é apenas reutilizável em outros lugares.

O bloco if __name__ == '__main__': é seguido pelo código que você deseja executar quando o arquivo é o programa principal. 

14. Pypi - Encontre bibliotecas para seu projeto (https://pypi.org/)

15. Como gerenciar os pacotes da nossa máquina local?
R15:.
1° Usamos o pip list no cmd para listar todos os pacotes/ módulos que temos instalados em seu pc
2° Depois de verificar que o pacote não esta instalado, instale o pacote com o pip instal <modulo/pacote>
3° Caso queira atualizar seria melhor fazer um pip unistall <biblioteca> e depois o pip install <biblioteca>
4° Para instalar versões especificas de um módulo com isso basta pip install <modulo>==<versão>
OBS: 8 Conteúdo aula 9 sobre publicação no pypi

16. O que são ambientes virtuais(venv)?
R16:. Ambiente virtual é uma instância isolada de Python. Capacidade de isolar as depedências que cada projeto possui, assim cada ambiente vai depender de dependências e módulos diferentes sem um interferir no outro.

Para iniciar deve abri o powersell e digitar o comando Set-ExecutionPolicy Unrestricted -Force -> Esse comando cria um ambiente virtual.

Entre no local onde quer executar o venv e digite python -m venv <Nome a sua escolha> - Após criar aperte ls para verificar que foi realmente criado o venv.

Para ativar o ambiente virtual para fazer as instalações apenas dentro dele, use .\pasta onde esta o venv\Scripts\activate - Para saber se esta no venv pasta ver o nome do seu venv na linha. Usando o pip lista vai verificar que tem poucas bibliotecas que é o que queriamos ver dentro do venv, assim podemos instalar apenas as que são necessárias para o projeto.

Siga as sugestões que vão aparecer para deixar o ambiente pronto para ser usado de atualização do pip 
python -m pip install --upgrade pip 

Você também pode desinstalar as bibliotecas que quiser, e quando for colocar o projeto para a nuvem é importante de diga as bibliotecas e versões que você usou para criar. E uma forma de fazer isso é usando o comando pip freeze > requirements.txt

Agora queremos voltar ao ambiente global, basta sair do venv usando deactivate + enter

Para poder instalar todas as bibliotecas de um projeto devemos instalar todas as bibliotecas no requirements.txt de uma vez só utilizando pip install -r .\requiremente.txt


17. Por que usar um Ambiente virtual(venv)?
R17:. O Ambiente virtual permite que você possa usar apenas os recursose bibliotecas que você possa precisar


18. Refatoração?
R18:. refere-se ao processo de reestruturar o código-fonte de um programa, alterando sua estrutura interna ou organização, sem modificar seu comportamento externo. O objetivo da refatoração é melhorar a qualidade do código, tornando-o mais legível, manutenível e eficiente, sem alterar sua funcionalidade.

ctrol + shift + r entra na forma de criar uma class para poder usar o código que você selecionou como uma função.

ctrol + shift + r selecionando Extract Variable conseguimos criar um method/ variavel para alguma formula.

Muito bom e muito útil de ser utilizado.


19. APIs - Um universo de possibilidades
R19:.  São conjuntos de regras e protocolos que permitem que diferentes componentes de software se comuniquem entre si. Uma API define os métodos e estruturas de dados disponíveis para interação com uma biblioteca, serviço, aplicativo ou plataforma externa. As APIs desempenham um papel fundamental na integração de sistemas e no desenvolvimento de software, permitindo que desenvolvedores acessem funcionalidades específicas sem precisar entender a complexidade interna dessas funcionalidades.

Utilizadas como:

> Módulos e Bibliotecas: fornecidas por meio de módulos ou bibliotecas. Um módulo é um arquivo Python que contém funções, classes e variáveis que podem ser importadas e usadas em outros programas. As bibliotecas são coleções de módulos relacionados que fornecem funcionalidades específicas. Por exemplo, a biblioteca requests oferece uma API para fazer solicitações HTTP.

> RESTful APIs: As APIs RESTful (Representational State Transfer) são um tipo comum de API que segue princípios de design específicos. Elas usam os métodos HTTP (como GET, POST, PUT e DELETE) para realizar operações em recursos, que são representados por URLs. As APIs RESTful são frequentemente usadas em serviços da web.

> JSON e XML: As APIs frequentemente trocam dados em formatos como JSON (JavaScript Object Notation) ou XML (eXtensible Markup Language). Esses formatos são usados para serializar dados de forma que possam ser transmitidos entre sistemas.

> Documentação de API: Boas APIs geralmente vêm com documentação que descreve como usá-las, incluindo uma lista de endpoints, métodos disponíveis e exemplos de solicitações e respostas.

> Chaves de API: Alguns serviços que fornecem APIs requerem que os desenvolvedores obtenham uma chave de API (API key) para autenticação. Essa chave é usada para identificar o desenvolvedor e controlar o acesso à API.

> Uso de APIs em Python: Para usar uma API em Python, os desenvolvedores normalmente fazem solicitações HTTP usando bibliotecas como requests. Os dados da resposta podem ser processados e utilizados em seus programas.

> Exemplos de APIs em Python: Existem APIs disponíveis para uma variedade de finalidades em Python, como acesso a serviços da web (por exemplo, a API do Twitter), integração de bancos de dados, automação de tarefas, aprendizado de máquina e muito mais.

Toda API possui 4 Partes Básicas

1 - URL BASE (http://dummy.restapiexample.com/)
2 - ENDPOINT (O que vem depois da url base /exemplo1 , /exemplo2, etc)
3 - RECURSO (Tudo que é retornado da api que considerado como recurso ou resource)
4 - VERBOS HTTP (GET/ POST/ PUT/ DELETE - O que o resource usa para se comunicar)
    GET - Obter dados existentes
    POST - Enviar dados
    PUT - Atualizar os dados
    DELETE - Excluir os dados

STATUS CODE (números identificadores que nos ajudam a ler e identificar se esta ou não funcionando)
    1xx: INFORMAÇÃO - Informações sobre processamento em andamento
    2xx: SUCESSO - A requisição foi bem sucedida
    3xx: REDIRECIONAMENTO - Requisição redirecionada
    4xx: ERRO DO CLIENTE - Erro no lado do cliente
    5xx: ERRO SERVIDOR - Erros no servidor

Ou Seja, as APIs são formadas por URL BASE + ENDPOINT
Já o que recebemos dela é chamado de RECURSO -> RESOURCE
E a forma como ele se comunica é através dos verbos HTTP

    APIs RESTFUL
- Stateless - Sem estado
- Cliente-servidor - Clien-server
- Cacheable - Capaz de armazenar informações temporárias
- Layered system - Sistema em camadas
- Code on demand - Código na demanda
- Uniform interface - Interfase uniforme
- Resource identification - Identificação de recursos
- Manipulation of resources through representations - Manipulação de recursos através de representações
- Self-descriptive messages - Mensagens auto-descritivas
- Hypermedia as the engine of application state - Mídia hipermédia como mecanismo de estados de aplicativos


20. Onde encontrar API's Oficiais e Não Oficiais?
R20:. Por que ter? Para poder ter a chance de fazer vários projetos diferentes e desenvolver integrações diferenciadas.
-> https://github.com/realpython/list-of-python-api-wrappers  (Várias API's) - ​APIs que possuem documentação em Python.

-> https://github.com/public-apis/public-apis (Lista de API's públicos)

-> https://github.com/n0shake/Public-APIs  (Lista de API's públicos)

-> https://github.com/search?q=api+list&type=Repositories  (Lista de API's públicos)

E para encontrar API's não oficiais basta entrar no google e pesquisar assim: <conteundo que quero> unnofficial api. Com isso vai encontrar vários diferentes. 

Use para os exercicios https://jsonplaceholder.typicode.com/

Dois grandes players na criação de API
Django(Framework completo) e Flask(Micro-framework)

Flask Restful: Biblioteca extra - Quem é mais avançado pode usar.

Flask: 



21. 
R21:. 

======================================================= Resumão =======================================================
O processo de aprendizado da programação envolve muitos conceitos, técnicas e práticas. Aqui está os pilares principais que devem ser um guia para a construção do meu aprendizado.

1° Variaveis: Como armazenar e usar informações e Aprendi os diferentes tipos de variaveis.

2° Controle de Fluxo: Para criar regras para solucionar os problemas armazenados é preciso ensinar o programa a tomar decisões atraves de regras. Baseadas em condições e comparações, bem especificas - Dominando o controle de fluxos(<, >, if, elif, else).

3° Funções: Como utilizar as funcionalidades e os codigos soltos dentro do programa, como empacotar tudo dentro de funções especificas para melhorar a legibilidade, organização e elegância.

4° Coleções: São usadas para armazenar e gerenciar múltiplos valores de dados em uma única estrutura. Elas são úteis para organizar, acessar e manipular conjuntos de elementos, como listas(list), tuplas(tuple), dicionários(dict) e conjuntos. As coleçoes facilitam a interação, pesquisa e manipulação de dados.

5° Classes: As classes servem para organizar nosso código, reutiliza-lo como comportamento, herdar e controlar propriedades, gerenciar dados e instâncias dentro do nosso código.

====================================================================================================================
Aulas Muito importantes

Capitulo 8 - aula 9 - Como PUBLICAR SEU pacote para Pypi
Capitulo 8 - aula 10 - Venv - Criando um ambiente virtual

Capitulo 9 - aula 8 - Get (Obter recurso) e como criar uma API
Capitulo 9 - Completo

