class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre  # Atributo privado

    def obtenerNombre(self):
        return self.__nombre  # Acceso controlado

persona = Persona("Ana")
print(persona.obtenerNombre())  
