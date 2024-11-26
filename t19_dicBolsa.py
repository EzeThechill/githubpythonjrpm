import os
os.system('cls' if os.name == 'nt' else 'clear')

# Llevar a cabo las siguientes tareas, 
# usando estos datos de acciones en la bolsa española:
#   Crear un diccionario para almacenar las acciones en VERDES y su precio actual. 
#   Mostrar el valor de BBVA (print())
#   Después, usando update(), agregar las acciones en ROJO. 
#   Sumar el total de precios y imprimirlo al final
#   Excluir SANtander del cálculo total de 


bolsa_verde = {"AENA":143.50,"BBVA":6.34,"REP":14.22,"SAN":3.324}
bolsa_rojo ={"OHLA":0.518,"ANE":34.32,"TEF":3.811}
# Valor de repsol "REP":14.22
print(" Valor de Repsol")
print(bolsa_verde["REP"])

# Una sola lista con todos (verdes + rojos)
print("Una solo diccionarios verdes + rojos")
bolsa = bolsa_verde | bolsa_rojo
print(bolsa)
# Sumar los valor res
print("Suma de todos los valores")
total = 0
for v in bolsa.values() :
    total = total + v
print (total)

#   Imprimir los valores de cada acción en esta lista de acciones:

acciones = {"MSFT": [91.5, 54.1, 76.4], "REP": [7.91, 5.6, 6.7], "BBVA": [6.9,5.6,7.0]}

for k, v in acciones.items() :
    print (k)
    for i in v :
        print(i, end=" ")
