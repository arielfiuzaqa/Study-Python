import sqlite3

with sqlite3.connect("artistas.db") as conexao:
    # Criar uma conexão com o banco de dados
    sql = conexao.cursor()
    # Rodar comando SQL - Criando estrutura
    sql.execute(
        "create table if not exists banda(nome text, estilo text, membros integer);"
    )
    # Exemplo de inserir dados
    sql.execute(
        "insert into banda(nome, estilo, membros) values ('The Beatles', 'Rock', 4)"
    )
    # Exemplos de usar dados da minha aplicação em um comando SQL
    nome = input("Digite o nome da banda")
    estilo = input("Digite o estilo da banda")
    quantidade_integrantes = int(input("Quantidade de integrantes da banda"))

    sql.execute(
        "insert into banda values(?,?,?)", [nome, estilo, quantidade_integrantes]
    )
    # Salavando alteração no banco de dados
    conexao.commit()

    # Exibir dados no console python(terminal)
    sql.execute("select * from banda;")
    for banda in bandas:
        print(banda)
