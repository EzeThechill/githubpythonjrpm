import sqlite3

class Demo :
    def __init__(self, ID, Name, Hint) :
        self.ID=ID
        self.Name = Name
        self.Hint = Hint


connection = sqlite3.connect("sqlite.db")

cursor = connection.cursor()

sql = "SELECT * FROM demo"

l)
filas = cursor.fetchall()
print(type(filas))

demos = [Demo(*f) for f in filas] # umpacking

for demo in demos :
    print(demo.ID, demo.Name, demo.Hint)

connection.close()