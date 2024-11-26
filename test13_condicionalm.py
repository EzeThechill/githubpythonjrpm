# color = "rojo"
# # switch
# if color == "rojo" :
#     print("Your fauvorite colour is red")
# elif color == "azul" :
#     print("Your fauvorite colour is azul")
#-----------------------------------------------
# color = "verde"
# match color:
#     case "rojo" :
#         print("Your fauvorite colour is red")
#     case "azul" :
#         print("Your fauvorite colour is azul")
#     case "verde" :
#         print("Your fauvorite colour is verde")
#     case _ :
#         print("We dont know this colour")
#------------------------------------------------------

# eleccion=0
# eleccion=input("Que vas a tomar?: ")
# match eleccion :
#     case "Café" :
#         print ("Aqui esta su café. Son $2.50")
#     case "Té" :
#         print ("Aqui esta su Té. Son $1.80")
#     case "Jugo" :
#         print ("Aqui esta su Jugo. Son $2.50")
#     case "Sandwich" :
#         print ("Aqui esta su Sandwich. Son $4.50")
#     case "Muffin" :
#         print ("Aqui esta su Muffinh. Son $2.00")
    

eleccion=0
def conseguir_precio (producto) :
    match producto :
        case "Café" :
            return 2.50
        case "Té" :
            return 1.80
        case "Jugo" :
            return 2.50
        case _ :
            return 0
        
if __name__=="__main__" :
    











