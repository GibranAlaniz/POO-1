class Animal:
    def sonido(self):
        return "Hace un sonido"

class Gato(Animal):
    def sonido(self):
        return "Miau"

gato = Gato()
print(gato.sonido()) 
