# Herança Multinível
class Usuario:
    def __init__(self, nome, salario, profissao):
        self.nome = nome
        self.salario = salario
        self.profissao = profissao

    def registrar_funcionario(self):
        print(f"Cadastrando usuário {self.nome}")

class Gestor(Usuario):
    def __init__(self, nome, salario, profissao, setor_responsavel):
        super().__init__(nome, salario, profissao)
        self.setor_responsavel = setor_responsavel

    def definir_setor(self, setor):
        print(f'Definindo setor para {setor}')

usuario1 = Usuario('Camila', 5000, 'Analista de Software')
gestor = Gestor('Roberta', 7000, 'Gestora', 'Gesão de Projetos')

print(usuario1)

# Herança Multipla - Criar novas classes sem re-criar funcionalidades existentes

class Pessoa:
    nome = "Sou uma pessoa"

    def convidar(self):
        print('Olá sou uma pessoa, vamos ao evento?')

class Profissional:
    nome = "Sou um profissional"

    def convidar(self):
        print('Olá sou um Profissional, vamos ao evento?')

class AtorProfissional(Pessoa,Profissional):
    pass

ator_profissional = AtorProfissional()
ator_profissional.convidar()

print(AtorProfissional.mro())
# MRO(Method Resolution Order) - muito show -Fazer resumo depois.


# Métodos Mágicos(Magic Method, dunder method(double understand))
print('\nMétodos Mágicos(Magic Method, dunder method(double understand))\n')
class Pessoas:
    def __init__(self):
        self.nome = 'Sou uma pessoa'
        self.habilidades = ['habilidade 1', 'habilidade 2', 'habilidade 3']
    # Representação para programadores(chamado com método repr(pessoas))
    def __repr__(self):
        return 'Classe Pessoas com propriedades nome e habilidades'
    # O que deve ser mensurado para determinar a quantidade daquela classe (chamada pelo método(len(pessoas)))
    def __len__(self):
        return len(self.habilidades)
    # Representando a classe no formato de string de forma rápida
    def __str__(self):
        return f'{self.nome} com as habilidades {self.habilidades}'
    # Para descobrir quais o possíveis methods magics que temos basta usar dir

    # Definindo como as funções vão se comportar.
pessoa = Pessoas()
print(pessoa.nome)
print(repr(pessoa))
print(len(pessoa))
print(str(pessoa))
print(dir(pessoa)) # Trás todos os methods magics
