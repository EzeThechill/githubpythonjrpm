# class Fruta:

# #constructor=================================
#     def __init__(self, nombre, precio):
#         self.nombre = nombre
#         self.precio = precio
#         self.__iva =3 #encapsulacion = privado
#     def mostrar_fruta(self):
#         print(f" Mi fruta es un {self.nombre} y cuesta {self.precio*self.__iva} €/kg ")

# #instanciamos===============================
# kiwi=Fruta("kiwi", 5.69)
# mango=Fruta("mango", 2.99)

#==========================================
# actualizando e imprimiendo
# print(kiwi.nombre)
# kiwi.precio = 5
# print(kiwi.precio)
# print(mango.nombre)
# mango.precio = 2.59
# print(mango.precio)
#==========================================
# usando metodos
# mango.mostrar_fruta()
#==========================================
from os import system
class Empleado :
        def __init__(self,dni,nombre, apellido1, apellido2, salario, puesto):
            self.dni = dni
            self.nombre = nombre
            self.apellido1 = apellido1
            self.apellido2 = apellido2
            self.salario = salario
            self.puesto = puesto

        def mostrar_empleado(self):
            print(f"Empleado.(Apellidos, Nombre) {self.apellido1} {self.apellido2},{self.nombre}\nDNI: {self.dni} \nPuesto: {self.puesto} \nSalario {self.salario} €/brutos mes ")
        def mostrar_nombre(self) :
            print(f" Empleado.(Apellidos, Nombre) {self.apellido1} {self.apellido2},{self.nombre} ")
        def calculo_paga_navidad (self) :
            paga_navidad=self.salario*(1+0.05)
            print(f" Empleado.(Apellidos, Nombre) {self.apellido1} {self.apellido2},{self.nombre} \nExtra de Navidad {paga_navidad} € ")

lista_de_empleados = []

print=("ALTA DE NUEVO EMPLEADO")
print="======================"
retour=True
while retour==True :
    system=("cls")
    nombre = input("Nombre:")
    apellido1 = input("Primer Apellido:")
    apellido2 = input("Segundo Apellido:")
    dni = input("DNI:")
    salario = input("Salario:")
    puesto = input("Puesto:")
    empleado = Empleado(dni, nombre, apellido1, apellido2,salario, puesto)
    lista_de_empleados.append (empleado)
    
seguir=input("Nuevo Empleado ? s/n")
if seguir == "n" :
    retour=False
        

empleado.mostrar_empleado()
    



