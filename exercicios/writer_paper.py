# Serve para treino de "escrita" / digitação dos conhecimentos para treinar usuabilidade!


print("\nFunção capitalize() - Mauscula e minuscula\n")
string_de_teste = "ariel é super foda! quero poder fazer mais. muito e muito mais"
string_de_teste2 = "ariel É UM CARA MUITO TOP. MUITO FODA MESMO!"

testando_o_teste = string_de_teste.capitalize()
testando_o_teste2 = string_de_teste2.capitalize()

print(testando_o_teste)
print(testando_o_teste2)
print(string_de_teste.capitalize())
print(string_de_teste2.capitalize())


print("\nFunção clear() - Limpar\n")
criando_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
criando_outra_lista = ["a", "b", "c", "c", "d", "e", "f", "g", "h"]

criando_lista.clear()
criando_outra_lista.clear()

print(criando_lista)
print(criando_outra_lista)
print(criando_lista.clear())
print(criando_outra_lista.clear())

print("\nFunção format() - formatadas\n")

nome = "Vaciloun"
idade = 1001
altura = 2.55

mensagem = (
    "Eu me chamo {} e tenho apenas {idade} e {altura} de altura, você quer levar?"
)
mensagem_formatada = mensagem.format(nome, altura=altura, idade=idade)

print(mensagem_formatada)

# Outro exemplo
# Definindo as variáveis
nome = "João"
idade = 30
altura = 1.80
# Criando uma string formatada
mensagem = "Olá, meu nome é {} e eu tenho {} anos. Minha altura é {} metros."
# Criando strings formatadas com base nas mesmas variáveis
mensagem1 = mensagem.format(nome, idade, altura)
mensagem2 = mensagem.format("Maria", 25, 1.65)
mensagem3 = mensagem.format("Ermanos", 99, 2.22)
# Imprimindo as strings formatadas
print(mensagem1)
print(mensagem2)
print(mensagem3)


print("\nFunção len() - Comprimento\n")

numerologia = [7777777, 1, 3]
nome_qualquer = "Vai se fuder!"

print(len(numerologia))
print(len(nome_qualquer))
print(len("Vai catar coquinho"))
print(len([50, 40, 20]))


print("\nFunção lower() - converte\n")

ruinton = "poderia tudo dar certo, MAS VOCÊ NÃO QUIS"
ruintin = "TA TUDO CERTO ATE NADA MAIS ESTA CERTO - rsrsrsrsrs"

print(ruinton.lower())
print(ruintin.lower())


print("\nFunção Criada menu()/ def - Funcionalidade\n")


def menu():
    print("Escolha uma opção: ")
    print("Opção 1")
    print("Opção 2")
    print("Opção 3")
    print("Opção 4")

    while True:
        escolha = input("Qual opção escolheu? ")

        if escolha == "1":
            print("Você escolheu a opção 1")
            break

        elif escolha == "2":
            print("Você escolheu a opção 2")
            break

        elif escolha == "3":
            print("Você escolheu a opção 3")
            break

        elif escolha == "4":
            print("Você escolheu a opção 4")
            break

        else:
            print("Opção inválida, por favor escolha uma opção.")


menu()


print("\nFunção open()  - Abrir arquivos\n")

frase = "O rato roeu a roupa do rei de Roma"
frase2 = "Pa-ro-xi-tona"
frase = "banana,maçã,uva,melancia"
frase2 = "banana.maçã.uva.melancia"

palavras = frase.split()
palavras2 = frase2.split()
frutas = frase.split(",")
frutas2 = frase2.split(".")
print(palavras)
print(palavras2)
print(frutas)
print(frutas2)


print("\nFunção strip()  - Removendo espaços em branco\n")

texto1 = "    Olá FDP    "
texto2 = "*Hoje não faro*"
texto3 = "----Hoje não faro----"

sem_espaco = texto1.strip()
sem_traco_estrela = texto2.strip("*")
sem_traco = texto3.strip("-")

print(sem_espaco)
print(sem_traco_estrela)
print(sem_traco)


print("\nFunção super()  - Atribuidos as classes pai e filha\n")


class Pai:
    def __init__(self, nome):
        self.nome = nome


class Filha(Pai):
    def __init__(self, nome, idade):
        super().__init__(nome)
        self.idade = idade


filha = Filha("Eduarda", 23)

print(filha.nome)
print(filha.idade)

# ESTUDE BEM O CASO 2
print("\nESTUDE BEM O CASO 2\n")


class Hj:
    def __init__(self, horario):
        self.horario = horario
        print(f"As horas: {horario}")


class Yuri(Hj):
    def __init__(self, horario, funcionario):
        super().__init__(horario)
        self.funcionario = funcionario
        print(f"O funcionario {funcionario} esta de folga.")


class Ariel(Yuri):
    def __init__(self, horario, funcionario, salario):
        super().__init__(horario, funcionario)
        self.salario = salario
        print(f"O valor do salario é de {salario}")


class Jorge(Ariel):
    def __init__(self, horario, funcionario, salario, recibo):
        super().__init__(horario, funcionario, salario)
        self.recibo = recibo
        print(f"Recibo. {recibo}")


# Simplesmente ativa todas as funções de todas as classes ao mesmo tempo mudando apenas os parametros de saída.
final = Jorge(15, "Tink Wink", 8000, "Recebido!")
final = Jorge(11, "Lalá", 12000, "Não Recebido!")
final = Jorge(9, "Pó", 2500, "Aguadando!")

# De Forma separda cada informação!
print(final.horario)
print(final.funcionario)
print(final.salario)
print(final.recibo)
