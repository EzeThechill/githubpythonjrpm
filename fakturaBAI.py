
import requests
URL = "https://zergabidea.gipuzkoa.eus/WAS/HACI/HGFZergaBideaWEB/ticketbai/inicio?locale=es_ES"

r=requests.get(URL)
datos = r.json()
print(datos)