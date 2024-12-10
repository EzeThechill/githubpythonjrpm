import sqlite3
import camiones_crul

def conexion_camiones():
    pass

def ver_camiones() :
    connection = sqlite3.connect("CAMIONES.db") # conectar a la BD
    cursor = connection.cursor()
    sql = "SELECT * FROM CAMIONES"
    cursor.execute(sql)
    filas = cursor.fetchall()
    demos = [camiones_crul.Camiones(*f) for f in filas] # umpacking

    for demo in demos :
        print(demo.ID, demo.TRUCK_NUMBER, demo.EURO_TYPE, demo.MODEL)

    connection.close() # cerramos BD

def alta_camiones():

    print("======================")
    print("= ALTA DE VEHICULOS  =")
    print("======================")

    truck_plate = input("Introduce nª Matricula: ")
    euro_tipo = input("Introduce Tipo Motor (EURO): ")
    modelo = input("Introduce Modelo Camion: ")


    connection = sqlite3.connect("CAMIONES.db")
    cursor = connection.cursor()
    sql = """
    INSERT INTO CAMIONES (TUCK_NUMBER, EURO_TYPE, MODEL)
    VALUES (?, ?, ?)
    """
    camiones = camiones_crul(truck_plate, euro_tipo, modelo )    
    cursor.execute(sql,(camiones.truck_plate, camiones.euro_tipo, camiones.modelo))
    
    connection.commit()
    connection.close()
    
def modificar_camines():
    pass

def borrar_camiones() :
    pass

def opciones():
    print("===================")
    print("MAESTRO DE CAMIONES")
    print("===================")
    creditos = 0
    while creditos == 0:
        menu = float(input("Introduce opcion\n1- Ver Registros.\n2- Nuevo Registro. \n3- Modificar Registro.  \n4- Borrar Regidtro \n0- Apagar Sistema\n"))
        match menu:
            case 1:
                ver_camiones()
            case 2:
                alta_camiones()
            case 3:
                pass
            case 4:
                pass
            case 0:
                print("Apagando sistema...")
                exit()
    return menu

# main

opciones()





