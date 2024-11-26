# def hacer_cafe(tipo_de_cafe="café", tamano="normal"):
    
#     print(f"Hemos hecho  {tipo_de_cafe} {tamano}")

# if __name__ == "__main__" :
#     tipo_de_cafe=input("que cafe ?: ")
#     tamano=input("que tamaño ?: ")    
#     hacer_cafe (tipo_de_cafe,tamano)
#     hacer_cafe ()
#----------------------------------------------------

# def calcular_precio(precio):
#     return precio * 2

# if __name__ == "__main__" :
#     precio = 5
#     x = calcular_precio(precio)
#     print(x) # resultado 10
#     print(precio) # resultado 5

# lista_de_precios = [1, 5, 8]
# def cambiar_lista_precios(lista_de_precios) :
#     lista_de_precios.append(3)
#     print(lista_de_precios)
#     return lista_de_precios

# if __name__ == "__main__" :
#     cambiar_lista_precios(lista_de_precios) # [1, 5, 8, 3]
#     print(lista_de_precios) #[1, 5, 8, 3]

# atencion con los MUTABLES en listas que se "actualizan" en la funcion
#----------------------------------------------------------------------
#Como portero de Pacha: comprobar la 3edad de los usuarios
# prohibido < 18 y avisar a los >65 sitio muy ruidoso

def control_edad(edad) :
    print(f"Tu edad es {edad}")

edad=26
if __name__ == "__main__" :
    edad = input ("¿Cual es tu edad? :")
    match edad :
        case _ if edad <18 :
            print ("No tienes edad minima. No puedes pasar")
        case _ if edad >64 :
            print ("Bienvenido,puedes pasar,el sonido esta muy alto y el ambiente es multitudinario.")
        case _:
            print(" ok")
        
        

