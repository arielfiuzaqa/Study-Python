'''Herança - permite que uma classe (chamada de classe filha ou subclasse) herde as características (atributos e métodos) 
de outra classe (chamada de classe pai ou superclasse). Isso significa que a classe filha pode reutilizar e estender o 
comportamento da classe pai.'''
print('\nHerança Simples (Pai)\n')
class Camera:
    def __init__(self,marca,megapixels):
        self.marca = marca
        self.megapixels = megapixels

    def tirar_foto(self):
        print(f"A camera {self.marca} com {self.megapixels} Mpixels está tomando a foto")


print('\nFilha 1\n')
class Cameraceular(Camera):
    def __init__(self, marca, megapixels, quantidade_de_cameras):
        super().__init__(marca, megapixels) # Puxa os selfs da que você quer usar de outra class
        self.quantidade_de_cameras = quantidade_de_cameras # Estância já que essa propriedade não tem no outro mas nesse

    def aplicar_filtro(self, filtro):
        print(f'Aplicando Filtros {filtro}')

    def tirar_foto(self, camera_a_utilizar): # Novo metodo criado para mudar o método de como esta escrito o método tirar_foto - Mesmo nome do metodo do pai
        print(f"A camera {self.marca} com {self.megapixels} Mpixels está tomando a foto e utilizando camera #{camera_a_utilizar}")

camera_celular = Cameraceular('Sony','25mp', 4) # Colocando a class como uma variável com instâncias variaveis
camera_celular.aplicar_filtro('Azul')
camera_celular.tirar_foto(2) # Se deixar sem argumanto dar um erro por conta da modificação do metodo pai dentro da filha


print('\nFilha 2\n')
class CameraSeguranca(Camera): # Classe de rotação da camera - Vai herdar da class Camera também!
    def __init__(self, marca, megapixels, hr_max_de_grav): # Adicionado o parametro proprio de hora máxima de gravação
        super().__init__(marca, megapixels)
        self.hr_max_de_grav = hr_max_de_grav

    def rotacionar_camera(self, direcao): # Colocando uma nova "função de rotação"
        print(f'Rotacionando a camera para {direcao}')

cam_seg = CameraSeguranca('Anatel','3mb', 10)
cam_seg.tirar_foto()
cam_seg.rotacionar_camera('esquerda')


# Verificando se uma classe é subclasse de outra
print('\nVerificando Sub-class\n')
print(issubclass(CameraSeguranca, Camera)) # A que imagino que seja as classes (filho , pai)
print(issubclass(Cameraceular, Camera)) # A que imagino que seja as classes (filho , pai)


