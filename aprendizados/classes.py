'''MÓDULO PROFISSIONAL DE CLASSES
Classes e Programação Orientada a Objetos (POO) são conceitos fundamentais em Python e na 
programação em geral.

Uma Classe em Python é um modelo para a criação de objetos. Ela define um conjunto de atributos 
(variáveis) e métodos (funções) que os objetos criados a partir dela possuirão. As classes são 
uma forma de organizar e estruturar o código, permitindo criar objetos que têm características 
e comportamentos específicos.

A POO é um paradigma de programação que se baseia no conceito de objetos e classes. Ela ajuda a 
organizar o código de uma maneira mais eficiente e orientada a objetos do mundo real. A POO se 
baseia em quatro princípios fundamentais:

Encapsulamento: A ideia de que um objeto deve encapsular seus próprios dados (atributos) e 
comportamentos (métodos), ocultando os detalhes internos e fornecendo uma interface para interação.

Herança: A capacidade de criar novas classes baseadas em classes existentes, permitindo 
reutilização de código e criação de hierarquias de classes.

Polimorfismo: A capacidade de objetos de diferentes classes responderem ao mesmo método de 
maneira única. Isso permite tratar objetos de diferentes classes de forma genérica.

Abstração: A simplificação de objetos complexos, fornecendo uma visão de alto nível de suas 
características e funcionalidades.

'''
# Classes



# Exemplo de Class 
print('\nExemplo de Class\n')
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ligado = False

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

meu_carro = Carro("Toyota", "Corolla", 2022)
meu_carro.ligar()
print(f"Marca: {meu_carro.marca}, Modelo: {meu_carro.modelo}, Ano: {meu_carro.ano}, Ligado: {meu_carro.ligado}")







