from os import system
system("cls")

class Empleado :
    def __init__(self,nombre, sueldo, puesto):
        self.nombre = nombre
        self.sueldo = sueldo
        self.puesto = puesto
    def calcular_nomina (self) :
        return self.sueldo

class Programador(Empleado):
    def __init__(self,nombre,sueldo, puesto, lenguaje):
        super().__init__(nombre, sueldo, puesto)
        self.lenguaje = lenguaje 
    def calcular_nomina (self) :
        nomina = self.sueldo * 1.05
        return nomina   

class Sistema_nominas :
    # parametro - una lista de clase empleado
    def __init__(self, empleados) :
        self.empleados = empleados
    def calcular_nominas(self, empleados):
        for empleado in empleado :
            print (f"Nomina para {empleado.nombre} - {empleado.puesto}")
            nomina = round(empleado.calcular_nomina(),2)
            print (f"- $ :{nomina}")
            print =("")
            total = total + nomina
        print(f"Total a pagar : {total}")

