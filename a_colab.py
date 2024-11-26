
# #PRIMERA CLASE

# markdown (instrucciones para dar formato a texto)\

# 12345
# print("Hola") # es un comentario
# # comebtario 1
# # assdfsd

# print("Hello Again")
# Hola
# Hello Again

# 12
# print("comentario adicion de celda ")

# comentario adicion de celda 

# 12
# x = 10
# y = "Hola"

# print(type(x))
# print(type(y))
# <class 'int'>
# <class 'str'>
# Importacion de LIBRERIAS (Modulos)


# import sys
# Usar LIBRERIAS (Modulos)

# print(sys.version)
# sys.version_info
# 3.10.12 (main, Sep 11 2024, 15:47:36) [GCC 11.4.0]
# sys.version_info(major=3, minor=10, micro=12, releaselevel='final', serial=0)
# Imprimir texto mas variable

# name = "Jose"
# edad = 60
# print("Mi nombre es" , name)
# print ("Mi edad es" , edad)
# #
# print("Mi nombre es " + name)
# print ("Mi edad es " + str (edad))
# #
# print ("Mi nombre es " + name + " y mi edad es " + str(edad))
# print (f"Mi nombre es {name} y mi edad es {str(edad)}")
# Mi nombre es Jose
# Mi edad es 60
# Mi nombre es Jose
# Mi edad es 60
# Mi nombre es Jose y mi edad es 60
# Mi nombre es Jose y mi edad es 60
# FORMULARIO

# Texto de título predeterminado


# # @title Texto de título predeterminado
# nombre1 = "Jose" # @param {"type":"string","placeholder":"NOMBRE"}
# print ( "Mi nombre es " + nombre1)
# nombre1:
# Jose
# Mi nombre es Jose
# Texto de título predeterminado


# # @title Texto de título predeterminado
# pais = "Chile" # @param ["España","Canada","Chile"] {"allow-input":true}
# edad1 = 45 # @param ["45","46","47"] {"type":"raw","allow-input":true}

# pais:
# Chile

# edad1:
# 45


# Programa de calculo de Costos.
# Suma de costes de productos.
# Jose R. Pablo
# 05/11/2024

# Suma de costes


# # @title Suma de costes {"run":"auto","vertical-output":true}
# cost_led = 10.1 # @param {"type":"number","placeholder":"Lampara Led p/u :"}
# cost_cable = 11.1 # @param {"type":"number","placeholder":"Cable p/mts :"}
# cost_regleta = 10.3 # @param {"type":"number","placeholder":"Regletas p/u"}

# cost_total = cost_led + cost_cable + cost_regleta

# print (f"El coste total es : {cost_total:.2f} euros")
# IVA=0.21
# print (f"El coste total con es IVA : {(cost_total*(1+IVA)):.2f} euros")
# #
# #tipos datos de las variables
# #print ( "Led : ",(type (cost_led)))
# #print ( "Cable : ",(type (cost_cable)))
# #print ( "Regleta : ",(type (cost_regleta)))
# #print ( "Total : ",(type (cost_total)))
# cost_led:
# 10.1
# cost_cable:
# 11.1
# cost_regleta:
# 10.3
# El coste total es : 31.50 euros
# El coste total con es IVA : 38.12 euros


# cost_led = int(input("Introduce el coste unitario del LED: "))

# if cost_led <= 10:
#     print("Mejor precio de LED")
# else:
#     print("El precio puede mejorar !")
#     print("Asi no venderas nada...")

# cost_cable = input("Introduce el coste por metro del CABLE: ")
# cost_regleta = input("Introduce el coste unitario de la REGLETA: ")
# print(str(cost_led))


# Introduce el coste unitario del LED: 14
# El precio puede mejorar !
# Asi no venderas nada...
# Introduce el coste por metro del CABLE: 12
# Introduce el coste unitario de la REGLETA: 16
# 14
# Condicional IF / ELSE
# Jose Ramon Pablo 05/11/2024


# nombre = input("Introduce tu USUARIO: ")

# if nombre == "Jose Ramon":
#     print("Bienvenido ", nombre)

# else:
#     print("No puedes acceder")
#     print("Adios")



# Introduce tu USUARIO: Paco
# No puedes acceder
# Adios
# Bucle WHILE
# Jose Ramon Pablo 06/11/2024


# [ ]
# 123456789101112131415
# acceso = 0
# while acceso < 3 :

#     nombre = input("Introduce tu USUARIO: ")

#     if nombre != "Jose Ramon":
#             print("No puedes acceder te quedan" , 2-acceso , "intentos")
#     else :
#             print("Hola," , nombre)
#             acceso = 4

# Introduce tu USUARIO: pepe
# No puedes acceder te quedan 2 intentos
# Introduce tu USUARIO: antonio
# No puedes acceder te quedan 1 intentos
# Introduce tu USUARIO: luis
# No puedes acceder te quedan 0 intentos
# Intentos agotados, contacta con el administrador

# import sys

# largo = float(sys.argv[1])
# ancho = float(sys.argv[2])
# print (f" La superficie del rectangulo es: {(largo*ancho):.2f} cm2")

#>> python area.py