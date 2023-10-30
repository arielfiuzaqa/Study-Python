# Classes Abstratas - Criando modelos a serem seguidos
# Criar um contrato(esqueleto) -> que deve ser implementado na classe que a herda
from abc import ABC, abstractmethod

class Camera(ABC):
    @abstractmethod
    def definir_tamanho_lente(self, tamanho):
        pass

class CameraProfissional(Camera):
    def definir_tamanho_lente(self, tamanho):
        print(f"Definindo o tamanho da lente {tamanho}mm")

camera_profissional = CameraProfissional()
camera_profissional.definir_tamanho_lente(5)

'''Desafio - 7.10'''
print('\nDesafio\n')

class Monitor(ABC):
    @abstractmethod
    def aumentar_claridade(self, valor):
        pass
    @abstractmethod
    def redeuzir_claridade(self, valor):
        pass

class MonitorFullHD(Monitor):
    def aumentar_claridade(self, valor):
        print(f'Aumentando a claridade em {valor} pontos')
    def redeuzir_claridade(self, valor):
        print(f'Reduzindo a claridade em {valor} pontos')

monitor = MonitorFullHD()
monitor.aumentar_claridade(20)
monitor.redeuzir_claridade(30)
