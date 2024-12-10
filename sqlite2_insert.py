import sqlite3

class Demo :
    def __init__(self, ID, Name, Hint) :
        self.ID=ID
        self.Name = Name
        self.Hint = Hint

connection = sqlite3.connect("sqlite.db")

cursor = connection.cursor()

sql = """
INSERT INTO demo (ID, Name, Hint)
VALUES (?, ?, ?)
"""
demo = Demo(101, " Mi Nombre", "Mi Pista")
cursor.execute(sql,(demo.ID, demo.Name, demo.Hint))

connection.commit()

connection.close()