# def hola():
#     """
#     Esta funcion es para imprimir hola
#     """
#     print ("hola",end=" ") 
#     x= 10 ** 10
#     y= 23
#     result = x + y
#     return (result)

# hola() 
# res = hola ()
# print (res)
# print (help(hola)) 
# print(hola.__doc__) # metodos dunder DOUBLE UNDERSCORE
# for i in range (15) :
#     hola()

# def sobremi(nombre,edad):
#     print(f"Tu nombre es {nombre}")
#     print(f"Tu edad es {edad}")


# # main program
# if __name__ =="__main__" :   # __metodos dunder__ DOUBLE UNDERSCORE
#     sobremi("jose",60) 
#     sobremi("ana",26)    
#     sobremi("maria",24)

def sumar(x, y):
    resultado = x + y
    return resultado

def resta(x, y):
    resultado = x - y
    return resultado

def producto(x, y):
    resultado = x * y
    return resultado

def division(x, y):
    resultado = x / y
    return resultado

def square(x,y) :
    resultado = x*y
    return resultado

# main program
if __name__ == "__main__" :
    print ("\n")
    print ("Calculadora basica")
    print ("\n")

    operacion = 0
    while operacion !="q" :
        operacion = input (" ¿Que operacion quieres realizar ? \n +,-,*,/,superficie \n ( q para salir ) ")
        if operacion=="q" :
            break
        numero_1 = float(input("Introduce un numero: "))
        numero_2 = float(input("Introduce un numero: "))
        
        if operacion=="+" :
            resultado = sumar(numero_1,numero_2)
        elif operacion=="-" :
            resultado = resta(numero_1,numero_2)
        elif operacion=="*" :
            resultado = producto(numero_1,numero_2)
        elif operacion=="/" :
            resultado = division(numero_1,numero_2)
        elif operacion=="superficie" :
            resultado = square(numero_1,numero_2)
        print(f"El resultado es : {resultado:.2f}")
        print ("\n")

# ---------------------------------------------------