# for i in range (100) :
#     if i not in [10, 20, 30, 40, 50, 60, 70, 80, 90]:
#         Print(i,end="-")
#----------------------------------------------------------
# i=0
# while i < 100 :
#     if i !=i*10 :
#         print (i,end=" ")
#     i=i+1
#
#!/usr/bin/env pyton3  (para "elegir" configuracion del interprete) Shebang

# contrasena = " "
# nueva_contrasena = "*"

# while contrasena != nueva_contrasena :
#     contrasena=input("Introduczca la contraseña :")
#     nueva_contrasena=input("Introduzca la nueva_contrasena:")
#     if contrasena!=nueva_contrasena :
#         print ("Las contraseñas no coinciden !")

# print ("Contraseña cambiada correctamente")
        
#-------------------------------------------------

# from datetime import datetime

# ahora = datetime.now()

# print (ahora.strftime ("%d/%m/%y"))

# strptime ("2011-10-11")

#-----------------------------------------------------

#pedir al usuario su fecha de nacimiento
# por ej : 17 May 1989
# usar strptime()

# imprimirlo en formato YYYY-mm-dd
# formato Internacional Standard ( ISO 8601)
# extra : validacion fechqa pasada

from datetime import datetime
ahora = datetime.now()
print (ahora)
fecha_usuario = input("Intro la fecha en formato ej. 17 may 1966: ")
fecha_trabajo = datetime.strptime(fecha_usuario, "%d %b %Y")
if fecha_trabajo <= ahora :
    print(fecha_trabajo)
    print(fecha_trabajo.strftime("%Y-%m-%d"))
    print (ahora-fecha_trabajo)
else :
    print( "La fecha de nacimiento debe estar en el pasado")

#from datetime import datetime
#import locale
#locale.setlocale(locale.LC_TIME, "Spanish_spain.1252")
