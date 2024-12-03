import winsound
from os import system
system("cls")

class Vehiculo :
    def __init__ (self, marca, modelo, combustible, autonomia_max,autonomia_act, averiado=False):
        self.marca=marca
        self.modelo=modelo
        self.combustible=combustible
        self.autonomia_max=autonomia_max
        self.autonomia_act=autonomia_act
        self.averiado=False

    def repostar (self, autonomia_anadida):
        self.autonomia_act = autonomia_act + autonomia_anadida

    def conducir(self) :
        if not self.averiado :
            if self.autonomia_act > 0 :
                self.autonomia_act=self.autonomia_act - 4
                print("Estas conduciendo")
                print(self.autonomia_act)
            else:
                print(f"Has agotado el combustible \nEl vehiculo esta averiado.\nLlama a tu taller")
                self.averiado= True
        else :            
            print("No puesdes conducir")


coche=Vehiculo("Ford", "KUGA", "Hibrido", 800, 20, averiado=False)

coche.conducir()
coche.conducir()
coche.conducir()
coche.conducir()
coche.conducir()
coche.conducir()
coche.conducir()
coche.conducir()

