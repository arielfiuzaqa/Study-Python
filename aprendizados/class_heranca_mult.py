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
# MRO(Method Resolution Order)