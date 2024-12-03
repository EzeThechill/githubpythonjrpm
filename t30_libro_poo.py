from os import system
system("cls")

class Libro:
    def __init__(self, titulo, isbn):
        self.titulo = titulo
        self.isbn = isbn

    def __str__(self):
        return f"Libro: {self.titulo} ISBN: {self.isbn}"
    
    def __eq__(self, other):
        return self.titulo == other.titulo and self.isbn == other.isbn

libro = Libro("Lord of the Rings", "123456x7h34")
libro1= Libro("Fundacion e Imperio", "987456v23n56")
libro2= Libro("Fundacion e Imperio", "987456v23n56")              
print(libro1 == libro2)




