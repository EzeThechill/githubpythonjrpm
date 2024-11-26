#TIPOS DE DATOS
# nombreAlumno = "Hola" # Camel Case
# NombreAlumno = "Hola" # Pascal case
# nombre_alumno = "Hola" # snake case  => Standard Python
# comentario  = """
# puedes utilizar tres comillas para crear textos muy largos
# y udar varias lineas
# """

# x = 45.64567656636548658
# print(x)
# x = 45.64567656636549 # maximos decimales 15

# x = 46.65e-2
# print(x)
# x = 0.4665 #multiplica el numero por 10(e) elevado a -2

# x = 34565
# print(type(x))
# # class int
# i =  ( isinstance(x, int)) # devuelve un Booleano,True / False

# if i  # por defecto seria True, para comparar con Falso, hay que escribirlo i==False


# MUTABLE / INMUTABLE

# x = 1000

# print(id(x)) # identifica el lugar de la memoria de donde se aloja el dato
# # 1524905583216

# x = 2000
# print(id(x))
# # 1524908541552


# RECOLECTOR DE BASURA

# import gc
# x = 1000
# print("id de x:" , id(x))
# del x # es un candidato para la coleccion de basura
# gc.collect() # Lanzar manualmente el recolector de basura
# print("Garbage collection triggered")