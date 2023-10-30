import requests
import time
import json
import os

# Usando e Salvo no replit
class TelegramBot():

  def __init__(self):
    #token = '6297401523:AAFbir_tq_ZeyzlfXZc8IXkaErQ_AbvoYuE'
    #self.url_base = f'https://api.telegram.org/bot{token}'

  # Iniciar o Bot
  def Iniciar(self):
    update_id = None
    while True:
      atualizacao = self.obter_mensagens(update_id)
      mensagens = atualizacao['result']
      if mensagens:
        for mensagem in mensagens:
          update_id = mensagem['update_id']
          chat_id = mensagem['message']['from']['id']
          eh_primeira_mensagem = mensagem['message']['message_id'] == 1
          resposta = self.criar_resposta(mensagem, eh_primeira_mensagem)
          self.responder(resposta, chat_id)

  # Obter mensagens
  def obter_mensagens(self, update_id):
    link_requisicao = f'{self.url_base}/getUpdates?timeout=100'
    if update_id:
      link_requisicao += f'&offset={update_id + 1}'
    resultado = requests.get(link_requisicao)
    return json.loads(resultado.content)

  # Criar uma resposta
  def criar_resposta(self, mensagem, eh_primeira_mensagem):
    mensagem = mensagem['message']['text']
    if eh_primeira_mensagem or mensagem.lower() == 'menu':
      return (
          f'''Olá Bem-Vindo a nossa Equipe. Digite o numero do produto que deseja saber mais sobre.{os.linesep}'''
          f'''1 - Café Caro{os.linesep}'''
          f'''2 - Café Quente{os.linesep}'''
          f'''3 - Café Árabe{os.linesep}''')
    if mensagem.lower() == '1':
      return (
          f'''O Café Caro é um café com cafeína e o aroma de café com cafeína. É um café com cafeína e o aroma de café com cafeína.{os.linesep}'''
          f'''\nConfirmar(s/n)?''')
    if mensagem.lower() == '2':
      return (
          f'''O Café Quente é um café com cafeína e o aroma de café com cafeína. É um café com cafeína e o aroma de café com cafeína.{os.linesep}'''
          f'''\nConfirmar(s/n)?''')
    if mensagem.lower() == '3':
      return (
          f'''O Café Árabe é um café com cafeína e o aroma de café com cafeína. É um café com cafeína e o aroma de café com cafeína.{os.linesep}'''
          f'''\nConfirmar(s/n)?''')
    if mensagem.lower() in ['s', 'sim']:
      return 'Pedido Confirmado!!'
    else:
      return 'Gostaria de Acessar o Menu? Digite "Menu"'

  # Responder às mensagens
  def responder(self, resposta, chat_id):
    # Enviar
    link_de_envio = f'{self.url_base}/sendMessage?chat_id={chat_id}&text={resposta}'
    requests.get(link_de_envio)


bot = TelegramBot()
bot.Iniciar()
