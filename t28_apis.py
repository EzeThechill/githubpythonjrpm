# #https://jsonplaceholder.typicode.com/
# import requests

# #user = input("Operario: ")
# URL="https://jsonplaceholder.typicode.com/posts"

# r=requests.get(URL)
# datos = r.json()
# print(type(datos))

# for i in datos :
#     print(i["title"])

import requests
from random import *

URL = "https://api.restful-api.dev/objects"

r=requests.get(URL)
datos = r.json()
a=(randint(1,10))
print(datos[a])


