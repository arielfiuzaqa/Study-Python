# Modulo de Teste
# Importando o modulo imagem função tirar_foto, qualidade_maxima, Camera (* Puxa todas as funcionalidades, mas não recomendado)
from imagem import tirar_foto, qualidade_maxima, Camera
# o 'as' é uma forma de dar um apelido para a função que queremos puxar 
def iniciar_gravacao():
    print('Iniciando Gravação')

tirar_foto()
print(qualidade_maxima)
camera = Camera()

def aumentar_volume():
    print('Aumentando Volume')
def diminuir_volume():
    print('Diminuindo Volume')


def ligar_carro():
    print("Ligando Carro")

if __name__ == '__main__':
    print('Tirando o Lamborguinni da garagem')
    print(f'Estamos no arquivo {__name__}')

def ligar_moto():
    print("Ligando moto")

if __name__ == '__main__':
    print('Tirando a XR da garagem')
    print(f'Estamos no arquivo {__name__}')