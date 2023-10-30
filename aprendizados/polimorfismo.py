# Polimorfismo - Devem conseguir se adaptar ao tipo de dado que é passado para ela. Seja flexivel
# Podendo possuir várias formas e usavéis em várias atividades diferentes.
print(10 + 10)
print('Ola' + 'Devil')

# Outro exemplo
print(len('Livro'))
print(len([25,30,50]))
print(len({'Titulo': 'Livro1', 'Lançamento': '2021', 'Categoria': 'Lifestyle'}))


# Exemplo com funções
print('\nExemplo com Função\n')

class Carro:
    def ligar(self):
        print("Carro Ligou")
    
class Moto:
    def ligar(self):
        print("Moto Ligou")

def iniciar(veiculo):
    veiculo.ligar()

carro = Carro()
moto = Moto()

iniciar(carro)
iniciar(moto)


print('\nJeito interessante de chamar e usar uma função\n')
# Adaptando de acordo com a necessidade do que é dado, ou seja, polimorfa! Vai imprimirde acordo com o que eu fornecer agora
class Pessoa:
    def apresentar(self, nome, idade=None, profissao=None):
        if idade and profissao != None:
            print(f'{nome}, {idade}, {profissao}')

        elif idade != None:
            print(f'{nome}, {idade}')

        elif profissao != None:
            print(f'{nome}, {profissao}')

        else:
            print(nome)

pessoa = Pessoa()
pessoa.apresentar('João')
pessoa.apresentar('João', 19)
pessoa.apresentar('João', 40, 'Engenheiro')
pessoa.apresentar('Vagabunda', 23, 'Estressar')
