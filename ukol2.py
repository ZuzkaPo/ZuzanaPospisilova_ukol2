import requests
#nactu od uzivatele nazev, ktery budu hledat
name = input('Zadej nazev pro ktery chces vyhledat ICO: ')

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}
#vytvorim post request a odeslu
data = {'obchodniJmeno': name }
response = requests.post('https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat', headers=headers, json=data)
json_resp = response.json()
#stahnu si ciselnik pro polozku Pravniforma
data = {"kodCiselniku": "PravniForma", "zdrojCiselniku": "res"}
response_ciselniky = requests.post('https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ciselniky-nazevniky/vyhledat', headers=headers, json=data)
json_ciselniky = response_ciselniky.json()

#Bonusova cast
#vytvorim si vlastni ciselnik kde klic je ciselny kod a hodnota je slovni nazev 
muj_ciselnik = {}
for i in json_ciselniky['ciselniky'][0]['polozkyCiselniku']:
    muj_ciselnik[i['kod']] = i['nazev'][0]['nazev']

#zpracuju odpoved projdu seznam nalezenych subjektu a pro kazdy vypisu jeho nazev, ICO a pravni formu
print(f"  Pocet nalezenych subjektu: {json_resp['pocetCelkem']}")
for i in json_resp['ekonomickeSubjekty']:
    print(f"{i['obchodniJmeno']}, {i['ico']}, {muj_ciselnik[i['pravniForma']]}" )
