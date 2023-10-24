import random
import PySimpleGUI as sg
import os
import pygame  # Importe a biblioteca pygame para reproduzir música de fundo

class PassGen:
    def __init__(self):
        sg.theme('DarkBlue16')
        # Inicialize o mixer do pygame para reprodução de áudio
        pygame.mixer.init()

        # Layout da tela
        layout = [
            [sg.Text("Site ou Software", size=(20, 1), justification='center', font=('Helvetica',)),
             sg.Input(key='site', size=(20, 1))],
            [sg.Text("Nome do Usuario", size=(20, 1), justification='center', font=('Helvetica')),
             sg.Input(key='usuario', size=(20, 1))],
            [sg.Text("Tamanho da Senha", size=(20, 1), justification='center', font=('Helvetica')),
             sg.Combo(values=list(range(30)), key='total_chars', default_value=1, size=(3, 1)),
             sg.Output(size=(32, 5))],
            [sg.Button("Gerar Senha")]
        ]
        # Declarando a Janela
        self.janela = sg.Window('Password Generator', layout)

    def Iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED:
                break
            if evento == 'Gerar Senha':
                nova_senha = self.gerar_senha(valores)
                print(nova_senha)
                self.salvar_senha(nova_senha, valores)

    def gerar_senha(self, valores):
        char_list = 'ABCDEFGHIJKLMNOPQRSTUVXZabcdefghijklmnopqrstuvxz123456789@#$%&!?*'
        chars = random.choices(char_list, k=int(valores['total_chars']))
        new_pass = ''.join(chars)
        return new_pass

    def salvar_senha(self, nova_senha, valores):
        with open('senhas.txt', 'a', newline='') as arquivo:
            arquivo.write(f"site: {valores['site']}, usuario: {valores['usuario']}, nova_senha: {nova_senha}\n")

        print('Arquivo Salvo!')

gen = PassGen()
gen.Iniciar()
