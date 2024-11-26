# variables en linea
# x,y,z,nombre_de_alumno = 5,10,"Hello", "Maria"
# print(x)
# print(y)
# print(z)
# print(nombre_de_alumno)
# print(x, y, z,nombre_de_alumno)
#==============================================
# valor NONE

# x = None

# if x:
#     print ("x tiene valor")
# else:
#     print ("x no tiene nada")
#==============================================

# import sys
# i="hola mundo"
# print(sys.getrefcount(i)) #cuantas veces esta en la memoria la variable i
# j=i
# print(sys.getrefcount(i))
# del j
# print(sys.getrefcount(i))

#==============================================
# Bucles RANGE

# for i in range (5) :
#     print(f"Hola{i}")
#-------------------------------------
# repeticiones = 10
# for i in range (repeticiones) :
#     print(f"Hola {i+1}")
#-------------------------------------
# inicio = 10
# fin = 50
# salto = 2
# for i in range (inicio, fin, salto ) :
#     print(f"Hola {i+1}")
#------------ ( variable  _  indeterminada, no la vas a usar...)
# inicio = 10
# fin = 50
# salto = 2
# for _ in range (inicio, fin, salto ) :
#     print(f"Hola {_}")
#--------------------------------------------------------
# Ejercicios de uso de RANGE
#--------------------------------------------------------
#Usando range(), imprimir los números de cero a 100, pero en el siguiente formato:“numero X”

# for i in range (100) :
#     print("numero", (i) )
#--------------------------------------------------------
#Escribir los números pares empezando por 10 hasta 20. El resultado será 10, 12, 14, 16, 18, 20.

# for i in range (10, 22, 2) :
#      print("numero", (i) )
#--------------------------------------------------------
#Recibes un correo de tu compañero de trabajo a las 4PM un viernes.
# “Muchas gracias por ayudarme. 
# No he tenido tiempo para terminar estas dos tareas antes de irme de vacaciones. 
# ¿Me podrías ayudar?”
# programa para imprimir tu nombre 50 veces
# nombre = input("¿Cúal es tu nombre?")

# nombre = input("Cual es tu nombre :")
# repeticiones = int(input("Repeticiones :"))
# for i in range (repeticiones) :
#     print (nombre )

#Ayudar a tu primo/prima para hacer las matemáticas. 
# Hacer las multiplicaciones de 5 usando range(). 
# una tabla concreta
# tabla = int(input ("¿Que tabla de multiplicar quieres aprender ? :"))
# for i in range (0, 11) :
#     print (tabla," x",i, "=",tabla*i)
# todas las tablas de la del 0 al 10
# for j in range (0, 11) :
#     for i in range (0, 11) :
#           print (j," x",i, "=",j*i)
#---------------------------------------------------
#Hay que hacer un poco de análisis, para tus compañeros de Marketing. 
#El producto “ABC Widget” vale 10 euros con 51 centimos. 
#Si vendemos 1 producto, ganaremos 21,02 euros. 
#Si vendemos 3, 4 y 5? 
#Mostrar las ganancias para cada supuesta venta, usando range().
# abc_widget=float(10.51)
# unidades_vendidas = int(input("¿Cuentas unidades vas a vender?: "))
# for j in range (1,unidades_vendidas+1) :
#     print( j,"Unidades vendidas de ABC Widget generan un ingreso de : ", float(j*abc_widget))
#--------------------------------------------------------------
#accion = input("¿Introducir el texto 'up' para contar en positivo desde cero 
# o teclear 'down' para contar en negativo?")
#numeros_de_veces = int(input("¿Cuantas veces quieres repetir?"))
# La respuesta debería ser:
# 0, 1, 2, 3, 4 ….hasta numeros_de_veces para la accion up. 
# 4, 3, 2, 1, 0 desde numeros_de_veces, para la opcion down. 

# numeros_de_veces = int(input("¿Cuantas veces quieres repetir? :"))
# if numeros_de_veces < 0 :
#     print ( "Solo numeros enteros positivos,por favor")
# orden = input("¿Como quieres contar? (up/down) :")
# salto = int(input("¿Con que intervalo? :"))
# if orden == "up" :
#     for i in range (0, numeros_de_veces+1,salto) :
#         print(i)
# elif orden == "down" :
#     for j in range (numeros_de_veces,-1,salto*-1) :
#         print(j)
#--------------------------------------------------------
#Animaciones - Coche en movimiento - https://emojipedia.org/
#Queremos mostrar un coche en movimento, 
#conduciendo desde la izquierda del Terminal hasta la final. 
#Incrementar los espacios
#import time
#car = "\U0001F697"  # car = "🏎️"
#distancia = 10
# dentro del bucle,
# incrementar los espacios e imprimir el coche al final de los espacios. 
# Cada vez, se incrementan los espacios para simular que se mueve
# print(" " * posicion, end="")
# \r imprime denuevo desde elprincipio de lalinea
#-----------------------------------------------
# import time
# car = "\U0001F806"
# distancia = 90
# for position in range (distancia) :
#     print(" " * position, end = "")
#     print(car, end = "\r")
#     time.sleep(0.01)
#---------------------------------------------------------------
import time

start = time.perf_counter() # comenzar

for i in range(100000):
    pass

end = time.perf_counter() # terminar
print(f"Elapsed time: {end - start}")
