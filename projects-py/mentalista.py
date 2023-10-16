import random

# Cores
class colors:
    cyan = '\033[1;36m'
    white = '\033[1;97m'
    yellow = '\033[1;33m'
    end = '\033[0m'
    green = '\033[92m'
    red = '\033[91m'
    blue = '\033[94m'

# Funções
def gerar_num_aleatorio():
    return random.randint(1, 100)

def adivinhar_numero():
    num_aleatorio = gerar_num_aleatorio()
    tentativas = 0

    print(colors.cyan + "Bem-vindo ao jogo de adivinhar o número!" + colors.end)
    print(colors.white + "Tente adivinhar o número entre 1 e 100." + colors.end)

    while True:
        try:
            tentativa = int(input(colors.yellow + "Qual número estou pensando? " + colors.end))
            tentativas += 1

            if tentativa < num_aleatorio:
                print(colors.blue + "Tente um número maior." + colors.end)
            elif tentativa > num_aleatorio:
                print(colors.blue + "Tente um número menor." + colors.end)
            else:
                print(colors.green + f"Parabéns! Você acertou o número {num_aleatorio} em {tentativas} tentativas." + colors.end)
                jogar_novamente = input("Deseja jogar novamente? (sim/não): ")
                if jogar_novamente.lower() != "sim":
                    break
                else:
                    num_aleatorio = gerar_num_aleatorio()
                    tentativas = 0
        except ValueError:
            print(colors.red + "Por favor, digite um número válido." + colors.end)

if __name__ == "__main__":
    adivinhar_numero()
