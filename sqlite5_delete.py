import sqlite3

class Demo :
    def __init__(self, ID, Name, Hint) :
        self.ID=ID
        self.Name = Name
        self.Hint = Hint

connection = sqlite3.connect("sqlite.db")

cursor = connection.cursor()

sql = """
DELETE FROM demo 
WHERE ID = ?
"""

cursor.execute(sql,(100,)) # ATENCION A LA COMA DESPUES DEL ID

connection.commit()

connection.close()