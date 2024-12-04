from os import system
system=("cls")

frutas = ["MANZANA", "pera", "NARANJA", "uva", "MELON"]
# lista = []
# for i in frutas :
#     if i.isupper() :
#         lista.append(i)
# print(lista)
# LIST COMPREHENSION  [  output /  bucle / condicion booleano ]
                                 # colecccion  opcional
lista_nueva = [f.lower() for f in frutas if f.isupper()]
print(lista_nueva)

numeros = [3, 54, -12, 4, -67, 99, -120]
lista_positiva = [f for f in numeros if f>0]
print(lista_positiva)

numbers = [2, 6, 7, 3, 4, 8]
pares = [f for f in numbers if f %2==0]
print (pares)

numbers_texto=["Par" if f %2==0 else "Impar" for f in numbers]
print(numbers_texto)

numeros1 = [1, 2, 3, 4, 5,6, 7, 8, 9, 10]
numeros_sqr = [g**2 for g in numeros1]
print(numeros_sqr)

notas= {"Alice" : 85, "Bob" : 70, "Charlie" : 95, "Diana" : 45}
aprobados={ k:v for k,v in notas.items() if v>49}
print(aprobados)