# Modulos

'''Crie um módulo chamado processamento_de_audio este módulo deverar ter 2 funções: aumentar_volume e diminuir_volume
Crie um segundo arquivo chamado app.py e importe o móduloe processamento_de_audio e use a função dentro dele.'''

from video import aumentar_volume as av, diminuir_volume as dv

av()
dv()


# Como usar o if__name_ == '__main__'

from video import ligar_carro
from video import ligar_moto

ligar_carro()
ligar_moto()

if __name__ == '__main__':
    print('Ligando Veiculos')
    print(f'Estamos no arquivo {__name__}')
