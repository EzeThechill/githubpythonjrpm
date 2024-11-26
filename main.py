import random
from os import system

# Diccionario con preguntas y respuestas - key son preguntas, values son respuestas correctas
system("cls")
quiz_data = {
    "¿En qué película aparece la frase 'Yo soy tu padre'?": "Star Wars",
    "¿Qué película tiene el récord de ser la más taquillera de todos los tiempos (hasta 2024)?": "Avatar",
    "¿Quién dirigió la película 'El laberinto del fauno'?": "Guillermo del Toro",
    "¿Qué película presenta al personaje 'Jack Sparrow'?": "Piratas del Caribe",
    "¿Qué película animada está ambientada en el Día de los Muertos?": "Coco",
}
#hola
print("🎥 ¡Bienvenido al Quiz de Películas! 🎥")
print("Responde las siguientes preguntas para, \nponer a prueba tu conocimiento sobre películas.")
print("-" * 50)

#print("Mezclando la lista____________________________")
preguntas = list(quiz_data.keys()) # convertir los keys en una 
random.shuffle(preguntas) # usar un método de random para barajar las preguntas
#for i in preguntas :
    #print (i)
#print("Lista mezclada____________________________")
#print("\n")
aciertos=0
errores=0
for pregunta in preguntas: # bucle para iterar por todas las preguntas
    respuesta = input(pregunta)# preguntar al usuario por su respuesta
    if respuesta.lower() == quiz_data[pregunta].lower():
        #print ("Correcto")   # si su respuesta es igual que la del quiz_data, es correcto!
        aciertos = aciertos + 1    


print (f"Conseguiste {aciertos} de {len(quiz_data)}")


    # usar .lower() para comprarar

# al final, mostrar los numeros correctos