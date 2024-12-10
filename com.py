import sqlite3
import camiones_crul

connection = sqlite3.connect("CAMIONES.db")
cursor = connection.cursor()
filas = cursor.fetchall()
demos = [camiones_crul.Camiones(*f) for f in filas] # umpacking
sql = "SELECT * FROM CAMIONES"
cursor.execute(sql)
for demo in demos :
    print(demo.ID, demo.TRUCK_NUMBER, demo.EURO_TYPE, demo.MODEL)
connection.close()