#Teniendo una lista de caracteres [“k”, “y”, “e”, “f”, “i”], 
# comprobar cada uno de los elementos para ver si es un vocal 
# (vocales = [“a”, “e”, “i” …]). 
# Mostrar True si es vocal y False si es constante.
# caracteres = ["k","y", "e", "f", "i"]
# vocales = ("a","e", "i","o", "u")
# for vocal in caracteres :
#     if vocal in vocales :
#         print(True, vocal)
#     else :
#         print(False, vocal)
#false k
#false y
#true e
#false f
#true i
# caracteres = ["k","y", "e", "f", "i"]
# vocales = ("a","e", "i","o", "u")
# for vocal in caracteres :
#     print (vocal in vocales)
#False
#False
#True
#False
#True   
#----------------------------------------------------
#Ana, Carlos y Maria van a pasar el fin de semana en un camping en Las Landas.
#Cada uno traerá diferentes cosas (saco de dormir, tienda, cantimplora, …). 
#Mostrar el equipamiento de cada uno, y al final, el equipamiento de todos. 
#Probablemente traerán una o más tiendas. 
#Al final, contar el número de tiendas que han traído todos.
# personas = ["Ana", "Carlos", "Maria"]
# x , y , z = personas
# lista_Ana = [x,"Saco de Dormir", "Tienda"]
# lista_Carlos = [y,"Navaja", "Cerillas", "Cuerda"]
# lista_Maria = [z, "Saco de Dormir", "Cerillas"]
# equipamiento = lista_Ana + lista_Carlos + lista_Maria
# print (lista_Ana)
# print (lista_Carlos)
# print (lista_Maria)
# print (equipamiento)
# print(" ,", equipamiento)
# print(equipamiento.count("Saco de Dormir"))  
# ------------------------------------------------------
# GESTION DE TIENDA
# Bienvenidos a mi tienda. Hoy tenemos especiales de:
#   manzanas
#   zumos
#   leche

# Introducir 
# “1” para ver todos los productos, 
# “2” para hacer una compra…”, 
# “3” para borrar un producto,

# mantenimiento de productos

print ("Buenos dias, bienvenidos a mi tienda.")
print ("Hoy tenemos especialidades:")
productos = ["manzanas", "zumos", "leche", "pera"]
productos_en_oferta = ["piña", "melocoton"]
print (5*(" "), "¿Que quieres hacer? :")
print ((10*" "), "1 .- Listar productos")
print ((10*" "),"2 .- Hacer una compra")
print ((10*" "),"3 .- Borrar un producto")
x=int(input("                                    Elije opcion:"))
if (x>3 or x<0 ) :
    print(5*(" "),"opcion invalida")
# Mostrar productos
if x == 1 :
    print ("Lista de Productos :")
    for i in productos :
        print (10*" ",i)
    print (" y en Oferta especial:")
    for i in productos_en_oferta :
        print (10*" ",i)
# Hacer compra
if x== 2 :
    print ("Hoy tenemos....")
    for i in productos :
        print (i)
    print ("y en oferta hoy.")
    for i in productos_en_oferta :
        print (i)
    compra = input ("¿Que quieres comprar? :")

    for j in productos+productos_en_oferta :
        if j==compra :
            print ("Las", j, "cuestan 10 €")
            print ("Aqui tienes tus",j ,".")
            dinero = int(input ("¿Dinero entregado? :"))
            print ("Su cambio", dinero-10,"Gracias" )
            if compra in productos :
                productos.remove (compra)
            else:
                productos_en_oferta.remove (compra)
            print (productos+productos_en_oferta)
if x==3 :
    print ("Productos en Tienda :")
    for i in productos :
        print (i)
    for i in productos_en_oferta :
        print (i)
    eliminar = input("¿Que producto quieres eliminar ? :")
    if eliminar in productos :
        productos.remove (eliminar)
    else:
        productos_en_oferta.remove (eliminar)
    print("Producto", eliminar,"eliminado")
    print("Gracias")
    print(productos+productos_en_oferta) 









    






            

    
