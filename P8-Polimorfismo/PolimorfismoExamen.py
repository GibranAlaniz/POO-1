def hacer_sonidos(animales):
    for animal in animales:
        animal.hacer_sonido()

animales = [
    Animal("Animal genérico"),
    Perro("Rex"),
    Gato("Silvestre"),
    Perro("Max"),
    Gato("Luna")
]

hacer_sonidos(animales)