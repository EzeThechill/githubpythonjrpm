# import math

# x = math.sqrt(16)
# print (x)
# x = math.factorial(5)
# print (x)
# print (math.pi)
# print (math.e)
#-------------------------------------------------------
# import random
# ## random.seed (42)
# print (random.random())
# print (random.randint(1, 10))

# numeros = [1,2,3,4,5]
# random.shuffle (numeros)
# print (numeros)
# frutas = ["kiwis", "manzanas", "platanos"]
# x = random.choice (frutas)
# print (x)
# x = random.choices (frutas, [6,5,1], k=2)
# print(x)

# population = range (0, 100)
# x = random.sample(population, 5)
# print(x)

# #Merseene Twister 2**19935 = 6,000 ( capacidad de Random )

# Actividades pagina 58 ___________________________________________


import random
#Eres profesor y tienes una lista de alumnos. ¿Qué función del 
#módulo random podrías usar para sacar un alumno aleatoriamente de la lista?


nombres= ['Arturo','Julio','Dani','Aurora','Roberto','Martina']
print (random.choice (nombres))

#¿Qué cambios harías para engañar a uno de los alumnos, siempre sacando su nombre, 
# aunque lo produzca aleatoriamente?

nombres= ['Arturo','Julio','Dani','Aurora','Roberto','Martina']
random.seed (10)
print (random.choice (nombres))

import math as m

x=15.6547

print(m.ceil(x)) # redondea hacia arriba
print(m.floor(x)) # redondea hacia abajo

print(m.pow(4,3)) # resuelve 4 elevado al cubo

print(m.gcd(8, 6)) # maximo comun divisor

print(m.factorial(4)) # 4*3*2*1 = 24

print(m.e) # constante de Euler
print(m.pi) # Constante pi