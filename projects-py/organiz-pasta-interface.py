import os
import shutil
import tkinter as tk
from tkinter import filedialog

# Função para organizar a pasta selecionada
def organizar_pasta():
    pasta_selecionada = filedialog.askdirectory()  # Abre uma janela de diálogo para selecionar uma pasta
    if pasta_selecionada:
        for filename in os.listdir(pasta_selecionada):
            caminho_completo = os.path.join(pasta_selecionada, filename)
            if os.path.isfile(caminho_completo):
                # Obtém a extensão do arquivo (o que está após o último ponto)
                extensao = filename.split('.')[-1].lower()
                
                # Obtém o diretório de destino com base no mapeamento de extensões
                destino = mapeamento_extensoes.get(extensao, 'Outros')
                
                # Cria o diretório de destino se ele não existir
                destino_path = os.path.join(pasta_selecionada, destino)
                if not os.path.exists(destino_path):
                    os.mkdir(destino_path)
                
                # Move o arquivo para o diretório de destino
                shutil.move(caminho_completo, os.path.join(destino_path, filename))
                print(f"Arquivo {filename} movido para {destino_path}")

# Mapeamento de extensões para diretórios de destino
mapeamento_extensoes = {
    'pdf': 'Documentos',
    'jpg': 'ImagensJPG',
    'mp3': 'Música',
    'zip': 'Arquivos Compactados',
    'txt': 'Textos',
    'exe': 'Programas',
    'rar': 'Arquivos Compactados',
    'docx': 'Documentos',
    'xlsx': 'Planilhas',
    'pptx': 'Presentações',
    'png': 'ImagensPNG',
    'gif': 'GIFs',
    'docx': 'DOCX'
    # Adicione mais extensões e diretórios conforme necessário
}

# Criar janela da interface
janela = tk.Tk()
janela.title("Organizador de Arquivos")

# Botão para selecionar a pasta e iniciar a organização
botao_selecionar = tk.Button(janela, text="Selecionar Pasta", command=organizar_pasta)
botao_selecionar.pack()

# Iniciar a interface gráfica
janela.mainloop()
