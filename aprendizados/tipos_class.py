'''Variáveis de uma classe - Quais podem ser usadas e em quais momentos posso usa-lás. 
dentro de uma classe, você pode usar vários tipos de variáveis para armazenar diferentes 
tipos de dados. Aqui estão alguns exemplos de tipos de variáveis comuns em uma classe'''

'''Variáveis de Instância: 
Essas variáveis pertencem a instâncias individuais da classe e armazenam dados específicos 
para cada instância.'''

print('\nVariáveis de Instância\n')
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome  # Variável de instância
        self.idade = idade  # Variável de instância

pessoa1 = Pessoa("Alice", 25)
pessoa2 = Pessoa("Bob", 30)
print(pessoa1.nome)  # Acesso a uma variável de instância
print(pessoa2.idade)  # Acesso a outra variável de instância


'''Variáveis de Classe: 
Essas variáveis são compartilhadas entre todas as instâncias da classe e armazenam dados que 
são comuns a todas elas. '''

print('\nVariáveis de Classe\n')
class Carro:
    quantidade = 0  # Variável de classe compartilhada

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        Carro.quantidade += 1  # Incrementa a variável de classe

carro1 = Carro("Toyota", "Corolla")
carro2 = Carro("Honda", "Civic")
carro2 = Carro("Jaguar", "Polo")
print(Carro.quantidade)  # Acesso à variável de classe


'''Variáveis Locais: Dentro de métodos, você pode usar variáveis locais para armazenar dados 
temporários que só existem durante a execução do método.'''

print('\nVariáveis Locais\n')
class Matematica:
    def soma(self, a, b):
        print(int(input("Digite um número: ")))
        print(int(input("Digite outro número: ")))
        resultado = a + b  # Variável local
        return resultado

calculadora = Matematica()
resultado_soma = calculadora.soma(5, 3)
print(resultado_soma)


'''Variáveis Privadas (Atributos com Underline Duplo): Embora não seja estritamente um tipo de 
variável, é uma convenção em Python usar atributos com underline duplo (exemplo: self.__atributo_privado) 
para torná-los "privados" e acessá-los apenas dentro da classe.'''

print('\nVariáveis Privadas\n')
class Exemplo:
    def __init__(self):
        self.__atributo_privado = 42

    def obter_atributo_privado(self):
        return self.__atributo_privado

instancia = Exemplo()
print(instancia.obter_atributo_privado())  # Acesso ao atributo privado



'''Métodos Comuns VS Instância VS Classe'''

# Métodos Comuns - Utiliza os dados da instância atraves do self
print('\nMétodos Comuns\n')
class Computador:
    sistema_operacional = 'Windowns 11'

    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video

    def exibir_dados_do_computador(self):
        print(self.marca, self.memoria_ram, self.placa_de_video, self.sistema_operacional)


# Métodos de Classes(Class Methods) - Uteis para modificar as classes e como são instanciadas e cpm instâncias diferentes.
# Como configurar para cada cliente uma configuração diferente por exemplo. Vamos usar os defs anteriores para continuar
#print('\nMétodos de Classes(Class Methods)\n')
# cls(conversão) que dizer que estamos passando a classe inteira e não só a instância. Nesse caso vamos definir apenas a memoria_ram
    @classmethod
    def computador_escritorio(cls, memoria_ram):
        return cls('Dell', memoria_ram, 'Placa de Video de Baixo Custo,')
    @classmethod
    def computador_config_pesado(cls, memoria_ram):
        return cls('Dell', memoria_ram, 'Placa de Video Alto Nivel,')

# Config p/ clientes de escritório
comp_escritorio = Computador.computador_escritorio('8GB')
# Config. p/ clientes de trabalho pesado (games, video, 3D)
comp_trabalho = Computador.computador_config_pesado('16GB')
# Exibindo os dados
print('#############################################################')
comp_escritorio.exibir_dados_do_computador()
comp_trabalho.exibir_dados_do_computador()


# Métodos Estáticos(Static Methods) - Não utiliza as instâncias através do metodo self e não modificam através do cls
# Quando utilizamos várias vezes o mesmo código e queremos que se torne uma funcionalidade para sempre usar.
print('\nMétodos Estáticos(Static Methods)\n')
class Pc:
    sistema_operacional = 'Windowns 11'

    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video

    def exibir_dados_do_computador(self):
        print(self.marca, self.memoria_ram, self.placa_de_video, self.sistema_operacional)

    @staticmethod
    def rod_programa_pesado(memoria_ram):
        if memoria_ram >= 8:
            return True
        else:
            return False

# Criar uma instância da classe Computador
computador = Pc('Dell', '16GB', 'Placa de Video de Alto Nivel')

# Chamar o método estático a partir da instância
resultado = computador.rod_programa_pesado(10)
print(resultado)




