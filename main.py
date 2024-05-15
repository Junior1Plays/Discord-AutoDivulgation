from colorama import Fore, Back, Style, init
import datetime
import json
import os
import pyperclip
import requests
import time

token = ''
invite = """"""
channels = {}

with open('token.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    token = conteudo

with open('invite.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    pyperclip.copy(conteudo)
    invite = pyperclip.paste()

with open('channels.json', 'r') as arquivo:
    conteudo = arquivo.read()
    channels = json.loads(conteudo)

init(autoreset=True)

def send_message(channel_id, div_server, message):
    if channel_id in channels[div_server]:
        body = {
            'content': message
        }
        headers = {
            "authorization": token
        }
        requests.post(f'https://discord.com/api/v10/channels/{channel_id}/messages', headers=headers, json=body)
        print(f"Divulgado no ID {channel_id} ({div_server})")

def imprimirChaves(json_data):
    for chave, subchaves in json_data.items():
        print(f"Enviando convites em: {chave}")
        for canal in subchaves:
            send_message(canal, chave, invite)

def send_messages():
    imprimirChaves(channels)
    
    agora = datetime.datetime.now()
    horario_daqui_a_5_minutos = agora + datetime.timedelta(minutes=5)
    horario_formatado = horario_daqui_a_5_minutos.strftime("%H:%M:%S")

    print(f"Próxima divulgação: {horario_formatado}")
    time.sleep(326)
    send_messages()
os.system('title Discord Auto-Div')

print(Fore.RED + 'Discord Auto-Div v1.0\nMade by Junior Schueller\n')

headers = {
    'authorization': token
}

userdata_req = requests.get('https://discord.com/api/v10/users/@me', headers=headers)
userdata_json = userdata_req.json()
print("Olá, " + Fore.CYAN + userdata_json['username'] + Fore.RESET + "!")
os.system('pause')

send_messages()
