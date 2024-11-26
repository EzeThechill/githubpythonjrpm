# implementation name
# python -m py_compile test9.py
# python -m dis test9.py

# numeros =[1, 6, 5, 8]

# for i in enumerate(numeros) :
#     print(f"{i}")
    
# for index, valor enumerate(numeros) :
#     print(f"{index}, {valor}")

# x = 2
# resultado = x*5
# assert resultado==6, "Error de calculo"


# i = 0
# while i<10 :
#     print(f"Hola", {i})
#     i=i+1

# i = 0
# while i<10 :
#     print(f"Hola", {i})
#     if i == 5:
#         break
#     i=i+1

# print ("fin de bucle" + str(i))

# i = 0
# while i<10 :
#     print(f"Hola", {i})
#     if i == 5:
#         continue #vuelve a la siguiente repeticion
#     i=i+1

# print ("fin de bucle" + str(i))

# Actividades básicas de while:
# Imprimir los valores desde 50 hasta 100.
# i=50
# while i<101 :
#     print(i,end="-")
#     i=i+1

#  
# Desde 5, imprimir los valores 5 a 20, pero excluye 12.

# i=5
# while i<21 :
#     if i != 12 :
#         print(i,end="-")
#     i=i+1


# Preguntar al usuario por números hasta que el usuario introduzca “q” para quit. 
# Sumar los valores e imprimir el resultado final. 

# num = input(" Introduce un numero ( Q para terminar) :")
# total=0

# while num !="q" :
#     total = total + int(num)
#     num = input(" Introduce un numero ( Q para terminar) :")

# print(f"El resultado final de la suma es: {total} " )
#------------------------------------------------------------
# OPCIONES DE MENU (2)
total=0
while True :
    num = input(" Introduce un numero ( Q para terminar) :")
    if num == "q" :
        break
    else : 
        total =total + int(num)
print(f"El resultado final de la suma es: {total:.2F} " )

