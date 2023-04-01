import requests
import time

convite = input("Convite: ")
token = input("Token: ")
exp = ["1068292377539792987", "741289313614037092", "615658321780801558", "667407426516942859", "616006505245835273"]
explite = ["680848027870822405", "680848033378074644", "681143447771676775", "681143568559243285", "680848066823454737"]
divagora = ["954981586049306675", "954981570945642496", "954981557410607124", "834919284609777744"]
divelite = ["1074109938282020945", "1000060482243268768", "1005228529664925727", "993871733155172443", "993871320632791070", "993872066547818546", "1003706842456789032", "1074121968045006889", "1008381320793169941"]
div = ["1090380916553171054", "1090381190910972025"]

def sendinvite():
  body = {
    "authorization": token
  }
  invite = {
    "content": convite
  }
  for channel in exp:
    r = requests.post("https://discord.com/api/v10/channels/" + channel + "/messages", headers=body, data=invite)
    print("DIVULGADO NO CANAL " + channel + " DA EXP")
  for channel in explite:
    r = requests.post("https://discord.com/api/v10/channels/" + channel + "/messages", headers=body, data=invite)
    print("DIVULGADO NO CANAL " + channel + " DA EXP LITE")
  for channel in divagora:
    r = requests.post("https://discord.com/api/v10/channels/" + channel + "/messages", headers=body, data=invite)
    print("DIVULGADO NO CANAL " + channel + " DO DIVULGUE AGORA")
  for channel in divelite:
    r = requests.post("https://discord.com/api/v10/channels/" + channel + "/messages", headers=body, data=invite)
    print("DIVULGADO NO CANAL " + channel + " DO DIVULGAÇÃO & ELITE")
  for channel in div:
    r = requests.post("https://discord.com/api/v10/channels/" + channel + "/messages", headers=body, data=invite)
    print("DIVULGADO NO CANAL " + channel + " DO DIVULGUE!")
  time.sleep(18000)
  sendinvite()
sendinvite()
