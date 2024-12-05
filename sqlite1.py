import sqlite3

connection = sqlite3.connect("sqlite.db")

cursor = connection.cursor()

sql = "SELECT * FROM demo"

cursor.execute(sql)
filas = cursor.fetchall()
print(type(filas))

for fila in filas :
    print(fila[0])
    print(f" {fila[2]} ")

connection.close()