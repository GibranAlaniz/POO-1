# Clase abstracta
from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass

    def describir(self):
        return f"Soy una figura con área {self.calcular_area()}"

# Ejercicio
from abc import ABC, abstractmethod

class Vehiculo(ABC):
    @abstractmethod
    def mover(self):
        pass

    @abstractmethod
    def detener(self):
        pass

    @abstractmethod
    def obtener_velocidad_maxima(self):
        pass

class Conducible(ABC):
    @abstractmethod
    def conducir(self):
        pass

    @abstractmethod
    def estacionar(self):
        pass

class Mantenible(ABC):
    @abstractmethod
    def revisar(self):
        pass

    @abstractmethod
    def reparar(self):
        pass

# Encapsulamiento
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    
    def get_nombre(self):
        return self.__nombre
    
    def set_edad(self, nueva_edad):
        if nueva_edad > 0:
            self.__edad = nueva_edad

persona = Persona("Juan", 25)
print(persona.get_nombre())

# Polimorfismo
class Animal:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza
    
    def hacer_sonido(self):
        return "Sonido genérico"

# Herencia
class Perro(Animal):
    def hacer_sonido(self):
        return "Guau guau"

perro = Perro("Firulais", "Doberman")
print(perro.nombre)
print(perro.hacer_sonido())
print(perro.raza)

def hacer_sonar(animal):
    print(animal.hacer_sonido())

gato = Animal("Gata", "Siames")
perro = Perro("Perro", "Labrador")

hacer_sonar(gato)
hacer_sonar(perro)

# Abstracción
class Figura(ABC):
    @abstractmethod
    def area(self):
        pass

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
        return self.lado * self.lado

cuadrado = Cuadrado(4)
print(cuadrado.area())
