import sqlite3

class Demo :
    def __init__(self, ID, Name, Hint) :
        self.ID=ID
        self.Name = Name
        self.Hint = Hint

connection = sqlite3.connect("sqlite.db")

cursor = connection.cursor()

sql = """
UPDATE demo 
SET Name = ?, Hint
WHERE ID = ?
"""

cursor.execute(sql,('Axl', 100))

connection.commit()

connection.close()