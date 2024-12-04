import t34_nominas
from os import system
system=("cls")
if __name__ == "__main__" :

    jon = t34_nominas.Empleado ("jon", 1000, "Analista")
    maria =t34_nominas.Programador ("Maria", 1500, "Programadora", "Python")
    empleados = [(jon,maria)]
    print(empleados)
    sistema = t34_nominas.Sistema_nominas(empleados)

    nominas = t34_nominas.Sistema_nominas(empleados)
    t34_nominas.calcular_nominas ()