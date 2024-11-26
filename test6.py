# x = range (10, 16)
# print(list(x)) #[10, 11, 12, 13, 14, 15]
# y = range (12, 22,3)
# print(list(y)) #[12, 15, 18, 21]
# z = range (100, -1, -10)
# print(list(z)) #[100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
# print (z[0]) # [100]
# print (z[5]) # [50]
#=======================================================
# LISTAS Y/O ARRAY

# x = [6, 7, 8, "Hola", True ] # Lista = Mutable,ordenado, podemos cambiar valores
# y = (6, 7, 8, "Hola", True ) # Tuple = INMutable, ordenado
# z = {6, 7, "Hola", True } # Set = INMutable, sin orden , NO duplicados
# x.append(4)
# x.append("Mario")
# print(x) # [6, 7, 8, 'Hola', True, 36, 4, 'Mario']
# print(x[-1]) # devuelve el ULTIMO registro de la lista # Mario
# print(x[:3]) # devuelve los tres primeros valores
# print(x[3:6]) # devuelve los valores desde el 3 al 6
# y = x[3:6] # creamos una nueva lista con los valores del 3 al 6 de la lista x
# print(x[0:6:2])
# x.remove(x[0])
# print(x)
# for i in x:
#     print(i)
#==================================================
#EJERCICIOS 
# Index     0   1    2     3        4    5   
# Elements 10   50   20   "Hola"  "Agur" 99
# Dada la siguiente lista, ¿qué esperas recibir con los comandos…?
# x = [10, 50, 20, "Hola", "Agur", 99]
# print (x[2:4])  # 20, "Hola"
# print (x[::2]) # 10, 20, "Agur"
# print (x[3::]) # "Hola", "Agur, 99"
# print (x[::]) # todos los elementos
# print (x[::-1]) # todos los elementos orden inverso  
#---------------------------------------------------
#   Teniendo 2 listas x, y….¿qué esperas recibir?  
# x = [10, 20, 30, 30, 50]
# y = [50, 60, 70, 80]
# print(x+y) #[10, 20, 30, 30, 50, 50, 60, 70, 80]
# z = x +y 
# print(z) #[10, 20, 30, 30, 50, 50, 60, 70, 80] en nueva lista "z"
# x += y
# print(x) #[10, 20, 30, 30, 50, 50, 60, 70, 80] nuevos valores lista "x"
#=============================================================
# # Imprimir todos los alumnos(chicos y chicas)
# Imprimir todas las alumnas
# lista_de_alumnos = ["Jon", "Pablo", "Aitor", "Gorka", "Maria", "Isabel"]
# print("Jon" not in lista_de_alumnos)
# print("Todos los Alumnos")
# for alumno in lista_de_alumnos :
#     print(alumno)
# print("Solo las Chicas")
# for lista1 in lista_de_alumnos [4:] :
#     print (lista1)
#-----------------------------------------------------------
#¿Por qué usar un tuple?
# import timeit
# print(timeit.timeit(stmt='("red", "green", "blue")', number=1000000000)) # con Tuple 10.67
# print(timeit.timeit(stmt='["red", "green", "blue"]', number=1000000000)) # con Tuple 48.57
#------------------------------------------------------------
#Crear un tuple para controlar las estaciones del año. 
# Mostrar “verano”
# Mostrar toda la lista de estaciones
# estaciones = (Invierno, Primavera, Verano, Otoño)
# If x == ( "Verano") :

# REPASO ACTIVIDADES TUPLAS Y LISTAS

frutas = ("kiwi", "manzana", "naranja")
          
for fruta in frutas :
    print (fruta) 

#unpacking
# x, y, z = frutas 
# print (x)
# print (y)
# print (z)

# *x, z = frutas
# print (x) # ['kiwi', 'manzana']
# print (type(x)) #<class 'list'>
# print (z)
#-------------------------------------
# rgb = (145, 54, 11)
# coordenadas = (123, 5, 4)
# x, y, _ = coordenadas