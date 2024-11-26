# #Numeros / convertir x = float(3.145) en un tipo de datos int
# x=float(3.56)
# print(x)
# x=int(x)
# print(x)
#=============================================
# # Completar _ en el comentario (e simbolo para float) : #equivalente a 5.67*10^_, o 56700.0
# y=5.67e4
# print(y)
# # y= 56700.0
#============================================
# # Calculadora de propinas / total cuenta % propina / cuenta con propina por separado.
pre_entrantes = float(input ("Importe entrantes : "))
pre_primeros = float(input("Importe primeros : "))
pre_segundos = float(input("Importe segundos : "))
pre_postre = float(input("Importe postres : "))
total_s_iva=float(pre_entrantes+pre_primeros+pre_segundos+pre_postre)
print("Entrantes: ",pre_entrantes, "€")
print("Primeros: ",pre_primeros, "€")
print("Segundos: ",pre_segundos, "€")
print("Postres: ",pre_postre, "€")
print("Total cuenta : ", total_s_iva,"€")
print("IVA 7% :" ,total_s_iva*0.7 ,"€" )
print("TOTAL : " ,total_s_iva*1.07,"€")
prop=float(input("Propina % :"))
print(f("Propina: ", {total_s_iva*prop/100,"€"}:.3f))
print("Total a pagar:" ,total_s_iva*1.07+total_s_iva*prop/100,"€" ) "
#==================================================================
#CONTRL DE ACCESO
# USUARIO = "admin"
# PASSWORD = "password123"

# user_name = input("Introduce tu nombre de usuario: " )
# user_password = input("Contraseña: ")
# control_master = USUARIO + PASSWORD
# control_user=user_name+user_password
# if control_master==control_user :
#     print("Acceso admin permitido")
# else:
#     print("Acceso denegado")