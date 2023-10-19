import os # navegar pelos arquivos na pasta e a biblioteca
import shutil #  mover os arquivos para pastas separadas com base em suas extensões.

# Caminho da pasta de downloads
pasta_downloads = 'C:\\Users\\14896\\Downloads'

# Itera sobre os arquivos na pasta de downloads
for filename in os.listdir(pasta_downloads):
    # Obtém o caminho completo do arquivo
    caminho_completo = os.path.join(pasta_downloads, filename)
    
    # Verifica se o caminho é um arquivo (não é uma pasta)
    if os.path.isfile(caminho_completo):
        # Obtém a extensão do arquivo (o que está após o último ponto)
        extensao = filename.split('.')[-1].lower()  # Converte para letras minúsculas

        # Define o diretório de destino com base na extensão
        destino = os.path.join(pasta_downloads, extensao)

        # Cria o diretório de destino se ele não existir
        if not os.path.exists(destino):
            os.mkdir(destino)

        # Move o arquivo para o diretório de destino - Com exceção de arquivos abertos
        try:
            shutil.move(caminho_completo, os.path.join(destino, filename))
        except (PermissionError, FileNotFoundError) as e:
            print(f"Não foi possível mover o arquivo {filename}: {str(e)}")

