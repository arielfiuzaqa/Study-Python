import random
from datetime import datetime

class Funcionario:
    def __init__(self, nome, idade, data_aniversario):
        self.nome = nome
        self.idade = idade
        self.data_aniversario = data_aniversario
        self.data_registro = datetime.now().strftime("%d/%m/%Y")
        self.cartao = self.sortear_cartao()

    def sortear_cartao(self):
        cartoes = ['R$50,00', 'R$250,00', 'R$120,00']
        return random.choice(cartoes)

    def apresentar(self):
        print(f"Olá {self.nome}, seu registro foi concluído com sucesso no dia {self.data_registro}. Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de {self.cartao}")


def main():
    nome = input("Digite o nome do usuário: ")
    idade = int(input("Digite a idade do usuário: "))
    data_aniversario = input("Digite a data de aniversário do usuário no formato dd/mm/aaaa: ")

    funcionario = Funcionario(nome, idade, data_aniversario)
    funcionario.apresentar()


if __name__ == "__main__":
    main()