class Pajaro:
    def hacerSonido(self):
        return "Pío"

class Perro:
    def hacerSonido(self):
        return "Guau"

def sonidoAnimal(animal):
    print(animal.hacerSonido())

pajaro = Pajaro()
perro = Perro()

sonidoAnimal(pajaro)  # Pío
sonidoAnimal(perro)   # Guau
