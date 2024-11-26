# resultado = int ( input("Introduce el resultado de tu examen : "))
# if resultado > 100 :
#     print("Error. Nota incorrecta)")
# elif resultado >90 :
#     print("Enhorabuena, tu nota es superior a la media")
# elif resultado >70 :
#     print("Enhorabuena, tu nota esta en la media")
# elif resultado > 50 :
#     print("Enhorabuena")
# elif resultado < 50 :
#     print("Estas por debajo de lamedia")
# ========================================================================
# peso = int (input ("Introduce tu peso (kg) : "))
# altura = float(input ("Introduce tu estatura (mts) : "))
# imc_user = peso/altura*altura
# if imc_user > 30 :
#     print ("Sobrepeso")
# if imc_user > 24 and imc_user < 30:
#     print ("Obeso")
#=========================================================================
# ACTIVIDADES PAGINA 13
#------------------------------------------------------------
# nombre1= input("Introduce tu nombre : ")
# edad1 = int(input("Introduce tu edad : "))
# sueldo1 = int (input("Cual es tu sueldo :"))
# print ("Cumpliras",(edad1+1),"en tu siguiente cumpleaños. ","Tu salario es", (sueldo1),"EUR")
#------------------------------------------------------------
# compD = input("¿Comose llama tu compañero de la derecha? : ")
# compI = input("¿Comose llama tu compañero de la Izquierda? : ")
# print("Tus compañeros son, a la izquierda",(compI),"y a la derecha",(compD), ".")
#------------------------------------------------------------
# nombre2 = input("Introduce tu nombre : ")
# edad2 =int (input ("Introduce tu edad : "))
# print ("Hola", (nombre2), ". Tienes", (edad2), "años")
#------------------------------------------------------------
# print ("Hola", 2023, "Agur", 5_000_000_000)
#============================================================
# COMO   un estudiante de primaria
# QUIERO un programa para calcular el area de un rectangulo
# PARA QUE no tenga que aprender laformula
# largo = float(input(" Introduce el largo de tu rectangulo (cm) : "))
# ancho = float(input(" Introduce el ancho de tu rectangulo (cm) : "))
# print (f" La superficie del rectangulo es:{(largo*ancho):.2f} cm2")
#============================================================
# COMO   turista americano
# QUIERO convertir la temperatura de celsius a farenheid
# PARA QUE interprete mejor latemperatura del agua
temperatura = float(input("Introduce la temperatura del agua: "))
unidad = input("Elige la unidad de temperatura ( C = Celsius / F = Farenheit) : ")
print (f"La temperatura actual es de", temperatura, unidad)
if unidad == "C" :
    print(f"La temperatura en Grados Ferenheit {temperatura*9/5+32:.2f} F .")
elif unidad == "F" :
    print(f"La temperatura en Grados Celsius {((temperatura-32)*5/9):.2f} C .")
else:
    print("Lo siento no entiendo tus datos")