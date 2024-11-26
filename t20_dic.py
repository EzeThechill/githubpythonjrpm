
temperaturas_medias = {
    "Enero": -5,
    "Febrero": -2,
    "Marzo": 4,
    "Abril": 10,
    "Mayo": 15,
    "Junio":20,
    "Enero": -7,
    "Julio": 25,
    "Agosto": 24,
    "Septiembre": 18,
    "Febrero": 2,
    "Octubre": 12,
    "Noviembre": 7,
    "Diciembre": 1
}

print(temperaturas_medias ["Diciembre"])

for k, v in temperaturas_medias.items() :
    if k == "Junio" or k=="Julio" or k=="Agosto" :
        print(k,v)

for k, v in temperaturas_medias.items() :
    if k in ("Junio", "Julio", "Agosto") :
        print(k,v)


# Eliminar Marzo
print(temperaturas_medias)
#del (temperaturas_medias["Marzo"])
temperaturas_medias.pop("Marzo")
print(temperaturas_medias)

# Temperaturas unicas
temperaturas_unicas=set(temperaturas_medias.values())
print(temperaturas_unicas)

# Diagrama de flujo

import a_limpia_ter
numero=int(input("introduce un numero:"))

if numero % 2 == 0 :
    print(f"{numero} es Par")
else :
    print(f"{numero} es Impar")
