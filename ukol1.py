import requests

name = input('Zadej ICO, pro ktere chces ziskat informace: ')
response = requests.get('https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/'+ name)
if response.status_code == 200:
    jsonresp = response.json()

    print(jsonresp['obchodniJmeno'])
    print(jsonresp['sidlo']['textovaAdresa'])
else:
    print(f"Status code odpovedi na request byl {response.status_code}")