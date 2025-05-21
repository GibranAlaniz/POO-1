class pisto:
    def __init__(self, hielera, hielera2):
        self.__hielera=hielera
        self.hielera2=hielera2
    
    def pistear1(self):
        self.hielera = "Vaciar"
        return self.__hielera
    def pistear2(self):
        self.hielera2="mah, está vacia"
        return self.hielera2
fiesta = pisto ("carton en hielera", "Unas cuanta frias")
print(fiesta.pistear1())
print(fiesta.pistear2())