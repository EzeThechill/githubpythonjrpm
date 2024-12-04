import winsound

from os import system
system("cls")


class Guitar :
    def __init__(self, marca, cuerdas) :
        self.marca = marca
        self.cuerdas = cuerdas
    def tocar(self):
        print("vrmm, vrmm, vrmmm")
class ElectricGuitar(Guitar):
    def __init__(self,marca, cuerdas, color):
        super().__init__(marca, cuerdas)
        self.color = color
class BassGuitar(Guitar) :
    def __init__(self,marca, cuerdas, strap) :
        super().__init__(marca, cuerdas)
        self.strap = strap
    def tocar(self):
        print("brooo, brooo, brooo")
        winsound.Beep(750,400)
class Band:
    def __init__ (self, instrumentos):
        self.instrumentos = instrumentos
    def actuar(self) :
        for instrumento in instrumentos :
            instrumento.tocar()  


# g=Guitar("Les Pauls", 6)
# print("Guitar")
# print(g.marca) # en clase Padre
# print(g.cuerdas)
# g.tocar() # en clase Padre

# e=ElectricGuitar("Fender", 6, "rojo")
# print("ElectricGuitar")
# print(e.marca) # viene del padre
# print(e.color)
# e.tocar() # viene del padre 

# h=BassGuitar("Luna", 4,"Trenza")
# print("BassGuitar")
# print(h.marca) # viene del padre
# print(h.strap)
# h.tocar() # viene del padre 

instrumentos = [ElectricGuitar("Fender", 6, "rojo"),BassGuitar("Luna", 4,"Trenza")]
b = Band(instrumentos)
b.actuar()


